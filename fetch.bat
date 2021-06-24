@ECHO OFF

TITLE Fetching and Preprocessing Data

ECHO Fetching Data...
:: Moving to the desired directory
SET root=D:\Mihir\Data Science\Material\Dataset\Automate Data Fetch and Upload
cd /D %root%
ECHO Current Directory:
cd

:: Pinging the site to check connection and site status
ECHO =====================================================================
PING github.com || ECHO "Cannot connect to github.com!"
ECHO =====================================================================

:: Downloading two required CSV files from OWID GitHub repo.
ECHO Downloading files...

cd Raw Data

wget -O India.csv https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/country_data/India.csv
wget -O Vaccinations.csv https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv

cd ..

:: Preprocessing and merging the files using the python script
ECHO "Executing Preprocessing Pipeline..."
cd ML_Pipeline
python process_data.py
cd ..

ECHO ====================================================
ECHO "Covid-19_Daily_Vaccinations_India.csv created."
ECHO ====================================================

