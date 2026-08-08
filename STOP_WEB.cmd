@echo off
taskkill /F /IM web_server.exe >nul 2>nul
if errorlevel 1 (
  echo Web server is not running.
) else (
  echo Web server stopped.
)
timeout /t 2 >nul
