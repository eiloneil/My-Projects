import pandas as pd
from datetime import date
import os
import pyodbc
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt




weeks = 20

## Creating the Database

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=mohprdsqlbi03;'
                      'Database=bi_corona;'
                      'Trusted_Connection=yes;')

sql_text = """
SET NOCOUNT ON;

select i.fullname
	,i.age
	,i.first_positive_result_test_date
	,i.ind_positive_and_heal_coronavirus
	,i.new_statuscasevalidationname
	,i.address
	,i.neighborhood_name
	,i.ind_active_heal
	,i.ind_active_sick
	,i.ind_death
from dwh.vw_Fact_Corona_Panel_Investigation_Model i
where i.first_positive_result_test_date >= CAST(getdate() - 7*%s as date)
--and ind_death = 1
    and ind_positive_and_heal_coronavirus = 1
""" % (weeks)
sql_query = pd.read_sql_query(sql_text, conn)

today = date.today()
current_date = str(today.strftime("%d-%m-%Y"))

## Creating Pandas DataFrame

df = pd.DataFrame(sql_query)
df['status'] = np.where(df['ind_active_heal'] == 1,'החלים',np.where((df['ind_death']) == 1,'נפטר','חולה פעיל'))
df.ind_death.sort_values(ascending=False)


## Count Patients Grouped by Week

agg_df = df.groupby(['status', pd.Grouper(key='first_positive_result_test_date', freq='W-SUN')])['ind_positive_and_heal_coronavirus'].sum().reset_index().sort_values('first_positive_result_test_date')
agg_df['first_positive_result_test_date'] = pd.to_datetime(agg_df['first_positive_result_test_date'].sort_values().dt.strftime('%Y-%m-%d'))
agg_df = agg_df.rename(index=str, columns={"ind_positive_and_heal_coronavirus": "CNT_patients"})

## Extract to Excel

path = r'\\fs-dev\public dev\ApplicationInfrastructure\dev\bi_dev8200\Eilon\extract to excel\weekly_infected_status.xlsx'
if os.path.exists(path):
    os.remove(path)
agg_df.to_excel(path, index=False, sheet_name='סטטוס נדבקים שבועי') 


