# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 12:38:14 2022

@author: Linus
"""
import pandas as pd
import numpy as np

f1 = 'contract_table.csv'
f2 = 'term.csv'
df = pd.read_csv(f1)
df_t = pd.read_csv(f2)
    
for i in df['Cpt_id']:
    if i == 100:
        df['start_date'] = pd.to_datetime(df['Cont_S_date'][df['Cpt_id']==100])
        df['end_date'] = pd.to_datetime(df['Cont_E_date'][df['Cpt_id']==100])
        df['instalments'] = round((df['end_date']-df['start_date'])/np.timedelta64(1, 'M'))
for i in df['Cpt_id']:
    if i == 101:
        df['start_date'] = pd.to_datetime(df['Cont_S_date'][df['Cpt_id']==101])
        df['end_date'] = pd.to_datetime(df['Cont_E_date'][df['Cpt_id']==101])
        df['instalments'] = round((df['end_date']-df['start_date'])/np.timedelta64(1, 'Y') * 4)
for i in df['Cpt_id']:
    if i == 102:
        df['start_date'] = pd.to_datetime(df['Cont_S_date'][df['Cpt_id']==102])
        df['end_date'] = pd.to_datetime(df['Cont_E_date'][df['Cpt_id']==102])
        df['instalments'] = round((df['end_date']-df['start_date'])/np.timedelta64(1, 'Y') * 2)
for i in df['Cpt_id']:
    if i == 103:
        df['start_date'] = pd.to_datetime(df['Cont_S_date'][df['Cpt_id']==103])
        df['end_date'] = pd.to_datetime(df['Cont_E_date'][df['Cpt_id']==103])
        df['instalments'] = round((df['end_date']-df['start_date'])/np.timedelta64(1, 'Y'))
        
print(df[['Cont_id','start_date','end_date','instalments']])