"""
PROYECTO: FishTrace - Trazabilidad de Crecimiento de Peces
MÓDULO: Procesador de Video Asíncrono (FrameProcessor.py)
DESCRIPCIÓN: Implementa un hilo de ejecución independiente (Worker Thread) dedicado
             al procesamiento intensivo de imágenes. Desacopla la lógica de visión
             artificial (OpenCV/AI) del hilo de la interfaz gráfica (GUI Main Thread)
             para mantener la aplicación fluida y responsiva.
"""

import cv2
from PySide6.QtCore import QThread, Signal, QObject
import time
import queue
import logging
import numpy as np

from Config.Config import Config
from .FishDetector import FishDetector
from .FishTracker import FishTracker    
from .SimpleMotionDetector import SimpleMotionDetector
from .BiometryService import BiometryService

logger = logging.getLogger(__name__)

class ProcessorSignals(QObject):
    """Clase para agrupar todas las señales del procesador"""
    result_ready = Signal(dict)
    progress_update = Signal(str)
    ia_time_ready = Signal(float) 
    roi_status = Signal(bool)

class FrameProcessor(QThread):
    result_ready = Signal(dict)
    progress_update = Signal(str)  
    
    def __init__(self, moondream_detector_instance):
        super().__init__()
        self.signals = ProcessorSignals()
        self.queue = queue.Queue(maxsize=1)
        self.running = True
        
        # Módulos auxiliares
        self.chroma_detector = FishDetector() 
        self.tracker = FishTracker()
        self.motion_detector = SimpleMotionDetector(threshold=12)
        self.biometry_service = BiometryService(moondream_detector_instance)
        
        self.processing = False
        self.frame_count = 0
        self.skip_validation = False 
        self.capture_requested = False
        
        self.moondream_detector = moondream_detector_instance
        self._check_ai_status()

    def _check_ai_status(self):
        if self.moondream_detector and hasattr(self.moondream_detector, 'is_ready') and self.moondream_detector.is_ready:
            has_api = bool(getattr(self.moondream_detector, 'api_model', None))
            if has_api:
                self.signals.progress_update.emit("✅ IA Avanzada + fallback local listos.")
            else:
                self.signals.progress_update.emit("⚠️ Modo local (fallback clásico) activo.")
        else:
            self.signals.progress_update.emit("❌ Detector no disponible.")

    def add_frame(self, frame_left, frame_top, params):
        try:
            if not self.queue.empty():
                try: 
                    self.queue.get_nowait()
                except queue.Empty: 
                    pass
            
            self.capture_requested = True
            self.queue.put((frame_left, frame_top, params))
            return True 
        except Exception as e:
            logger.error(f"Error anadiendo frame a cola: {e}.")
            return False 

    def run(self):
        """Loop principal optimizado."""
        logger.info("FrameProcessor iniciado.")
        while self.running:
            try:
                frame_left, frame_top, params = self.queue.get(timeout=0.1)
                
                should_process = (
                    self.motion_detector.is_stable(frame_left) or 
                    self.capture_requested or
                    Config.DEBUG_MODE
                )
                self.capture_requested = False 

                if not should_process and not self.skip_validation:
                    if self.frame_count % 30 == 0:
                        motion_level = self.motion_detector.get_motion_level()
                        self.signals.progress_update.emit(
                            f"⏳ Esperando estabilidad... ({motion_level:.1f}%)"
                        )
                    
                    self.queue.task_done()
                    self.frame_count += 1
                    continue

                # Procesar frames
                self.signals.progress_update.emit("🔬 Iniciando análisis biométrico...")
                result = self.process_frames(frame_left, frame_top, params)
                
                if result:
                    self.result_ready.emit(result)
                    self.signals.result_ready.emit(result)
                else:
                    self.result_ready.emit({})
                
                self.queue.task_done()
                self.frame_count += 1
                
            except queue.Empty: 
                continue
            except Exception as e:
                logger.error(f"Error en FrameProcessor loop: {str(e)}.")
                self.result_ready.emit({'error': str(e)})

    def process_frames(self, frame_left, frame_top, params):
        try:
            start_time = time.time()

            scales = params.get('scales', {}) if isinstance(params, dict) else {}
            hsv_lateral = params.get('hsv_lateral', []) if isinstance(params, dict) else []
            hsv_cenital = params.get('hsv_cenital', []) if isinstance(params, dict) else []
            detection_params = params.get('detection', {}) if isinstance(params, dict) else {}

            scale_front_left = scales.get(
                'lat_front',
                params.get('scale_front_left', Config.SCALE_LAT_FRONT)
            )
            scale_back_left = scales.get(
                'lat_back',
                params.get('scale_back_left', Config.SCALE_LAT_BACK)
            )
            scale_front_top = scales.get(
                'top_front',
                params.get('scale_front_top', Config.SCALE_TOP_FRONT)
            )
            scale_back_top = scales.get(
                'top_back',
                params.get('scale_back_top', Config.SCALE_TOP_BACK)
            )

            if isinstance(hsv_lateral, (list, tuple)) and len(hsv_lateral) >= 6:
                hsv_left = {
                    'h_min': hsv_lateral[0],
                    'h_max': hsv_lateral[1],
                    's_min': hsv_lateral[2],
                    's_max': hsv_lateral[3],
                    'v_min': hsv_lateral[4],
                    'v_max': hsv_lateral[5]
                }
            else:
                hsv_left = {
                    'h_min': params.get('hue_left_min', Config.HSV_H_MIN),
                    'h_max': params.get('hue_left_max', Config.HSV_H_MAX),
                    's_min': params.get('sat_left_min', Config.HSV_S_MIN),
                    's_max': params.get('sat_left_max', Config.HSV_S_MAX),
                    'v_min': params.get('val_left_min', Config.HSV_V_MIN),
                    'v_max': params.get('val_left_max', Config.HSV_V_MAX)
                }

            if isinstance(hsv_cenital, (list, tuple)) and len(hsv_cenital) >= 6:
                hsv_top = {
                    'h_min': hsv_cenital[0],
                    'h_max': hsv_cenital[1],
                    's_min': hsv_cenital[2],
                    's_max': hsv_cenital[3],
                    'v_min': hsv_cenital[4],
                    'v_max': hsv_cenital[5]
                }
            else:
                hsv_top = {
                    'h_min': params.get('hue_top_min', Config.HSV_H_MIN),
                    'h_max': params.get('hue_top_max', Config.HSV_H_MAX),
                    's_min': params.get('sat_top_min', Config.HSV_S_MIN),
                    's_max': params.get('sat_top_max', Config.HSV_S_MAX),
                    'v_min': params.get('val_top_min', Config.HSV_V_MIN),
                    'v_max': params.get('val_top_max', Config.HSV_V_MAX)
                }

            contour_min_area = int(detection_params.get('min_area', Config.MIN_CONTOUR_AREA))
            contour_max_area = int(detection_params.get('max_area', Config.MAX_CONTOUR_AREA))
            confidence_threshold = float(detection_params.get('confidence', Config.CONFIDENCE_THRESHOLD))

            is_stable = self.motion_detector.is_stable(frame_left)
            if not is_stable and not self.skip_validation and not Config.DEBUG_MODE:
                return None

            self.signals.progress_update.emit("🧠 Analizando con BiometryService...")
            ia_start = time.time()
            
            try:
                metrics, img_lat_ann, img_top_ann = self.biometry_service.analyze_and_annotate(
                    img_lat=frame_left,
                    img_top=frame_top,
                    scale_lat_front=scale_front_left,
                    scale_lat_back=scale_back_left,
                    scale_top_front=scale_front_top,
                    scale_top_back=scale_back_top,                   
                    draw_box=Config.DEBUG_MODE,   
                    draw_skeleton=Config.DEBUG_MODE
                )

                if Config.DEBUG_MODE and img_lat_ann is not None:
                    cv2.imshow('DEBUG: Skeleton', img_lat_ann)
                    
            except Exception as e:
                logger.error(f"Error en BiometryService: {e}.")
                self.signals.progress_update.emit(f"❌ Error en análisis: {str(e)}")
                return None
            
            ia_time_ms = (time.time() - ia_start) * 1000
            self.signals.ia_time_ready.emit(ia_time_ms)
            # Añadir temporalmente para diagnosticar:
            import inspect
            sig = inspect.signature(self.tracker.update)
            logger.info(f"DEBUG: Firma detectada de update: {sig}")
            logger.info(f"DEBUG: Tipo de metrics: {type(metrics)}")

            # 3. VALIDACIÓN DE RESULTADOS
            if metrics is None or metrics.get('length_cm', 0) <= 0:
                self.signals.roi_status.emit(False)
                return None

            self.signals.roi_status.emit(True)

            # 4. EXTRACCIÓN DE CONTORNOS Y ACTUALIZACIÓN DEL TRACKER
            c_lat = self._retrieve_contour_for_tracker(
                frame_left,
                hsv_left,
                min_area=contour_min_area,
                max_area=contour_max_area
            )
            c_top = self._retrieve_contour_for_tracker(
                frame_top,
                hsv_top,
                min_area=contour_min_area,
                max_area=contour_max_area
            )
            
            try:
                self.tracker.update(
                    metrics=metrics,           # Pásalo primero y por nombre
                    contour_left=c_lat,
                    contour_top=c_top,
                    timestamp=start_time
                )
            except Exception as e:
                logger.error(f"Error en FishTracker.update: {e}")

            # 5. EMPAQUETADO DE RESULTADOS
            is_stable = self.motion_detector.is_stable(frame_left)
            smoothed_metrics = self.tracker.get_smoothed_measurement()
            tracking_stats = self.tracker.get_tracking_stats()
            tracking_count = len(self.tracker.measurements)
            confidence = self._calculate_confidence(metrics, is_stable, ia_time_ms)

            if tracking_count < Config.TEMPORAL_SMOOTHING_MIN_FRAMES:
                confidence = max(0.0, confidence - 0.05)

            box_lat = metrics.get('box_lat')
            box_top = metrics.get('box_top')

            return {
                'frame_left': img_lat_ann if img_lat_ann is not None else frame_left,
                'frame_top': img_top_ann if img_top_ann is not None else frame_top,
                'box_lat': box_lat,
                'box_top': box_top,
                'contour_left': c_lat,
                'contour_top': c_top,
                'detected_lat': c_lat is not None,
                'detected_top': c_top is not None,
                'metrics': metrics,
                'smoothed_metrics': smoothed_metrics,
                'tracking_count': tracking_count,
                'tracking_stats': tracking_stats,
                'is_consistent': tracking_stats.get('is_consistent', False),
                'confidence': confidence,
                'confidence_threshold': confidence_threshold,
                'processing_time': (time.time() - start_time) * 1000,
                'ia_time': ia_time_ms,
                'is_stable': is_stable,
                'status': metrics.get('status', 'OK')
            }

        except Exception as e:
            logger.error(f"Error critico en process_frames: {str(e)}", exc_info=True)
            return None

    def _retrieve_contour_for_tracker(self, clean_frame, hsv_params, min_area=500, max_area=None):
        """
        Acepta parámetros HSV específicos para la cámara

        """
        if clean_frame is None:
            return None
        
        try:
            lower = np.array([hsv_params['h_min'], hsv_params['s_min'], hsv_params['v_min']])
            upper = np.array([hsv_params['h_max'], hsv_params['s_max'], hsv_params['v_max']])
            
            # Convertir a HSV
            hsv = cv2.cvtColor(clean_frame, cv2.COLOR_BGR2HSV)
            
            # Crear máscara del FONDO 
            mask_background = cv2.inRange(hsv, lower, upper)
            
            # Invertir para obtener máscara del PEZ
            mask = cv2.bitwise_not(mask_background)
            
            # Limpieza morfológica
            kernel = np.ones((5, 5), np.uint8)
            mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
            mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
            
            if Config.DEBUG_MODE:
                cv2.imshow('DEBUG: Mask', mask)

            if mask is None or mask.size == 0:
                return None
            
            # Encontrar contorno
            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            
            # Filtro rápido de área
            if max_area is None or max_area <= 0:
                valid = [c for c in contours if cv2.contourArea(c) >= min_area]
            else:
                valid = [
                    c for c in contours
                    if min_area <= cv2.contourArea(c) <= max_area
                ]
            return max(valid, key=cv2.contourArea) if valid else None

        except Exception as e:
            logger.debug(f"No se pudo extraer contorno para tracker: {e}.")
            return None

    def _calculate_confidence(self, metrics, is_stable, ia_time_ms):
        """Calcula score de confianza."""
        confidence = 0.8
        
        if is_stable: confidence += 0.1
        if ia_time_ms > 3000: confidence -= 0.1
        
        tracker_stats = self.tracker.get_tracking_stats()
        if tracker_stats['is_consistent']: confidence += 0.05
        
        length = metrics.get('length_cm', 0)
        weight = metrics.get('weight_g', 0)
        
        if length < Config.MIN_LENGTH_CM or length > Config.MAX_LENGTH_CM: confidence -= 0.2
        if weight <= 0: confidence -= 0.1
        
        k_factor = metrics.get('condition_factor', 0)
        if 0.8 <= k_factor <= 1.8: confidence += 0.05
        
        return max(0.0, min(1.0, confidence))

    def stop(self):
        logger.info("Deteniendo FrameProcessor...")
        self.running = False
        try:
            while not self.queue.empty():
                self.queue.get_nowait()
                self.queue.task_done()
        except queue.Empty:
            pass
    
    def set_hsv_ranges(self, h_min, h_max, s_min, s_max, v_min, v_max):
        if hasattr(self.chroma_detector, 'set_hsv_ranges'):
            self.chroma_detector.set_hsv_ranges(h_min, h_max, s_min, s_max, v_min, v_max)
            logger.info(f"Rangos HSV actualizados.")