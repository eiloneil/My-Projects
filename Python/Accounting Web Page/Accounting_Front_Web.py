import streamlit as st
import pandas as pd
from Accounting_BackEnd import main

pd.options.display.float_format = '{:,.2f}'.format

## Set Entities lists from which to select
labs = ['AID','Ilex','Electra','MH']
samplers = ['FEMI', 'TEREM']
bill_types = ['Sampler','Lab']

entities = {'labs':labs
            ,'samplers':samplers}

ent_col1, ent_col2 = st.columns([1,1])
entTitle_col1, entTitle_col2 = st.columns([1,1])

## Create ST Dropdown Entities' menues 
EntityType = ent_col1.selectbox(
     'Select Entity\'s Type',
     entities.keys())

x = entTitle_col1.subheader('You selected: '+ EntityType)

EntityName = ent_col2.selectbox(
     'Select Entity\'s Name',
     entities[EntityType])
y = entTitle_col2.subheader('You selected: '+ EntityName)

uploadedFile = st.file_uploader('Upload Excel Here', type=['csv','xlsx'],accept_multiple_files=False,key="fileUploader")

if uploadedFile != None:
    try: 
        df = pd.read_csv(uploadedFile)
        
    except Exception as e:
        df = pd.read_excel(uploadedFile)
    
    df = main(df, EntityType, EntityName)
    df['Price_Per_Type'] = df['Price_Per_Type'].apply(lambda x: f'{x:,}')
    df['Count'] = df['Count'].apply(lambda x: f'{x:,}')
    
    st.write(df.head(5).astype(str))
    
    TotalCount, TotalPrice = sum(df['Count'].str.replace(',', '').astype(float)), sum(df['Price_Per_Type'].str.replace(',', '').astype(float))
    
    totals_col1, totals_col2 = st.columns([1,1])
    totals_col1.markdown('Total Count: '+ f'{TotalCount:,.0f}')
    totals_col2.markdown('Total Price: '+ f'{TotalPrice:,.2f}')