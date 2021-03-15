# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 12:11:39 2021

@author: ramza
"""
import csv
#Read Data from CSV file
with open("C:\Users\ramza\Desktop\PyBank\PyBank_budget_data.csv", "r") as csvfile:
     csv_reader = csv.reader(csvfile, delimiter=",")
for row in csv_reader:
 print(row)

import pandas as pd
data=pd.read_csv('C:\Users\ramza\Desktop\PyBank\PyBank_budget_data.csv')
print(data)
