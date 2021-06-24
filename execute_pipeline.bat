@ECHO OFF

TITLE Executing Pipeline

CALL fetch.bat

python get_state_data.py

CALL upload_data.bat

EXIT