@echo off

cd /d %~dp0

pip install -U -r requirements.txt
pip uninstall -y cairocffi
pipwin uninstall cairocffi
pipwin install cairocffi
pip install cairocffi

echo @echo off > start.bat
echo python -m Hazard >> start.bat
echo pause >> start.bat
echo exit >> start.bat
start start.bat

pause
exit