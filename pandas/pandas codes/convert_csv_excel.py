# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 11:03:06 2022

@author: vasudevreddy h
"""

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

d1 = pd.Series(data)

print(d1)

type(d1)

#############################
age_det = {
    'name':['navin','praven','kiran'],
    'age' :[23,30,35]
      
                     }
type(age_det)
data1 = pd.DataFrame(age_det)
print(data1)

data1

###########################################
#convert dataframe to csv
d1.to_csv('data.csv')
#read csv file
data = pd.read_csv('data.csv',index_col=0)
data
