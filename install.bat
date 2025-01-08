@echo off
set TEMP_DIR=%TEMP%
set VERSION=v0.1.91
curl -L -o %TEMP_DIR%\install.whl https://github.com/notguoxin/custom-webui/releases/download/%VERSION%/open_webui-%VERSION%-py3-none-any.whl
schtasks /End /TN Autorun 
pip install %TEMP_DIR%\\install.whl 
del /s /f /q %TEMP_DIR%\\install.whl 
schtasks /Run /TN Autorun 
timeout /T 15 
exit