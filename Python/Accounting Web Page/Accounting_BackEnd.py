import streamlit as st
import pandas as pd

# pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.options.display.float_format = '{:,.2f}'.format

labs = ['AID','Ilex','Electra','MH']
bill_types = ['Sampler','Lab']

class Price:
    def __init__(self,lab,test_type,price):
        self.lab = lab
        self.test_type = test_type
        self.price = price

    def to_dict(self):
        return {(self.lab ,self.test_type):self.price}


lab_prices = {}
#AID
lab_prices.update(Price(lab = 'AID',test_type='singel_regular', price = 119.34).to_dict())
lab_prices.update(Price(lab = 'AID',test_type='son_no_bag', price = 15.21).to_dict())
lab_prices.update(Price(lab = 'AID',test_type='son_with_bag', price = 17.55).to_dict())
lab_prices.update(Price(lab = 'AID',test_type='Father_pooling', price = 119.34).to_dict())
#Ilex
lab_prices.update(Price(lab = 'Ilex',test_type='singel_regular', price = 119.34).to_dict())
lab_prices.update(Price(lab = 'Ilex',test_type='son_no_bag', price = 29.25).to_dict())
lab_prices.update(Price(lab = 'Ilex',test_type='son_with_bag', price = 17.55).to_dict())
lab_prices.update(Price(lab = 'Ilex',test_type='Father_pooling',price = 159.12).to_dict())
#Electra
lab_prices.update(Price(lab = 'Electra',test_type='singel_regular', price = 89.622).to_dict())
lab_prices.update(Price(lab = 'Electra',test_type='son_no_bag', price = 25.74).to_dict())
lab_prices.update(Price(lab = 'Electra',test_type='son_with_bag', price = 23.985).to_dict())
lab_prices.update(Price(lab = 'Electra',test_type='Father_pooling', price = 114.66).to_dict())
lab_prices.update(Price(lab = 'Electra',test_type='singel_pooling', price = 71.6976).to_dict())
#MH
lab_prices.update(Price(lab = 'MH',test_type='singel_regular', price = 116.5203).to_dict())
lab_prices.update(Price(lab = 'MH',test_type='son_no_bag', price = 28.08).to_dict())
lab_prices.update(Price(lab = 'MH',test_type='son_with_bag', price = 17.55).to_dict())
lab_prices.update(Price(lab = 'MH',test_type='Father_pooling', price = 116.5203).to_dict())

def get_lab_price(lab,test_type):
    if (lab,test_type) in lab_prices.keys():
        return lab_prices[(lab,test_type)]
    else:
        return -10000000
    



def get_Count_df(df):
    df = df.copy(deep=True)
    df = df.groupby('type').count().reset_index()[['type', 'barcode']].rename(columns={'barcode':'Count'})
    return df

def index_price_to_df(df, name):
    df = df.copy(deep=True)
    df['Price_Per_Unit'] = df.apply(lambda row: get_lab_price(name, row['type']), axis=1)
    df['Price_Per_Type'] = df.apply(lambda row: row['Price_Per_Unit'] * row['Count'], axis=1)
    return df


def main(df, type, name):
    df = df.copy(deep=True)
    df = get_Count_df(df)
    df = index_price_to_df(df, name)
    return df
