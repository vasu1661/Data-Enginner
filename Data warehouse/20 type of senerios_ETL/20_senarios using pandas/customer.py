# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 16:28:13 2022

@author: Linus
"""

import pandas as pd

fname = 'customer.csv'

df = pd.read_csv(fname)

cust_name_lst = []
cust_city_lst = []
cust_since_lst = []

dup_cust_name = []
dup_cust_city = []
dup_cust_since = []
dup_repeat =[]
dup_cust_phone = []

si = df.set_index('cust_phone')
df_dict = si.T.to_dict('list')

for k,v in df_dict.items():
    cust_name_lst.append(v[0])
    cust_city_lst.append(v[1])
    cust_since_lst.append(v[2])

target_cust_dict = {'cust_name':cust_name_lst,
                    'cust_phone':df_dict.keys(),
                    'cust_city':cust_city_lst,
                    'cust_since':cust_since_lst}

df_target = pd.DataFrame(target_cust_dict)

dup_df = df[df.duplicated()]
dup_si = dup_df.set_index('cust_phone')
dup_dict = dup_si.T.to_dict('list')

for k,v in dup_dict.items():
    count = 0
    for i in list(df['cust_phone']):
        if i == k:
            count+=1
    v.append(count)
    dup_dict.update({k:v})
    
for k,v in dup_dict.items():
    dup_cust_name.append(v[0])
    dup_cust_city.append(v[1])
    dup_cust_since.append(v[2])
    dup_repeat.append(v[3])
    dup_cust_phone.append(k)
    
dup_cust_dict = {'cust_name':dup_cust_name,
               'cust_phone':dup_cust_phone,
               'cust_city':dup_cust_city,
               'cust_since':dup_cust_since,
               'instances':dup_repeat}

df_dup = pd.DataFrame(dup_cust_dict)

print(df_target)
print(df_dup)

df_target.to_csv('target.csv')
df_dup.to_csv('duplicate_record.csv')