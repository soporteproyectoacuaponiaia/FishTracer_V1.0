# 🐟 Sistema de Trazabilidad de Crecimiento de Trucha Arcoíris mediante Visión por Computadora

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen.svg)

**Sistema no invasivo de monitoreo biométrico para acuicultura sostenible**

[Inicio Rápido](#-inicio-rápido) •
[Características](#-características-principales) •
[Documentación](#-📚-documentación-completa) •
[Publicación](##-publicación-científica) •
[Equipo](#-equipo-de-desarrollo)

</div>

---

## 📋 Tabla de Contenidos

- [Descripción General](#-descripción-general)
- [Características Principales](#-características-principales)
- [Tecnologías Utilizadas](#-tecnologías-utilizadas)
- [Requisitos del Sistema](#-requisitos-del-sistema)
- [Instalación Rápida](#-instalación-rápida)
- [Configuración Inicial](#-configuración-inicial)
- [Guía de Uso](#-guía-de-uso)
- [Arquitectura del Sistema](#-arquitectura-del-sistema)
- [Ventajas del Sistema](#-ventajas-del-sistema)
- [Publicación Científica](#-publicación-científica)
- [Equipo de Desarrollo](#-equipo-de-desarrollo)
- [Licencia](#-licencia)
- [Contacto](#-contacto)

---

## 🎯 Descripción General

Este proyecto es el resultado de una investigación académica desarrollada en el **Laboratorio Experimental de Sistemas Tecnológicos Orientados a Modelos Acuapónicos (LESTOMA)** de la **Universidad de Cundinamarca**, extensión Facatativá, Colombia.

El sistema implementa técnicas avanzadas de **visión por computadora** e **inteligencia artificial** para realizar el monitoreo no invasivo del crecimiento de truchas arcoíris (*Oncorhynchus mykiss*), eliminando la necesidad de manipulación manual que genera estrés y mortalidad en los peces.

### 🔬 Problema que Resuelve

En la acuicultura tradicional, el proceso de medición manual presenta varios desafíos:

- ⚠️ **Mortalidad del 1-2%** de las muestras debido al estrés por manipulación
- 💰 **Altos costos operativos** (50-60% del presupuesto es alimento)
- ⏱️ **Proceso lento y laborioso** que requiere personal especializado
- 📉 **Datos inconsistentes** por variabilidad en mediciones manuales
- 😰 **Estrés en los peces** que afecta su desarrollo y bienestar

### 💡 Solución Propuesta

Sistema automatizado que:

- 📸 Captura imágenes simultáneas desde dos cámaras (cenital y lateral)
- 🤖 Procesa automáticamente mediante algoritmos de Machine Learning
- 📏 Calcula dimensiones biométricas (largo, alto, ancho, peso)
- 💾 Almacena datos para trazabilidad histórica

---

## ✨ Características Principales

### 🎥 Sistema de Captura Dual
- **Cámara Cenital**: Vista superior para medir longitud y ancho
- **Cámara Lateral**: Vista lateral para medir longitud y alto
- Captura sincronizada en tiempo real
- Resolución Full HD (1080p)

### 🧠 Inteligencia Artificial
- **Detección semántica** del pez mediante Moondream (VLM)
- **Segmentación con SAM** del contorno del pez (MobileSAM)
- **Segmentación HSV** como fallback (visión clásica)
- **Corrección de distorsión óptica** mediante Ley de Snell adaptada a 3 medios
- **Precisión del 93%** en medición longitudinal (validado en investigación)

### 📊 Análisis Biométrico
- Cálculo automático de:
  - ✅ Longitud (cm)
  - ✅ Alto (cm)
  - ✅ Ancho/Espesor (cm)
  - ✅ Peso estimado (g)
  - ✅ Factor de condición K

### 💾 Trazabilidad Completa
- Almacenamiento de historial de crecimiento
- Asignación de ID único por medición
- Registro de fecha y hora
- Base de datos relacional
- Exportación de datos para análisis

### 🔧 Interfaz Amigable
- Visualización en tiempo real de ambas cámaras
- Modo manual y automático de captura
- Resultados instantáneos
- Panel de control intuitivo

---

## 🛠️ Tecnologías Utilizadas

### Lenguajes y Frameworks
- **Python 3.11+** - Lenguaje principal (recomendado)
- **OpenCV** - Procesamiento de imágenes (CPU + CUDA opcional)
- **NumPy** - Cálculos numéricos
- **PySide6 (Qt6)** - Interfaz gráfica moderna

### Inteligencia Artificial
- **Moondream** - Modelo de lenguaje visual (VLM) para detección semántica del pez
- **SAM (Segment Anything Model)** - MobileSAM para segmentación precisa del contorno
- **OpenCV HSV** - Segmentación clásica como fallback
- **Algoritmos personalizados** - Corrección óptica y calibración

### Base de Datos
- **SQLite** - Almacenamiento local de datos
- **JSON** - Intercambio de datos entre módulos

### Hardware Recomendado
- **Cámaras**: 
  - Logitech C930e (1080p Full HD)
  - Kisonli HD-1081 (1080p Full HD)
- **Procesador**: AMD Ryzen 7 5800XT o superior (8 núcleos, 4.8 GHz)
- **GPU**: NVIDIA GeForce RTX 4060 o superior
- **RAM**: 24 GB mínimo
- **Sistema Operativo**: Windows 11 (recomendado)

---

## 💻 Requisitos del Sistema

### Requisitos Mínimos
- **OS**: Windows 10/11 (64-bit)
- **Procesador**: Intel i5 o AMD Ryzen 5 (4 núcleos)
- **RAM**: 8 GB
- **GPU**: Opcional (NVIDIA RTX para aceleración, 100% funcional sin GPU)
- **Almacenamiento**: 5 GB libres
- **Python**: 3.10 o superior (3.11 recomendado)

### Requisitos Recomendados
- **OS**: Windows 11 (64-bit)
- **Procesador**: AMD Ryzen 7 o Intel i7 (8+ núcleos)
- **RAM**: 16-24 GB
- **GPU**: NVIDIA RTX 3060+ (opcional, para ~2.5x performance con CUDA)
- **Almacenamiento**: 10 GB libres (SSD recomendado)
- **Python**: 3.11+
- **Cámaras**: 2x Full HD 1080p (USB 3.0)

---

## 📚 Documentación Completa

### 🎯 Guías por Caso de Uso

| Necesitas... | Lee... | Audiencia |
|--|--|--|
| **Instalar en tu PC** | [INSTALL.md](INSTALL.md) | Usuarios finales |
| **Compilar ejecutable** | [BUILD_GUIDE.md](BUILD_GUIDE.md) | Desarrolladores |
| **Quick reference** | [BUILD_QUICK_REF.txt](BUILD_QUICK_REF.txt) | Todos (1 página) |
| **Activar GPU (opcional)** | [CUDA_SETUP.md](CUDA_SETUP.md) | Power users |
| **API y configuración** | [Config/Config.py](Config/Config.py) | Desarrolladores |

### 📖 Flujos de Trabajo

**👤 Soy usuario final, solo quiero usar la app:**
1. Lee [INSTALL.md](INSTALL.md) (5 min)
2. Ejecuta `build_exe.bat` → elige opción [2] (1 min)
3. Haz clic en "FishTrace" desde Desktop ✅

**👨‍💻 Soy desarrollador, necesito cambiar el código:**
1. Lee [INSTALL.md](INSTALL.md) sección "Instalación Manual" (5 min)
2. Haz cambios en el código
3. Ejecuta `python app.py` para probar (desarrollo)
4. Cuando esté listo, ejecuta `build_exe.bat` → opción [2] o [5]

**🚀 Necesito compilar para producción:**
1. Lee [BUILD_GUIDE.md](BUILD_GUIDE.md) (10 min)
2. Ejecuta `build_exe.bat` → opción [3] (requiere admin)
3. Instala en `C:\Program Files\FishTrace` automáticamente ✅

**⚡ Quiero activar aceleración GPU (opcional):**
1. Lee [CUDA_SETUP.md](CUDA_SETUP.md) (15 min)
2. Instala CUDA Toolkit + recompila OpenCV (30-60 min)
3. Ejecuta `build_exe.bat` → opción [2]
4. Sistema usa GPU automáticamente 🎮

---

## ⚡ Inicio Rápido

### 🎯 3 Pasos para Empezar

```batch
# 1. Ejecutar script de instalación
build_exe.bat

# 2. Seleccionar opción [2] o [3]
# [2] = Local + Desktop shortcuts
# [3] = Program Files (producción)

# 3. Esperar ~1 minuto → ✅ Listo
```

**Resultado:** Ejecutable compilado + accesos directos automáticos

---

## 🚀 Instalación Completa (Manual)

### Paso 1: Clonar el Repositorio

```bash
git clone https://github.com/stivencastro138/acuaponia-v1.002.git
cd acuaponia-v1.002
```

### Paso 2: Configurar API de Moondream

1. Obtén tu clave API gratuita de Moondream en: [https://moondream.ai/](https://moondream.ai/)
2. Crea un archivo `.env` en la raíz del proyecto:

```bash
# Crear archivo .env
notepad .env
```

3. Agrega tu clave API:

```env
MOONDREAM_API_KEY=tu_clave_api_aqui
```

### Paso 3: Compilar (Automático con build_exe.bat)

**Opción A: Instalación Automática Recomendada**

```bash
build_exe.bat
```

Elige una opción:
- **[1]** Local EXE (desarrollo)
- **[2]** Local + Desktop + Menú Inicio (testing) ⭐ **Recomendado**
- **[3]** Program Files + Desktop + Menú Inicio (producción, requiere admin)
- **[4]** Solo instalar dependencias
- **[5]** Limpiar y compilar desde cero

**⏱️ Tiempo estimado**: 1-2 minutos

**Opción B: Instalación Manual (para desarrollo)**

```bash
# Crear entorno virtual
python -m venv .venv
.venv\Scripts\activate

# Instalar dependencias
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

# Ejecutar
python app.py
```

### Paso 4: Ejecutar

Después de compilar con `build_exe.bat`:

```bash
# Opción 1: Desde Desktop (si elegiste opción [2] o [3])
# → Doble clic en "FishTrace" en Desktop

# Opción 2: Desde línea de comandos
.\FishTrace.exe

# Opción 3: Desde código (desarrollo)
python app.py
```

---

## ⚙️ Configuración Inicial

### 1. Calibración de Escalas (cm/píxel)

**PreCalibración por defecto:**
El sistema viene precalibrado para el túnel experimental de LESTOMA-UDEC:
- **Cámara Lateral**: 
  - Zona cercana: 0.00635786 cm/px (7 cm del lente)
  - Zona lejana: 0.01827964 cm/px (22 cm del lente)
- **Cámara Cenital**:
  - Zona cercana: 0.00507581 cm/px
  - Zona lejana: 0.01502311 cm/px

**Para ajustar calibración (si cambias cámaras o distancias):**
1. Abre la aplicación
2. Ve a **Configuración > Calibración de Escalas**
3. Usa el "Calibrador de Escala" con objeto de referencia conocido
4. Haz clic en "Aplicar Calibración Manual"
5. Los valores se guardan en `config.json`

### 2. Configuración del Túnel de Muestreo

**Distancias críticas (según diseño LESTOMA):**
- **Cámara a acrílico**: 7 cm (no cambies, es la validada)
- **Grosor del acrílico**: 0.4 cm (4 mm, material del túnel)
- **Profundidad del agua**: hasta 15 cm máximo

**Condiciones óptimas:**
- ✅ Fondo **blanco o verde claro** para mejor contraste HSV
- ✅ Iluminación uniforme y sin sombras (LEDs recomendado)
- ✅ Evita reflejos directos en el acrílico
- ✅ Agua limpia sin turbidez

### 3. API Key de Moondream (IA)

Requerida para detección automática:

```bash
# En Windows PowerShell (Como Administrador)
[System.Environment]::SetEnvironmentVariable("MOONDREAM_API_KEY", "tu_clave", "Machine")

# O crear archivo .env
echo MOONDREAM_API_KEY=tu_clave > .env
```

Obtén tu clave gratuita en: https://moondream.ai/

### 4. Opcional: ngrok para API remota

Si quieres acceso desde internet (captura desde móvil):

```bash
# PowerShell (Como Administrador)
[System.Environment]::SetEnvironmentVariable("NGROK_AUTHTOKEN", "tu_token", "Machine")

# O en .env
echo NGROK_AUTHTOKEN=tu_token >> .env
```

Obtén gratis en: https://ngrok.com/

---

## 📖 Guía de Uso

### Modo Manual

1. **Iniciar captura**:
   - Haz clic en "Captura Manual"
   - Espera a que el pez esté completamente dentro del túnel
   - Presiona "Capturar Frame"

2. **Procesamiento**:
   - El sistema detecta automáticamente el pez
   - Se aplica corrección óptica
   - Se calculan las dimensiones biométricas

3. **Guardar resultados**:
   - Revisa las mediciones en pantalla
   - Haz clic en "Guardar Medición"
   - Los datos se almacenan en la base de datos

### Modo Automático

1. **Activar modo automático**:
   - Ve a **Configuración > Modo de Captura**
   - Selecciona "Automático"
   - Define intervalo de captura (recomendado: cada 5 segundos)

2. **Monitoreo en tiempo real**:
   - El sistema detecta automáticamente cuando un pez pasa
   - Captura y procesa las imágenes
   - Guarda los resultados automáticamente

3. **Revisión de datos**:
   - Accede a **Trazabilidad > Historial**
   - Filtra por fecha, ID o rango de tamaño
   - Exporta datos a CSV o Excel

### Modo Remoto (API REST + Móvil)

FishTrace incluye API REST para captura remota desde dispositivos móviles u otro software:

**1. Activar API (con ngrok para acceso remoto):**
   - Ve a **Configuración > API REST**
   - Habilita "Servidor API"
   - (Opcional) Habilita ngrok si tienes NGROK_AUTHTOKEN configurado
   - Se genera URL pública para acceso remoto

**2. Endpoints disponibles:**
   ```
   POST /api/capture        → Enviar imagen para analizar
   GET  /api/measurements   → Obtener historial de mediciones
   POST /api/measurement    → Guardar nueva medición manualmente
   GET  /api/status         → Estado del sistema
   ```

**3. Captura desde móvil:**
   - Escanea QR en la ventana de configuración
   - Captura foto desde app móvil (iOS/Android)
   - La imagen se procesa en el servidor local
   - Resultado aparece en historial

**Nota:** Requiere opcional `NGROK_AUTHTOKEN` en `.env` para acceso remoto desde internet.

---

## 🏗️ Arquitectura del Sistema

```
┌─────────────────────────────────────────────────────┐
│                 ZONA DE MUESTREO                    │
│  ┌────────────┐        ┌────────────┐               │
│  │  TANQUE 1  │◄──────►│  TANQUE 2  │               │
│  └────────────┘        └────────────┘               │
│         │                     │                     │
│         │    ┌──────────┐     │                     │
│         └───►│  TÚNEL   │◄────┘                     │
│              │  DE PASO │                           │
│              └────┬─────┘                           │
│                   │                                 │
│         ┌─────────┴──────────┐                      │
│         │                    │                      │
│    ┌────▼────┐         ┌────▼────┐                  │ 
│    │ CÁMARA  │         │ CÁMARA  │                  │
│    │ CENITAL │         │ LATERAL │                  │
│    └────┬────┘         └────┬────┘                  │
└─────────┼───────────────────┼───────────────────────┘
          │                   │
          │     USB / Red     │
          └────────┬──────────┘
                   │
     ┌─────────────▼──────────────┐
     │  SISTEMA DE PROCESAMIENTO  │
     │                            │
     │  ┌──────────────────────┐  │
     │  │  MOONDREAM + SAM     │  │
     │  │  (Detección semántica│  │
     │  │   + Segmentación)    │  │
     │  └──────────┬───────────┘  │
     │             │              │
     │  ┌──────────▼───────────┐  │
     │  │  OpenCV + Algoritmos │  │
     │  │  (Segmentación)      │  │
     │  └──────────┬───────────┘  │
     │             │              │
     │  ┌──────────▼───────────┐  │
     │  │  Corrección Óptica   │  │
     │  │  (Refracción)        │  │
     │  └──────────┬───────────┘  │
     │             │              │
     │  ┌──────────▼───────────┐  │
     │  │  Cálculo Biométrico  │  │
     │  │  (L, A, An, Peso)    │  │
     │  └──────────┬───────────┘  │
     └─────────────┼──────────────┘
                   │
     ┌─────────────▼──────────────┐
     │      BASE DE DATOS         │
     │  ┌──────────────────────┐  │
     │  │  Historial           │  │
     │  │  Trazabilidad        │  │
     │  │  Imágenes            │  │
     │  │  Datos Biométricos   │  │
     │  └──────────────────────┘  │
     └────────────────────────────┘
```

### Estructura de Directorios

```
acuaponia-v1.002/
│
├── app.py                      # Punto de entrada de la aplicación
├── build_exe.bat              # Script de compilación a ejecutable
├── config.json                # Configuración guardada del usuario
├── requirements.txt           # Dependencias Python
├── logo.ico                   # Ícono de la aplicación
├── save_ok.wav               # Sonido de confirmación
│
├── BasedeDatos/              # Gestión de base de datos
│   ├── __init__.py
│   └── DatabaseManager.py    # ORM y operaciones SQLite
│
├── Config/                   # Configuración centralizada
│   ├── __init__.py
│   └── Config.py             # Constantes, calibración, API keys
│
├── Herramientas/            # Utilidades especializadas
│   ├── mobil.py             # API REST para captura desde móvil
│   └── SensorService.py     # Integración con sensores IoT
│
├── Modulos/                 # Módulos principales del sistema
│   ├── MainWindow.py         # Interfaz gráfica (PySide6)
│   ├── OptimizedCamera.py    # Control y sincronización de cámaras
│   ├── FishDetector.py       # Detección con HSV + CUDA opcional
│   ├── AdvancedDetector.py   # Detección avanzada con IA
│   ├── BiometryService.py    # Cálculos biométricos
│   ├── MorphometricAnalyzer.py # Análisis de dimensiones
│   ├── FrameProcessor.py     # Procesamiento async de frames
│   ├── ApiService.py         # REST API + ngrok para acceso remoto
│   ├── StatusBar.py          # Monitoreo de CPU/RAM/GPU
│   └── Otros módulos especializados
│
├── Resultados/              # Salida de mediciones
│   ├── Imagenes_Automaticas/ # Fotos de capturas automáticas
│   ├── Imagenes_Manuales/   # Fotos de capturas manuales
│   ├── CSV/                 # Exportación de datos
│   ├── Graficos/            # Gráficos generados
│   └── Reportes/            # Reportes en PDF
│
├── Eventos/                 # Logs del sistema
│   └── app.log              # Archivo de registro
│
└── .env (opcional)          # Variables de entorno
    # MOONDREAM_API_KEY = tu_clave
    # NGROK_AUTHTOKEN = tu_token (opcional, para API remota)
```

---

## 🌟 Ventajas del Sistema

### 🐟 Beneficios para los Peces

| Método Tradicional | Este Sistema |
|-------------------|--------------|
| ❌ Manipulación manual estresante | ✅ Completamente no invasivo |
| ❌ Mortalidad 1-2% | ✅ 0% mortalidad por medición |
| ❌ Riesgo de pérdida de mucosa protectora | ✅ Sin contacto físico |
| ❌ Interrupción del comportamiento natural | ✅ Monitoreo durante paso natural |
| ❌ Susceptibilidad a enfermedades | ✅ Ambiente no alterado |

### 💰 Beneficios Económicos

- **Reducción de costos de alimento**: Ajuste preciso de dosificación (ahorro del 10-15%)
- **Menor mortalidad**: Reducción del 1-2% de pérdidas por manipulación
- **Optimización de mano de obra**: Automatización del proceso de medición
- **Mejor tasa de conversión alimenticia**: Alimentación basada en datos precisos

### 📊 Beneficios Operativos

- **Datos más consistentes y precisos**: 93% de precisión en mediciones longitudinales
- **Monitoreo continuo**: Posibilidad de medir semanalmente sin estrés
- **Trazabilidad completa**: Historial detallado de cada pez
- **Escalabilidad**: Puede monitorear grandes poblaciones eficientemente
- **Información en tiempo real**: Decisiones basadas en datos actualizados

### 🔬 Beneficios Científicos

- **Investigación no destructiva**: Estudios longitudinales sin afectar a los sujetos
- **Gran volumen de datos**: Muestreos frecuentes y completos
- **Reproducibilidad**: Mediciones estandarizadas y objetivas
- **Correlación multivariable**: Análisis de múltiples parámetros simultáneos

---

## 📚 Publicación Científica

Este proyecto forma parte de una investigación publicada en:

**Título**: *"Implementation of a prototype desktop software based on computer vision for the growth traceability of rainbow trout fish (Oncorhynchus mykiss) in the LESTOMA-UDEC Laboratory"*

**Revista**: I+T+C: Investigación - Tecnología - Ciencia  
**Volumen**: 1, Número 19  
**Año**: 2025  
**ISSN**: e-ISSN: 2805-7201

### 📖 Resumen de la Investigación

La investigación validó el sistema mediante un estudio de **mes y medio** con **100 ejemplares** de trucha arcoíris, comparando mediciones automáticas vs. manuales:

**Resultados clave**:
- ✅ **93% de precisión** en medición longitudinal
- ✅ **10% de desviación** en estimación de peso
- ✅ **0% de mortalidad** durante las mediciones automatizadas
- ✅ **Reducción significativa** del tiempo de medición

### 🔍 Metodología Científica

El sistema implementa corrección de **distorsión óptica** mediante la Ley de Snell adaptada a 3 medios (aire, acrílico, agua):

**Constantes de refracción (definidas en Config.py):**

| Parámetro | Valor | Descripción |
|--|--|--|
| `N_AIRE` | 1.0 | Índice de refracción del aire |
| `N_ACRILICO` | 1.5 | Índice de refracción del acrílico del túnel |
| `N_AGUA` | 1.333 | Índice de refracción del agua |
| `DIST_AIRE` | 7.0 cm | Distancia cámara a la pared acrílica |
| `ESP_ACRILICO` | 0.4 cm | Espesor de la pared acrílica |
| `DIST_AGUA_MAX` | 15.0 cm | Profundidad máxima del agua en el túnel |

**Fórmula de corrección implementada:**

```python
# Camino óptico total (suma de distancias / índices de refracción)
dist_aparente = (DIST_AIRE / N_AIRE) + (ESP_ACRILICO / N_ACRILICO) + (dist_agua_actual / N_AGUA)

# Factor de corrección
factor_correccion = dist_aparente / dist_real

# Escala aplicada a píxeles para obtener medidas en cm
escala_final = escala_aire * factor_correccion
```

**Calibración espacial por zonas:**

El sistema realiza calibración en 2 zonas del túnel:
- **Zona cercana** (7 cm del lente): Escala cercan: 0.00635786 cm/px (lateral), 0.00507581 cm/px (cenital)
- **Zona lejana** (22 cm del lente): Escala lejana: 0.01827964 cm/px (lateral), 0.01502311 cm/px (cenital)

La escala se interpola linealmente según la posición vertical del pez, compensando la distorsión radial inherente a las lentes.

**Validación morfométrica:**

Todas las mediciones son validadas contra restricciones biológicas de trucha (*Oncorhynchus mykiss*):
- **Longitud**: 4-50 cm (rango normal para cultivo)
- **Factor K de Fulton**: 0.7-2.2 (tolerancia)  / 0.9-1.5 (óptimo)
- **Relación de aspecto**: 2.5-7.0 (largo/alto)
- **Solidez**: 0.75-0.97 (lleno del contorno)
- **Simetría**: mínimo 0.70 respecto al eje longitudinal

### 📄 Citar este Trabajo

Si utilizas este sistema en tu investigación, por favor cita:

```bibtex
@article{andrade2025,
  title={Implementation of a prototype desktop software based on computer vision for the growth traceability of rainbow trout fish (Oncorhynchus mykiss) in the LESTOMA-UDEC Laboratory},
  author={Andrade Ramírez, Jaime Eduardo and López Cruz, Ivone Gisela and Castro Martínez, Yeffersson Stiven and Flórez Lesmes, Alejandro},
  journal={I+T+C: Investigación - Tecnología - Ciencia},
  volume={1},
  number={19},
  year={2025},
  publisher={Universidad Comfacauca}
}
```

---

## 👥 Equipo de Desarrollo

### Investigadores Principales

<table>
  <tr>
    <td align="center">
      <strong>Jaime Eduardo Andrade Ramírez</strong><br>
      <em>Director del Proyecto</em><br>
      Universidad de Cundinamarca<br>
      📧 jeandrade@ucundinamarca.edu.co
    </td>
    <td align="center">
      <strong>Ivone Gisela López Cruz</strong><br>
      <em>Investigadora Principal</em><br>
      Universidad de Cundinamarca<br>
      📧 iglopez@ucundinamarca.edu.co
    </td>
  </tr>
  <tr>
    <td align="center">
      <strong>Yeffersson Stiven Castro Martínez</strong><br>
      <em>Desarrollador Principal</em><br>
      Universidad de Cundinamarca<br>
      📧 ystivencastro@ucundinamarca.edu.co<br>
      🔗 <a href="https://github.com/stivencastro138">GitHub</a>
    </td>
  </tr>
</table>

### 🏛️ Institución

**Universidad de Cundinamarca**  
Extensión Facatativá, Cundinamarca, Colombia

**Laboratorio**: LESTOMA (Laboratorio Experimental de Sistemas Tecnológicos Orientados a Modelos Acuapónicos)
---

## 📄 Licencia

Este proyecto está licenciado bajo la **Licencia MIT** - ver el archivo [LICENSE](LICENSE) para más detalles.

```
MIT License

Copyright (c) 2025 Universidad de Cundinamarca - LESTOMA

Se concede permiso, de forma gratuita, a cualquier persona que obtenga una copia
de este software y archivos de documentación asociados (el "Software"), para 
utilizar el Software sin restricciones, incluyendo sin limitación los derechos 
de usar, copiar, modificar, fusionar, publicar, distribuir, sublicenciar y/o 
vender copias del Software, y permitir a las personas a las que se les 
proporcione el Software hacer lo mismo, sujeto a las siguientes condiciones:

El aviso de copyright anterior y este aviso de permiso se incluirán en todas 
las copias o porciones sustanciales del Software.

EL SOFTWARE SE PROPORCIONA "TAL CUAL", SIN GARANTÍA DE NINGÚN TIPO...
```

---

## 📞 Contacto

### Soporte Técnico
- 📧 Email: ystivencastro@ucundinamarca.edu.co
- 🐛 Issues: [GitHub Issues](https://github.com/stivencastro138/acuaponia-v1.002/issues)

### Investigación y Colaboración Académica
- 📧 Email: iglopez@ucundinamarca.edu.co
- 🏛️ Laboratorio LESTOMA-UDEC

### Redes Sociales
- 🔗 GitHub: [@stivencastro138](https://github.com/stivencastro138)

---

## 🙏 Agradecimientos

Agradecimientos especiales a:

- **Universidad de Cundinamarca** por el apoyo institucional
- **Laboratorio LESTOMA-UDEC** por las instalaciones y recursos
- Comunidad de **OpenCV** y **Python** por las herramientas open-source
- Todos los **colaboradores** y **testers** del proyecto

---

## 📅 Roadmap

### Versión Actual (v1.2) ✅
- ✅ Sistema de captura dual de imágenes
- ✅ Detección automática con IA (Moondream + SAM/MobileSAM + HSV fallback)
- ✅ Corrección de distorsión óptica avanzada
- ✅ Cálculo de biometría completa (L, A, An, K, Peso)
- ✅ Base de datos local con trazabilidad
- ✅ Script de compilación profesional (5 opciones)
- ✅ CUDA detection y GPU acceleration (opcional)
- ✅ Documentación completa (4 guías + README)
- ✅ **Status: Production Ready**

---

## ❓ FAQ (Preguntas Frecuentes)

<details>
<summary><strong>¿Funciona con otras especies de peces?</strong></summary>

El sistema está optimizado para trucha arcoíris, pero puede adaptarse a otras especies con ajustes en los parámetros de calibración. Se requeriría reentrenamiento del modelo de IA para especies con morfología significativamente diferente.

</details>

<details>
<summary><strong>¿Necesito conocimientos de programación para usarlo?</strong></summary>

No. La interfaz gráfica está diseñada para ser intuitiva y no requiere conocimientos técnicos. Solo necesitas seguir la guía de instalación y calibración inicial.

</details>

<details>
<summary><strong>¿Puedo usar cámaras de otras marcas?</strong></summary>

Sí, el sistema es compatible con cualquier cámara USB que soporte resolución 1080p. Sin embargo, se recomienda calibrar específicamente para tu modelo de cámara.

</details>

<details>
<summary><strong>¿El sistema funciona en tiempo real?</strong></summary>

Sí, el procesamiento se realiza en tiempo real. El tiempo de análisis por pez es aproximadamente 2-3 segundos, dependiendo del hardware.

</details>

<details>
<summary><strong>¿Qué hago si la precisión es baja?</strong></summary>

1. Verifica la calibración de las cámaras
2. Asegúrate de que la distancia cámara-vidrio sea de 7 cm
3. Comprueba la iluminación (uniforme, sin reflejos)
4. Limpia el vidrio del túnel
5. Verifica que no haya burbujas en el agua

</details>

<details>
<summary><strong>¿Puedo exportar los datos?</strong></summary>

Sí, el sistema permite exportar a formato CSV, Excel y JSON para análisis posterior en otras herramientas.

</details>

---

<div align="center">

### ⭐ Si este proyecto te fue útil, ¡dale una estrella!

**Desarrollado con ❤️ por el equipo LESTOMA-UDEC**

[⬆️ Volver arriba](#-sistema-de-trazabilidad-de-crecimiento-de-trucha-arcoíris-mediante-visión-por-computadora)

---

**© 2026 Universidad de Cundinamarca - LESTOMA. Todos los derechos reservados.**

</div>
