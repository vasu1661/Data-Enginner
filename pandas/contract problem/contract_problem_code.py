import pandas as pd
table_1 = pd.read_csv('cont_term_table.csv')
table_2 = pd.read_csv('contract_table.csv')
output = pd.read_csv('')
print(table_1)
print(table_2)

df = pd.DataFrame(table_2)
s_date = df['cont_s_date'] = pd.to_datetime(df['cont_s_date']).dt.year
print(s_date)
print(df.set_index('cont_s_date',inplace=True))
e_date = df['cont_e_date'] = pd.to_datetime(df['cont_e_date']).months()
print(e_date)
exc_date = (s_date - e_date)
print(exc_date)
df1 = pd.merge(table_1,table_2,on='cpt_id',how ='inner')
#df2 = df1.set_index('cpt_id',inplace=True)
#df1.loc[100]
# df1.get('cpt_id')

# for i in df1.get('cpt_id'):
#    if i == 100:
#        date = s_date - e_date
         amount = total_amt / date
         
#    elif i == 101:
#        print ('quaterly')
#    else:
#        print('Yearly')
# excep_output = {'exc_id':'','exc_date':'','contract_id':'','amount':'amount'}

# excep_output



--------------------------------------

# Importing required libraries
import pandas as pd
from datetime import date
import numpy as np
 
# Making a dataframe which will have two
# columns two store different dates
# table_1 = pd.read_csv('cont_term_table.csv')
df = pd.read_csv('contract_table.csv').to_dict()
df
a = df['cont_s_date']
a
b = df['cont_e_date']
b

# pd.DataFrame({s_date: np.array([datetime.datetime(2010,1,10), datetime.datetime(2012,4,6)]),
#                    e_date: np.array(
#                      [datetime.datetime(2012,1,12),
#                       datetime.datetime(2013,5,22)])})
 
# # Used to convert the difference in terms of months
# df['nb_months'] = ((s_date - e_date)/np.timedelta64(1, 'M'))
# df['nb_months'] = df['nb_months'].astype(int)
# print(df)
# f_date = date(2014, 7, 2)
# l_date = date(2016, 7, 11)
# delta = l_date - f_date
# print(delta.days)
# df['year'] = (pd.DatetimeIndex(df['cont_s_date'])-pd.DatetimeIndex(df['cont_e_date']))
# df.head()
# df['month'] = pd.DatetimeIndex(df['cont_s_date']).month
# df.head()
df1['nb_months'] = ((df1['cont_e_date'] -df1['cont_s_date'])/np.timedelta64(1, 'M'))
df1['nb_months'] = df1['nb_months'].astype(int)

