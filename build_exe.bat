@echo off
setlocal enabledelayedexpansion
title Compilador y Empaquetador FishTrace v1.002
color 0B

set "APP_NAME=FishTrace"
set "APP_VERSION=1.002"
set "PYTHON_VER=3.11"
set "CURRENT_DIR=%CD%"

REM ============================================================
REM                    BANNER Y MENU PRINCIPAL
REM ============================================================
cls
echo.
echo ╔════════════════════════════════════════════════════════╗
echo ║                                                        ║
echo ║        FishTrace v%APP_VERSION% - Compilador Profesional        ║
echo ║                                                        ║
echo ║    Sistema de Trazabilidad de Peces - Empaquetado    ║
echo ║                                                        ║
echo ╚════════════════════════════════════════════════════════╝
echo.

REM ============================================================
REM              VERIFICACIONES PREVIAS
REM ============================================================
echo [*] Realizando verificaciones previas...
echo.

REM Verificar Python 3.11
py -%PYTHON_VER% --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python %PYTHON_VER% no encontrado en PATH
    echo         Por favor, instala Python %PYTHON_VER% desde python.org
    echo         e incluye en PATH durante instalacion
    pause
    exit /b 1
)
echo [✓] Python %PYTHON_VER% detectado

REM Verificar logo.ico
if not exist "logo.ico" (
    echo [!] Advertencia: logo.ico no encontrado
    echo     El ejecutable usara icono por defecto
) else (
    echo [✓] logo.ico encontrado
)

REM Verificar requirements.txt
if not exist "requirements.txt" (
    echo [ERROR] requirements.txt no encontrado
    echo         Copia el archivo de dependencias a la raiz del proyecto
    pause
    exit /b 1
)
echo [✓] requirements.txt encontrado

REM Verificar app.py
if not exist "app.py" (
    echo [ERROR] app.py no encontrado
    echo         El archivo principal debe estar en la raiz del proyecto
    pause
    exit /b 1
)
echo [✓] app.py encontrado

echo.
echo ════════════════════════════════════════════════════════
echo.

REM ============================================================
REM          MENU DE OPCIONES INSTALACION
REM ============================================================
:MENU_PRINCIPAL
cls
echo.
echo        OPCIONES DE COMPILACION Y EMPAQUETADO
echo.
echo    [1] Compilar EXE en carpeta actual (recomendado desarrollo)
echo    [2] Crear EXE con acceso directo en Desktop
echo    [3] Instalar en Program Files (requiere admin)
echo    [4] Solo instalar dependencias Python (sin compilar)
echo    [5] Limpiar y compilar desde cero
echo    [0] Salir
echo.
set /p OPCION="Selecciona una opcion [0-5]: "

if "%OPCION%"=="0" exit /b 0
if "%OPCION%"=="1" goto COMPILE_LOCAL
if "%OPCION%"=="2" goto COMPILE_WITH_SHORTCUTS
if "%OPCION%"=="3" goto COMPILE_PROGRAM_FILES
if "%OPCION%"=="4" goto INSTALL_DEPS_ONLY
if "%OPCION%"=="5" goto CLEAN_BUILD

echo [ERROR] Opcion invalida
timeout /t 2
goto MENU_PRINCIPAL

REM ============================================================
REM                 OPCION 1: COMPILAR LOCAL
REM ============================================================
:COMPILE_LOCAL
cls
echo.
echo [*] Compilando EXE en carpeta actual...
echo.
call :INSTALL_DEPENDENCIES
if errorlevel 1 goto ERROR_EXIT
call :BUILD_EXE "%CURRENT_DIR%"
if errorlevel 1 goto ERROR_EXIT
call :SUCCESS_LOCAL
goto END_PROGRAM

REM ============================================================
REM        OPCION 2: COMPILAR CON ACCESOS DIRECTO
REM ============================================================
:COMPILE_WITH_SHORTCUTS
cls
echo.
echo [*] Compilando EXE y creando accesos directo...
echo.
call :INSTALL_DEPENDENCIES
if errorlevel 1 goto ERROR_EXIT
call :BUILD_EXE "%CURRENT_DIR%"
if errorlevel 1 goto ERROR_EXIT
call :CREATE_SHORTCUTS
if errorlevel 1 goto ERROR_EXIT
call :SUCCESS_WITH_SHORTCUTS
goto END_PROGRAM

REM ============================================================
REM     OPCION 3: INSTALAR EN PROGRAM FILES (ADMIN)
REM ============================================================
:COMPILE_PROGRAM_FILES
cls
echo.
echo [*] Verificando permisos de administrador...
echo.

net session >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Se requieren permisos de administrador
    echo         Ejecuta este script como administrador
    pause
    goto MENU_PRINCIPAL
)

set "INSTALL_PATH=C:\Program Files\FishTrace"
echo [*] Instalación en: %INSTALL_PATH%
echo.
call :INSTALL_DEPENDENCIES
if errorlevel 1 goto ERROR_EXIT
call :BUILD_EXE "%INSTALL_PATH%"
if errorlevel 1 goto ERROR_EXIT
call :CREATE_SHORTCUTS
if errorlevel 1 goto ERROR_EXIT
call :SUCCESS_PROGRAM_FILES
goto END_PROGRAM

REM ============================================================
REM         OPCION 4: SOLO INSTALAR DEPENDENCIAS
REM ============================================================
:INSTALL_DEPS_ONLY
cls
echo.
echo [*] Instalando solo dependencias Python...
echo.
call :INSTALL_DEPENDENCIES
if errorlevel 1 goto ERROR_EXIT
echo.
echo [✓] Dependencias instaladas correctamente
echo.
pause
goto MENU_PRINCIPAL

REM ============================================================
REM          OPCION 5: LIMPIAR Y COMPILAR DESDE CERO
REM ============================================================
:CLEAN_BUILD
cls
echo.
echo [!] Procederá a eliminar archivos compilados previos
echo.
set /p CONFIRM="¿Continuar? (s/n): "
if /i not "%CONFIRM%"=="s" goto MENU_PRINCIPAL

echo [*] Limpiando directorios...
if exist "build" (
    echo    Eliminando: build\
    rd /s /q "build" >nul 2>&1
)
if exist "dist" (
    echo    Eliminando: dist\
    rd /s /q "dist" >nul 2>&1
)
if exist "%APP_NAME%.exe" (
    echo    Eliminando: %APP_NAME%.exe
    del /f /q "%APP_NAME%.exe" >nul 2>&1
)

echo.
echo [*] Compilando desde cero...
echo.
call :INSTALL_DEPENDENCIES
if errorlevel 1 goto ERROR_EXIT
call :BUILD_EXE "%CURRENT_DIR%"
if errorlevel 1 goto ERROR_EXIT
call :SUCCESS_LOCAL
goto END_PROGRAM

REM ============================================================
REM               FUNCIONES AUXILIARES
REM ============================================================

:INSTALL_DEPENDENCIES
echo [1/3] Actualizando pip...
py -%PYTHON_VER% -m pip install --upgrade pip setuptools wheel >nul 2>&1
if errorlevel 1 (
    echo [ERROR] No se pudo actualizar pip
    exit /b 1
)

echo [2/3] Instalando PyInstaller y dependencias build...
py -%PYTHON_VER% -m pip install pyinstaller pyqtdarktheme==2.1.0 darkdetect >nul 2>&1
if errorlevel 1 (
    echo [ERROR] No se pudo instalar paquetes build
    exit /b 1
)

echo [3/3] Instalando dependencias del proyecto...
py -%PYTHON_VER% -m pip install -r requirements.txt >nul 2>&1
if errorlevel 1 (
    echo [ERROR] No se pudo instalar requirements.txt
    exit /b 1
)

echo.
echo [✓] Todas las dependencias instaladas
exit /b 0

:BUILD_EXE
setlocal
set "OUTPUT_PATH=%~1"

echo [*] Limpiando compilaciones previas...
if exist "build" rd /s /q "build" >nul 2>&1
if exist "dist" rd /s /q "dist" >nul 2>&1

echo [*] Compilando ejecutable...
echo    (Primera compilación puede tomar 30-60 segundos)
echo.

set "ICON_FLAG="
if exist "logo.ico" set "ICON_FLAG=--icon logo.ico"

py -%PYTHON_VER% -m PyInstaller --noconfirm --onefile --windowed ^
 --name "%APP_NAME%" ^
 %ICON_FLAG% ^
 --exclude-module PyQt6 ^
 --add-data "Config:Config" ^
 --add-data "Modulos:Modulos" ^
 --add-data "BasedeDatos:BasedeDatos" ^
 --add-data "Herramientas:Herramientas" ^
 --add-data "Resultados:Resultados" ^
 app.py >nul 2>&1

if not exist "dist\%APP_NAME%.exe" (
    echo [ERROR] PyInstaller no pudo generar el EXE
    endlocal
    exit /b 1
)

echo [*] Moviendo ejecutable a: %OUTPUT_PATH%\%APP_NAME%.exe
move /y "dist\%APP_NAME%.exe" "%OUTPUT_PATH%\%APP_NAME%.exe" >nul 2>&1

echo [*] Limpiando directorios temporales...
if exist "build" rd /s /q "build" >nul 2>&1
if exist "dist" rd /s /q "dist" >nul 2>&1

echo [✓] Ejecutable compilado: %OUTPUT_PATH%\%APP_NAME%.exe

endlocal
exit /b 0

:CREATE_SHORTCUTS
setlocal
set "EXE_PATH=%~1"

echo [*] Creando accesos directo en Desktop...

REM Crear acceso directo en Desktop
set "DESKTOP=%USERPROFILE%\Desktop"
powershell -NoProfile -Command ^
 "$WshShell = New-Object -ComObject WScript.Shell; " ^
 "$Link = $WshShell.CreateShortcut('%DESKTOP%\FishTrace.lnk'); " ^
 "$Link.TargetPath = '%EXE_PATH%\%APP_NAME%.exe'; " ^
 "$Link.WorkingDirectory = '%CURRENT_DIR%'; " ^
 "$Link.IconLocation = '%CURRENT_DIR%\logo.ico'; " ^
 "$Link.Save()" >nul 2>&1

if errorlevel 1 (
    echo [!] No se pudo crear acceso en Desktop (ignorado)
) else (
    echo [✓] Acceso directo creado en Desktop
)

echo [*] Creando acceso directo en Menú Inicio...

REM Crear acceso directo en Menú Inicio
set "START_MENU=%APPDATA%\Microsoft\Windows\Start Menu\Programs"
powershell -NoProfile -Command ^
 "$WshShell = New-Object -ComObject WScript.Shell; " ^
 "$Link = $WshShell.CreateShortcut('%START_MENU%\FishTrace.lnk'); " ^
 "$Link.TargetPath = '%EXE_PATH%\%APP_NAME%.exe'; " ^
 "$Link.WorkingDirectory = '%CURRENT_DIR%'; " ^
 "$Link.IconLocation = '%CURRENT_DIR%\logo.ico'; " ^
 "$Link.Save()" >nul 2>&1

if errorlevel 1 (
    echo [!] No se pudo crear acceso en Menú Inicio (ignorado)
) else (
    echo [✓] Acceso directo creado en Menú Inicio
)

endlocal
exit /b 0

:SUCCESS_LOCAL
echo.
echo ════════════════════════════════════════════════════════
echo.
echo [✓] ¡COMPILACION EXITOSA!
echo.
echo    Ejecutable: %CURRENT_DIR%\%APP_NAME%.exe
echo.
echo    Pasos siguientes:
echo    1. Ejecutar: %APP_NAME%.exe
echo    2. Calibrar cámaras en primer uso
echo    3. Ver logs en: Eventos\app.log
echo.
echo    Documentacion:
echo    - Instalacion: INSTALL.md
echo    - CUDA GPU:    CUDA_SETUP.md
echo.
pause
exit /b 0

:SUCCESS_WITH_SHORTCUTS
echo.
echo ════════════════════════════════════════════════════════
echo.
echo [✓] ¡COMPILACION Y ACCESOS DIRECTO EXITOSOS!
echo.
echo    Ejecutable: %CURRENT_DIR%\%APP_NAME%.exe
echo.
echo    Accesos directos creados:
echo    - [✓] Escritorio
echo    - [✓] Menú Inicio
echo.
echo    Haz doble clic en FishTrace desde Desktop
echo.
pause
exit /b 0

:SUCCESS_PROGRAM_FILES
echo.
echo ════════════════════════════════════════════════════════
echo.
echo [✓] ¡INSTALACION EN PROGRAM FILES EXITOSA!
echo.
echo    Instalado en: C:\Program Files\FishTrace\%APP_NAME%.exe
echo.
echo    Accesos directos creados:
echo    - [✓] Escritorio
echo    - [✓] Menú Inicio
echo.
pause
exit /b 0

:ERROR_EXIT
echo.
echo ════════════════════════════════════════════════════════
echo [ERROR] La compilación falló
echo.
echo Posibles causas:
echo - Python %PYTHON_VER% no está instalado
echo - requirements.txt no se pudo instalar
echo - PyInstaller Error
echo.
echo Ver Eventos\app.log para más detalles
echo.
pause
exit /b 1

:END_PROGRAM
echo.
echo Presiona cualquier tecla para volver al menú principal...
pause >nul
goto MENU_PRINCIPAL