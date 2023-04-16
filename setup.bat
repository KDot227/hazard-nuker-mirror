@echo off

cd /d %~dp0

python -m pip install -U -r requirements.txt
python -m pip uninstall -y cairocffi
python -m pipwin uninstall cairocffi
python -m pipwin install cairocffi
python -m pip install cairocffi

echo python -m Hazard > start.bat
start start.bat

pause
exit