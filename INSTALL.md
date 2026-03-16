# 📦 Guía de Instalación - FishTrace v1.002

## 🎯 Requisitos del Sistema

### Hardware Mínimo
- **CPU:** Intel i5 / AMD Ryzen 5 o superior
- **RAM:** 8 GB mínimo, 16 GB recomendado
- **GPU:** Opcional (NVIDIA RTX series para aceleración)
- **Almacenamiento:** 500 MB + espacio para base de datos

### Software Requerido
- **Windows:** 10 / 11 (64-bit)
- **Python:** 3.10+ (3.11 recomendado)
- **pip:** Gestor de paquetes Python

### Cámaras Soportadas
- Cámaras USB estándar (OpenCV compatible)
- Configuración estéreo (2 cámaras recomendadas)

---

## 🚀 Instalación Rápida

### 1️⃣ **Clonar / Descargar el Repositorio**

```bash
# Opción A: Clonar desde Git
git clone https://github.com/tu-usuario/FishTrace.git
cd FishTrace

# Opción B: Descargar ZIP
# Descargar desde GitHub → Code → Download ZIP
# Descomprimir en carpeta deseada
```

### 2️⃣ **Crear Entorno Virtual**

```bash
# Crear entorno Python aislado
python -m venv .venv

# Activar entorno
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # macOS/Linux (si aplica)
```

### 3️⃣ **Instalar Dependencias**

```bash
# Actualizar pip
python -m pip install --upgrade pip setuptools wheel

# Instalar paquetes
pip install -r requirements.txt
```

### 4️⃣ **Configurar API Key (Moondream IA)**

```bash
# Crear archivo .env en la raíz del proyecto
echo MOONDREAM_API_KEY=tu_api_key_aqui > .env
```

Obtener API key: https://huggingface.co/

### 5️⃣ **Ejecutar la Aplicación**

```bash
python app.py
```

---

## 🎮 Activar Aceleración GPU (Opcional)

Si tienes GPU NVIDIA RTX y quieres **mejor performance**:

```bash
# Ver guía detallada
cat CUDA_SETUP.md
```

**Resumen rápido:**
```bash
# Desinstalar OpenCV actual
pip uninstall opencv-contrib-python -y

# Instalar con CUDA (si disponible)
pip install opencv-contrib-python-cuda
```

Si no está disponible, compilar localmente (ver `CUDA_SETUP.md`).

---

## ⚙️ Configuración Inicial

Cuando inicia FishTrace por primera vez:

1. **Calibración de Cámaras**
   - Aparecerá asistente de calibración en la pestaña "Calibración"
   - Seguir instrucciones en pantalla
   - Capturar imágenes de patrón de tablero de ajedrez

2. **Configuración de Sensores IoT** (Opcional)
   - Si tienes sensores conectados (API REST)
   - Configurar endpoints en "Configuración → Sensores"

3. **Preferencias de Interfaz**
   - Tema (Oscuro/Claro)
   - Tamaño de fuente
   - Densidad de elementos

---

## 📋 Estructura del Proyecto

```
FishTrace/
├── app.py                 # Punto de entrada
├── requirements.txt       # Dependencias
├── CUDA_SETUP.md         # Guía aceleración GPU
├── INSTALL.md            # Este archivo
├── Config/
│   └── Config.py         # Configuración global
├── Modulos/
│   ├── MainWindow.py     # UI principal
│   ├── FrameProcessor.py # Procesamiento async
│   ├── BiometryService.py
│   └── ...
├── BasedeDatos/
│   └── DatabaseManager.py
├── Herramientas/
│   ├── SensorService.py
│   └── mobil.py          # Captura desde móvil
├── Resultados/           # Mediciones guardadas
│   ├── Imagenes_Manuales/
│   ├── Imagenes_Automaticas/
│   └── CSV/
└── Eventos/
    └── app.log           # Logs de ejecución
```

---

## 🔗 Primeros Pasos

### **Modo Automático (Recomendado)**
1. Clic en **"Captura Automática"**
2. Sistema detecta pez automáticamente
3. Captura 5 frames y calcula biometría

### **Modo Manual**
1. Clic en **"Captura Manual"**
2. Colocar pez en cámara
3. Hacer clic en **"Capturar"**
4. Ajustar contorno manualmente si es necesario
5. Ingresar medidas adicionales (altura, peso)
6. Guardar

### **Modo Externo (Móvil)**
1. Activar servidor en **"Configuración"**
2. Scanear QR en app móvil
3. Capturar desde teléfono
4. Fotos se sincronizan automáticamente

---

## 🐛 Troubleshooting

### **Problema: "No suitable video device found"**

```
Error: No camera detected
```

**Solución:**
- Verificar que cámaras estén conectadas a USB
- Revisar en `Configuración → Cámaras`
- Cambiar índices de cámara si es necesario
- Reiniciar aplicación

### **Problema: "API Key inválida"**

```
Error: Moondream API authentication failed
```

**Solución:**
- Verificar fichero `.env` tiene `MOONDREAM_API_KEY=...`
- Obtener nueva key en https://huggingface.co/
- Reiniciar aplicación

### **Problema: "Faltan dependencias"**

```
ModuleNotFoundError: No module named 'torch'
```

**Solución:**
```bash
pip install -r requirements.txt --upgrade
```

### **Problema: Aplicación muy lenta**

**Solución:**
- Habilitar CUDA (ver `CUDA_SETUP.md`)
- Reducir resolución de cámaras
- Cerrar otras aplicaciones

---

## 📊 Monitoreo de Recursos

La aplicación muestra en **StatusBar** (parte inferior):
- **CPU:** Uso de procesador
- **RAM:** Memoria disponible
- **GPU:** Uso de videotarjeta (si CUDA activo)
- **VRAM:** Memoria de GPU (si CUDA activo)

**Valores normales:**
- CPU: 15-30% durante captura
- RAM: 500-800 MB
- GPU: 5-20% (si CUDA activo)

Si excede 90%, considerar:
- Reducir resolución
- Cerrar otras aplicaciones
- Compilar OpenCV con CUDA

---

## 📝 Archivos de Registro

Los logs se guardan en: `Eventos/app.log`

**Ver últimas líneas:**
```bash
tail -n 50 Eventos\app.log
```

**Buscar errores:**
```bash
findstr /I "ERROR" Eventos\app.log
```

**Buscar estado de CUDA:**
```bash
findstr /I "CUDA" Eventos\app.log
```

---

## 🔄 Actualización

Para obtener nuevas versiones:

```bash
# Descargar cambios
git pull origin main

# Reinstalar dependencias actualizadas (por si hay cambios)
pip install -r requirements.txt --upgrade
```

---

## 📞 Soporte

### Documentación
- Guía CUDA: `CUDA_SETUP.md`
- Config: `Config/Config.py` (ver constantes)
- Logs: `Eventos/app.log`

### Reportar Bugs
1. Revisar `Eventos/app.log`
2. Notar líneas con `ERROR` o `WARNING`
3. Copia la línea y contexto
4. Reporta en GitHub Issues

---

## 📄 Licencia

Ver fichero `LICENSE` en la raíz del proyecto.

---

**Última actualización:** 16 Mar 2026  
**Versión:** FishTrace v1.002  
**Estado:** Production Ready ✅
