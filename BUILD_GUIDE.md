# 🔨 Guía de Compilación - FishTrace v1.002

## 📋 Descripción

`build_exe.bat` es el script mejorado para **compilar**, **empaquetar** y **distribuir** FishTrace como ejecutable profesional.

Incluye:
- ✅ Menú interactivo (5 opciones)
- ✅ Verificaciones previas (Python, archivos)
- ✅ Creación automática de accesos directo
- ✅ Instalación en múltiples ubicaciones
- ✅ Manejo robusto de errores

---

## 🚀 Inicio Rápido

### Opción 1: Acceso Directo + Desktop (Recomendado)

```batch
# 1. Doble clic en build_exe.bat
# 2. Selecciona opción: [2] Compilar EXE con acceso directo en Desktop
# 3. Espera 30-60 segundos
# 4. ✅ Listo: Haz clic en "FishTrace" desde Desktop
```

**Resultado:**
- 📁 EXE compilado: `FishTrace.exe` en carpeta raíz
- 🖥️ Atajo en Desktop
- 📌 Atajo en Menú Inicio

---

## 🎯 Opciones Disponibles

### **[1] Compilar EXE en Carpeta Actual**
```
Para: Desarrollo local
Ubicación: C:\...\FishTrace\FishTrace.exe
Accesos: Ninguno (manual)
Tiempo: ~1 min
```

**Uso:**
- Cambios rápidos en código
- Testing antes de distribuir
- Desarrolladores

---

### **[2] Crear EXE con Acceso Directo en Desktop**
```
Para: Usuarios finales (local)
Ubicación: C:\...\FishTrace\FishTrace.exe
Accesos: Desktop + Menú Inicio
Tiempo: ~1 min
```

**Genera:**
- Ejecutable compilado ✓
- Acceso directo Desktop ✓
- Acceso directo Menú Inicio ✓

**Recomendado para:** Beta testing, usuarios locales

---

### **[3] Instalar en Program Files**
```
Para: Distribución profesional
Ubicación: C:\Program Files\FishTrace\FishTrace.exe
Accesos: Desktop + Menú Inicio
Requiere: Admin
Tiempo: ~1 min
```

**Nota:**
- Requiere **ejecutar como administrador**
- Instala "como programa profesional"
- Fácil desinstalación desde Control Panel

---

### **[4] Solo Instalar Dependencias Python**
```
Para: Solo preparar entorno
Instala: pip packages de requirements.txt
No compila: EXE
Tiempo: ~2-3 min (depende de conexión)
```

**Uso:**
- Preparar antes de cambios de código
- Verificar que dependencias instalan correctamente

---

### **[5] Limpiar y Compilar Desde Cero**
```
Para: "Fresh start" después de problemas
Elimina: build/, dist/, FishTrace.exe
Compila: Nuevo EXE limpio
Tiempo: ~1 min
```

**Usado cuando:**
- Cambios grandes en código
- Problemas con compilación anterior
- Actualización de dependencias

---

## 📥 Requisitos Previos

### ✅ Lo Que Necesitas

1. **Python 3.11+**
   ```bash
   # Descargar desde python.org
   # IMPORTANTE: Marcar "Add Python to PATH" en instalador
   
   # Verificar
   py --version
   ```

2. **Logo (Opcional)**
   - `logo.ico` en raíz del proyecto
   - Si no existe, EXE usa icono Windows default

3. **Archivo Requirements**
   - `requirements.txt` debe existir en raíz

4. **Archivo Principal**
   - `app.py` debe existir en raíz

---

## ⚠️ Solución de Problemas

### **Error: "Python 3.11 no encontrado"**

**Causa:** Python no está en PATH

**Solución:**
```bash
# 1. Instala Python desde python.org
# 2. Durante instalación, MARCA: "Add Python to PATH"
# 3. Reinicia CMD
# 4. Verifica: py --version
```

---

### **Error: "PyInstaller Error"**

**Causa:** requirements.txt no instaló correctamente

**Solución:**
```batch
# 1. Ejecuta: build_exe.bat
# 2. Selecciona: [4] Solo instalar dependencias
# 3. Espera a que termine
# 4. Intenta compilar de nuevo
# 5. Si sigue fallando: [5] Limpiar y compilar desde cero
```

---

### **Error: "No se pueden crear accesos directo"**

**Causa:** Problema con PowerShell

**Solución:**
```powershell
# 1. Abre PowerShell como admin
# 2. Ejecuta:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# 3. Intenta de nuevo
```

---

### **Error: "Permiso denegado" en Program Files**

**Causa:** Se necesitan permisos admin

**Solución:**
```batch
# 1. Clic derecho en build_exe.bat
# 2. "Ejecutar como administrador"
# 3. Selecciona: [3] Instalar en Program Files
```

---

## 📊 Benchmarks Compilación

| Acción | Tiempo Típico |
|--------|---------------|
| Opción 1 (Local EXE) | 1 min |
| Opción 2 (+ Desktop) | 1 min + 5 seg |
| Opción 3 (Program Files) | 1 min + Admin check |
| Opción 4 (Deps only) | 2-3 min (conexión) |
| Opción 5 (Clean build) | 1 min |

**Primera compilación:** +30 seg (PyInstaller setup)

---

## 🔍 Verificación Post-Compilación

### **Comprobar que EXE funciona:**

```batch
# Opción 1: Local
cd C:\...\FishTrace
.\FishTrace.exe

# Opción 2: Desktop
# Doble clic en "FishTrace" en Desktop

# Opción 3: Program Files
# Busca "FishTrace" en Menú Inicio
```

### **Ver logs si hay errores:**

```batch
# Si algo falla, revisar:
type Eventos\app.log

# Último error:
findstr /I "ERROR" Eventos\app.log
```

---

## 🛠️ Usos Comunes

### **Compilar para Testing**
```batch
[2] Compilar EXE con acceso directo en Desktop
→ Resultado: Acceso rápido en Desktop para probar
```

### **Compilar para Usuario Final (Local)**
```batch
[2] Compilar EXE con acceso directo en Desktop
→ Resultado: Listo para dar USB o install remoto
```

### **Compilar para Distribución Profesional**
```batch
[3] Instalar en Program Files (requiere admin)
→ Resultado: Programa instalado "como professional"
           Fácil desinstalación desde Control Panel
```

### **Resetear Todo y Recompilar**
```batch
[5] Limpiar y compilar desde cero
→ Resultado: EXE limpio, sin artifacts previos
```

---

## 📝 Archivos Generados

**Después de compilar, verás:**

```
FishTrace/
├── FishTrace.exe              ← EXE ejecutable
├── build_exe.bat              ← Este script
├── app.py
├── requirements.txt
└── [resto de archivos]
```

**En Desktop (si seleccionaste opción 2 o 3):**
```
Desktop/
└── FishTrace.lnk              ← Acceso directo
```

**En Menú Inicio:**
```
Menú Inicio → Todos los programas → FishTrace
```

**En Program Files (si seleccionaste opción 3):**
```
C:\Program Files\FishTrace\FishTrace.exe
```

---

## 🚀 Siguiente Fase: INNO SETUP

Cuando el proyecto esté más estable (v1.1+), considera migrar a **INNO SETUP** para:
- ✓ Instalador profesional `.exe` único
- ✓ Opciones de desinstalación
- ✓ Actualizaciones automáticas
- ✓ Mejor UX para usuarios finales

Documentación: Consultar `INSTALL.md` sección "Distribución Profesional"

---

## 📞 Soporte

**Problemas de compilación:**
1. Revisar `Eventos\app.log`
2. Ver sección "Solución de Problemas" arriba
3. Ejecutar opción [4] para reinstalar dependencias

**Problemas de ejecución del EXE:**
1. Revisar `Eventos/app.log`
2. Ver `INSTALL.md` para troubleshooting general
3. Verificar Python 3.11: `py --version`

---

**Última actualización:** 16 Mar 2026  
**Versión:** build_exe.bat v1.002  
**Status:** Production Ready ✅
