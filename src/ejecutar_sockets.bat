@echo off
REM Abrir el servidor en una nueva ventana
start cmd /k "python servidor.py"

REM Esperar 2 segundos para que el servidor arranque
timeout /t 2

REM Abrir el cliente en otra ventana
start cmd /k "python cliente.py"

pause