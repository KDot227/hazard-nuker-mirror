@echo off

python -m pip install -U -r requirements.txt
python -m pip uninstall -y cairocffi
python -m pipwin uninstall cairocffi
python -m pipwin install cairocffi
python -m pip install cairocffi
python -m Hazard

pause
exit