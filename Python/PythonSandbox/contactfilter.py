# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 20:04:55 2020

@author: eilon.eilstein
"""

import pptx
import pandas as pd

data = {"DataType" : ['ABS', 'PRC'],
             "col1" : [49321,1.0],
             "col2" : [42321,0.9],
             "col3" : [38321,0.75],
             "col4" : [19321,0.48],
             "col5" : [321,0.009]}

df = pd.DataFrame(data)

col_lst = list(df)
col_lst.remove('DataType')
print(df[col_lst].values.tolist())
