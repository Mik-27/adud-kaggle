@ECHO OFF

TITLE Upload Data to Kaggle

cd Processed Data

kaggle datasets status mihir27/covid19-vaccinations-india

kaggle datasets version -m "Updated Dataset"

ECHO ===================================================

ECHO Dataset Updated Successfully 

ECHO ===================================================
