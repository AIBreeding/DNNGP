@echo off
cd /d %~dp0
call conda env create -f ./Scripts/environment-win.yaml
echo Done
pause