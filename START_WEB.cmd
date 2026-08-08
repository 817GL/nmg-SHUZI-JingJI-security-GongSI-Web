@echo off
setlocal
cd /d "%~dp0"
echo Starting Password Pool Web v2.0.2 Standalone...
if not exist "server\web_server.exe" (
  echo [FAILED] server\web_server.exe is missing.
  echo Please extract the whole ZIP again.
  pause
  exit /b 1
)
"server\web_server.exe"
endlocal
