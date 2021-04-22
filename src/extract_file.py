import sqlite3
import pandas as pd
from glob import glob
import json

def extract_csv_file(f):
    try:
        df = pd.read_csv(f)
        return df
    except:
        pass

def extract_excel_file(f):
    try:
        raw_df = pd.read_excel(f, sheet_name=None)
        sheets = list(raw_df.keys()) 
        df = pd.DataFrame()
        for sheet in sheets:
            df = df.append(raw_df[sheet], ignore_index = True) 
        return df
    except:
        pass

def extract_json_file(f):
    try:
        df = pd.read_json(f, lines=True)
        return df
    except:
        pass
    
def extract(f, columns):
    extracted_data = pd.DataFrame(columns = columns)
    for csvfile in glob(r"data/{}*.csv".format(f)):
        extracted_data = extracted_data.append(extract_csv_file(csvfile), ignore_index=True)
    for excelfile in glob(r"data/{}*.xls*".format(f)):
        extracted_data = extracted_data.append(extract_excel_file(excelfile)[columns], ignore_index=True)
    for jsonfile in glob(r"data/{}*.json".format(f)):
        extracted_data = extracted_data.append(extract_json_file(jsonfile), ignore_index=True)
    return extracted_data.drop_duplicates()
    
