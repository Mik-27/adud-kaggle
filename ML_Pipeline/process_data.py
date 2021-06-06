import pandas as pd
import numpy as np

def merge_data():
    
    # Importing Data
    df_india = pd.read_csv(r"..\Raw Data\India.csv")
    df_world = pd.read_csv(r"..\Raw Data\vaccinations.csv")
    
    # Adding row for missing date viz. 2021-04-20
    missed_date = pd.DataFrame({'date':'2021-04-20', 'location':'India', 'vaccine':'Covaxin, Oxford/AstraZeneca'}, index=[93.5])
    df_india = df_india.append(missed_date, ignore_index=False)
    df_india = df_india.sort_index().reset_index(drop=True)
    
    # Drop data for date = '2021-02-14'
    df_world.drop(df_world[(df_world['location'] == 'India') & (df_world['date'] == '2021-02-14')].index[0], axis=0, inplace=True)
    
    # Get useful columns
    useful_df = df_world[df_world['location'] == 'India'].iloc[:,7:]
    useful_df = useful_df.reset_index()
    udf_cols = useful_df.columns.tolist()
    udf_cols.remove('index')
    
    # Merge/concat data from the two tables
    df = pd.concat([df_india, useful_df], axis=1, ignore_index=True)
    df.drop([7], axis=1, inplace=True)
    
    df_cols = df_india.columns.tolist()
    df_cols.extend(udf_cols)
    
    df.columns = df_cols
    
    #Preprocessing - Missing values
    df.date = pd.to_datetime(df['date'])
    df.loc[1,"people_fully_vaccinated_per_hundred"] = 0.0
    df["people_fully_vaccinated_per_hundred"] = df["people_fully_vaccinated_per_hundred"].fillna(method='bfill')
    df["change"] = df.daily_vaccinations.diff()
    df.rename({'change': 'daily_change_in_vaccinations'}, axis=1, inplace=True)
    df.fillna(0, inplace=True)
    cols = df.columns.to_list()
    
    # Final columns list
    cols = ['location',
     'date',
     'vaccine',
     'source_url',
     'total_vaccinations',
     'total_vaccinations_per_hundred',
     'people_vaccinated',
     'people_vaccinated_per_hundred',
     'people_fully_vaccinated',
     'people_fully_vaccinated_per_hundred',       
     'daily_vaccinations',
     'daily_change_in_vaccinations',
     'daily_vaccinations_per_million',
     ]
    df = df[cols]
    
    df.to_csv(r"D:\Mihir\Data Science\Material\Dataset\Processed Data\Covid-19_Daily_Vaccinations_India.csv")
    
merge_data()
