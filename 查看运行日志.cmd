@echo off
setlocal
cd /d "%~dp0"
if not exist "data\logs" mkdir "data\logs"
start "" "data\logs"
endlocal
