# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 11:41:44 2022

@author: Linus
"""

import pandas as pd
#from datetime import datetime, timedelta
import numpy as np

dir_path = 'F:\\iBridge360\\office\\contract\\'
fname = 'contract_table.csv'
df = pd.read_csv(fname)
set_index = df.set_index('Cpt_id')
data1 = set_index.T.to_dict('list')
amt = []
cont_id = []
exp_rec_id = []

for k,v in data1.items() :
    if k == 100:
        start_date = pd.to_datetime(v[2])
        end_date = pd.to_datetime(v[3])
        span = round((end_date - start_date)/np.timedelta64(1, 'M'))
        exp_emi = v[4]/span
        for i in range(span):
            amt.append(exp_emi)
            cont_id.append(v[0])
    elif k == 101:
        start_date = pd.to_datetime(v[2])
        end_date = pd.to_datetime(v[3])
        span = round((end_date - start_date)/np.timedelta64(1, 'Y') * 4)
        exp_emi = v[4]/span
        for i in range(span):
            amt.append(exp_emi)
            cont_id.append(v[0])
    elif k == 102:
        start_date = pd.to_datetime(v[2])
        end_date = pd.to_datetime(v[3])
        span = round((end_date - start_date)/np.timedelta64(1, 'Y') * 2)
        exp_emi = v[4]/span
        for i in range(span):
            amt.append(exp_emi)
            cont_id.append(v[0])
    elif k == 103:
        start_date = pd.to_datetime(v[2])
        end_date = pd.to_datetime(v[3])
        span = round((end_date - start_date)/np.timedelta64(1, 'Y'))
        exp_emi = v[4]/span
        for i in range(span):
            amt.append(exp_emi)
            cont_id.append(v[0])
        
    else :
        print('you are not belong here')
 
for i in range(1,(len(amt)+1)):
    exp_rec_id.append(i)
    
data_dict = {
             'Exp_rec_id':exp_rec_id,
             'contract_id':cont_id,
             'Amount':amt
             }

df_up = pd.DataFrame(data_dict)
df_up.to_csv('exp_rec_table.csv',index=False)

print(df_up)
