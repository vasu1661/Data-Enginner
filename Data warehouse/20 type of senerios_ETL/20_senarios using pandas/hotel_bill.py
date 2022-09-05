# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 14:49:45 2022

@author: Linus
"""

import pandas as pd
fname = 'items.csv'

df = pd.read_csv(fname)
si = df.set_index('item')
df_dict = si.T.to_dict('list')

item_lst = list(df_dict.keys())
value_lst = list(df_dict.values())

class Hotel_Bill():
    def __init__(self):
        self.item = ''
        self.price = 0
        self.quantity = 0
        self.phone_num = 0
        self.email = ''
        self.gst = .05
        self.discount = .035
        self.bill = 0
    
    def Input(self):
        for k,v in df_dict.items():
            print(k,':',v[0])
        self.phone_num = int(input('enter phone number : '))
        self.email = input('enter mail id : ')
        self.item = input('enetr item : ')
        self.quantity = float(input('enter quantity : '))
        
    def calc_bill(self):
        if self.item in item_lst:
            self.i_num = item_lst.index(self.item)
            self.bill = self.quantity * int(value_lst[self.i_num][0])
            self.gst_amt = self.bill * self.gst
            self.bill_before_discount = self.bill + self.gst_amt
        else:
            print('items is not in our menu')
                
    def discount(self):
        if self.item != 'Dosa' and self.bill_before_discount > 300:
            self.discount_amt = self.bill_before_discount * self.discount
            self.final_bill = self.bill_before_discount - self.discount_amt
        else:
            if self.item == 'Dosa':
                print('Dosa is not under discounted item')
                self.discount_amt = 0
                self.final_bill = self.bill_before_discount
            else:
                print('bill amount is less then 300 not elegible for the discount ')
                self.discount_amt = 0
                self.final_bill = self.bill_before_discount
                
    def display(self):
        Hotel_Bill.Input(self)
        Hotel_Bill.calc_bill(self)
        print()
        Hotel_Bill.discount(self)
        print('phone number    : ',self.phone_num)
        print('mail id         : ',self.email)
        print('item            : ',self.item)
        print('quantity        : ',self.quantity)
        print('bill before gst : ',self.bill)
        print('gst             : ',self.gst_amt)
        print('bill with gst   : ',self.bill_before_discount)
        print('discount        : ','{:.2f}'.format(self.discount_amt))
        print('final bill      : ',self.final_bill)
        
print('------------------main block starts------------------------')
obj = Hotel_Bill()
obj.display()
print('-------------------main block ends-------------------------')
            
                