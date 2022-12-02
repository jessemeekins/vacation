#%%
import streamlit as st
import pandas as pd
import datetime as dt

file = '/Users/jessemeekins/Documents/VS Code/Vacation_streamlit/assets/2023 vacation picks spreadhseet.xlsx'

sheet_names = ['D1A 2023']
for n in sheet_names:
    df = pd.read_excel(file, sheet_name=n)

    three_day = 0
    four_day = 0
    five_day = 0

    seveteen = 0
    sixteen = 0 
    fifteen = 0 
    fourteen = 0
    thirteen = 0
    twelve = 0
    hire_date = df['VAC. DAYS'].dropna()


    for years in hire_date:

        #i = dt.datetime.strftime(i, '%Y/%m/%d')
        #s = i.split('/')
        #years = 2023 - int(s[0])   


        
        #return Three Day, Four Day, Five Day

        if years >= 17:
            # 4, 0, 1 # 17 days
            three_day += 4
            four_day += 0
            five_day += 1
            seveteen+=1
        elif years >= 16:
            # 4, 1, 0 # 16 days
            three_day += 4
            four_day += 1
            five_day += 0
            sixteen+=1
        elif years >= 15:
            # 5, 0, 0 # 15 days
            three_day += 5
            four_day += 0
            five_day += 0
            fifteen+=1
        elif years >= 14:
            # 3, 0 ,1 # 14 days
            three_day += 3
            four_day += 0
            five_day += 1
            fourteen+=1
        elif years >= 13:
            # 3, 1, 0 # 13 days
            thirteen+=1
            three_day += 3
            four_day += 1
            five_day += 0
        elif years >= 12:
            twelve+=1
            # 4, 0, 0 # 12 days
            three_day += 4
            four_day += 0
            five_day += 0
        else:
            three_day += 0
            four_day += 0
            five_day += 0

    print(n+':')
    print('3 days: ' , three_day)
    print('4 days: ' , four_day)
    print('5 days: ' , five_day)
    print('-'*30)
    print(twelve,'-',thirteen,'-' ,fourteen,'-', fifteen,'-', sixteen,'-', seveteen)


