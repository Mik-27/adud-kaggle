@ECHO OFF

TITLE Fetching and Preprocessing Data

set url=%1

:: Moving to the desired directory
SET root=D:\Mihir\Data Science\Material\Dataset\Automate Data Fetch and Upload
cd /D %root%
ECHO Current Directory:
cd

ECHO ============================================================
:: Downloading two required PDF file from Government website.
ECHO Downloading file...
ECHO Url: %url%

cd Raw Data
wget -O state_vaccinations.pdf %url%
cd ..

ECHO "Executing Preprocessing Pipeline..."
cd ML_Pipeline

::env1\Scripts\activate.bat

python process_data2.py
::deactivate

ECHO ====================================================
ECHO "Covid-19_Statewise_Vaccination_India.csv created."
ECHO ====================================================

PAUSE