import tabula as tb
import pandas as pd
import os

def preprocess():
    dir = os.path.dirname(__file__)
    print(dir)

    df = tb.read_pdf("..\Raw Data\State_vaccinations.pdf", pages=1)[1]
    df.drop(df.index[:1], axis=0, inplace=True)
    df.drop(["S. No."], axis=1, inplace=True)
    df.columns = ["State/UT", "First Dose", "Second Dose", "Total Doses"]
    df.to_csv("..\Processed Data\Covid-19_Statewise_Vaccination_India.csv")
    print('Finished.')
    
preprocess()