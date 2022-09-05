# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 10:36:43 2022

@author: Linus
"""

import pandas as pd

fguest = 'guest.csv'
fcust = 'customer.csv'

dfg = pd.read_csv(fguest)
dfc = pd.read_csv(fcust)

dfg_si = dfg.set_index('phone')
dfc_si = dfc.set_index('c_phone')

dfg_dict = dfg_si.T.to_dict('list')
dfc_dict = dfc_si.T.to_dict('list')

dfg_dict_key = list(dfg_dict.keys())

dict_call = {}
c_id = []
flg = []

for k in dfg_dict_key:
    if k in dfc_dict.keys():
        dfg_dict.pop(k)
    else:
        val = dfg_dict.get(k)
        dict_call.update({k:val})
        
for i in range(1,(len(dfg_dict)+1)):
    c_id.append(i)
for i in range(1,(len(dfg_dict)+1)):
    flg.append('Y')
    
dfg_call_up = {'c_id':c_id,
               'c_name':[v[0] for k,v in dict_call.items()],
               'city':[v[1] for k,v in dict_call.items()],
               'phone':list(dict_call.keys())}

dfc2 = {'name':[v[0] for k,v in dict_call.items()],
        'city':[v[1] for k,v in dict_call.items()],
        'phone':list(dict_call.keys()),
        'pro_flg':flg}

dfcall = pd.DataFrame(dfg_call_up)
dfg_flag = pd.DataFrame(dfc2)

print(dfcall)
print(dfg_flag)

dfcall.to_csv('call.csv')
dfg_flag.to_csv('guest_turned_cust.csv')