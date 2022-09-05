# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 17:21:40 2022

@author: Linus
"""
import pandas as pd
fname = 'source.csv'

df = pd.read_csv(fname)

si = df.set_index('phone')
df_dict = si.T.to_dict('list')

g_name = []
city = []
phone = []
company =[]
     
for k,v in df_dict.items():
    for i in range(v[3]):
        g_name.append(v[0])
        city.append(v[1])
        phone.append(k)
        company.append(v[2])
    
output_dict = {'guest name':g_name,
                'city':city,
                'phone':phone,
                'company':company}

df_output = pd.DataFrame(output_dict)
print(df_output)
df_output.to_csv('dup_source.csv')

