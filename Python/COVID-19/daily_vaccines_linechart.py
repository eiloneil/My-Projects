import pandas as pd
from datetime import date
import os
import pyodbc
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
from openpyxl import load_workbook

### Connection Dictionary

dbs = {
    "bi": {
        "server": "mohprdsqlbi03",
        "database": "BI_Corona"
    },
    "xrm": {
        "server": "lsxrm365extrnl",
        "database": "Korona_MSCRM"
    },
    "df": {
        "server": "ls-sql16-df",
        "database": "DataFactoryMRR"
    },
    "df-test": {
        "server": "MOHPRDSQL02",
        "database": "DataFactoryMRR"
    }
}


### Define "Run_SQL" Function

def run_sql(sql_name, db_name): #insert SQL file name and DB --> Return DataFrame of Query Output

    db = dbs[db_name]
    SQL_SERVER = "{SQL Server}"
    server = db['server']
    database = db['database']
    
    #Set The Connection
    conn = pyodbc.connect('Driver='+SQL_SERVER+';'
                          'Server='+server+';'
                          'Database='+database+';'
                          'Trusted_Connection=yes;')

    #Set Query Text
    path = r"\\FSMTT\HomeFolders\eilon.eilstein\Desktop\Jupyter Notebooks\scripts\\" + sql_name + '.sql'
    fd = open(path, 'r')
    sql = fd.read()
    
    #Run Query and Return as DataFrame
    sql_query = pd.read_sql_query(sql, conn)
    df = pd.DataFrame(sql_query)
    
    return df

# Create DataFrame from SQL Query

sql_name = 'daily_vaccinations_BI'
df = run_sql(sql_name, 'bi')


# Export To Excel

raw_path = r'\\fs-dev\public dev\ApplicationInfrastructure\dev\bi_dev8200\Eilon\extract to excel\vaccines\\'
raw_excel_name = r'Daily_vaccination_data.xlsx'
xl_path = raw_path+raw_excel_name


# Change Date Format

df['Date'] = pd.to_datetime(df['Date'])


# Write Non-Derstructively to Existing Excel

with pd.ExcelWriter(xl_path, datetime_format='YYYY-MM-DD') as writer:
    df.to_excel(writer, sheet_name='גלם', index=False)

# Refresh PivotTable

import win32com.client

# create path
p_path = r'\\fs-dev\public dev\ApplicationInfrastructure\dev\bi_dev8200\Eilon\extract to excel\vaccines\\'
p_excel_name = r'v_pvt.xlsx'
full_p_path = p_path + p_excel_name


# Start an instance of Excel
xlapp = win32com.client.DispatchEx("Excel.Application")

# Open the workbook in said instance of Excel
wb = xlapp.workbooks.open(full_p_path)

# Optional, e.g. if you want to debug
# xlapp.Visible = True

# Refresh all data connections.
wb.RefreshAll()
wb.Save()

# Quit
xlapp.Quit()
