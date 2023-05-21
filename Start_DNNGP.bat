@echo off
setlocal enabledelayedexpansion
for /f "delims=" %%i in ('where conda') do set VAR=%%i 
set "search=miniconda3\"

call set "part1=%%VAR:*%search%=%%"

set "VAR=!VAR:%part1%=!"
set "VAR=%VAR%Scripts\activate.bat"

for /f "tokens=2 delims= " %%i in ('conda info --envs ^| findstr /R "DNNGP3"') do set dnngp_env=%%i

call %VAR% %dnngp_env%
cd /d %~dp0
start ./Scripts/DNNGP-win.exe