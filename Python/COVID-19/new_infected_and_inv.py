import pandas as pd
from datetime import date
import os
import pyodbc
import numpy as np 

weeks = 5 #int(input())


conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=mohprdsqlbi03;'
                      'Database=bi_corona;'
                      'Trusted_Connection=yes;')

sql_text = """
SET NOCOUNT ON;



select i.inv_end_date
	,i.CNT_complete_inv
	,s.CNT_sick
from (
	select  cast(i.invest_end_date as date) inv_end_date
			,count(distinct i.investigation_ID) as CNT_complete_inv
	from dwh.vw_Fact_Corona_Panel_Investigation_Model i
	where cast(i.invest_end_date as date) >= getdate() - (7*%s) and cast(i.invest_end_date as date) < cast(getdate() as date)
		and i.ind_positive_and_heal_coronavirus = 1
        
	group by cast(i.invest_end_date as date)
	) i
left join (
		select cast(i.first_positive_result_test_date as date) sick_date
				,count(distinct i.investigation_ID) as CNT_sick
		from dwh.vw_Fact_Corona_Panel_Investigation_Model i
		where i.first_positive_result_test_date >= getdate() - (7*%s) and cast(i.first_positive_result_test_date as date) < cast(getdate() as date)
			and i.ind_positive_and_heal_coronavirus = 1
			group by cast(i.first_positive_result_test_date as date) 

			) s on s.sick_date = i.inv_end_date
order by 1 asc


""" % (weeks, weeks)
sql_query = pd.read_sql_query(sql_text, conn)

today = date.today()
current_date = str(today.strftime("%d-%m-%Y"))


df = pd.DataFrame(sql_query)
df['BL_Daily'] = df['CNT_sick']-df['CNT_complete_inv']
df['BL'] = df.BL_Daily.cumsum()
df

path = r'\\fs-dev\public dev\ApplicationInfrastructure\dev\bi_dev8200\Eilon\extract to excel\daily_new_sick_and_invs.xlsx'
if os.path.exists(path):
    os.remove(path)
df.to_excel(path, index=False, sheet_name='סטטוס נדבקים שבועי') 

#import matplotlib.pyplot as plt
#%matplotlib notebook
#plt.plot(df['inv_end_date'], df['CNT_sick'], marker='o',color='r')
#plt.plot(df['inv_end_date'], df['CNT_complete_inv'], marker='o',color='c')
## plt.plot(df['inv_end_date'], df['BL'],color='b')
## plt.figure(num=None, figsize=(20, 60), dpi=80, facecolor='w', edgecolor='k')
#plt.xticks(rotation=90)
#plt.grid(linewidth=0.2)
#plt.legend(['New Infected','Complete Investigations','BL'])
#plt.show()