import streamlit as st
from vacation_functions import *
import pandas as pd


def manager_generate_lines(YEAR, SHIFT, DIVISION):
    
    lines = get_all_lines_filtered(YEAR, SHIFT, DIVISION)

    current_index = 0
    for i in range (1,42):

        try:
            key = 'key'
            value = f'{YEAR}{SHIFT}{DIVISION}{i}three_days'
            line = next(filter(lambda d: d.get(key) == value, lines), None)
            line_number = line["LINE_NUMBER"]
            quantity = line["QUANTITIY"]
            number_of_days = line["NUMBER_OF_DAYS"]

            st.subheader(f"[Line {i}](#line-{i})")

            col1, col2, col3, col4, col5= st.columns([1,1,1,0.5,1])
            col1.subheader('3 Days ')
            col2.metric('Num of Picks Left', quantity)
            if quantity == 0:
                col3.warning('SOLD OUT!')
                col4.button('N/A', key=[f'{SHIFT}_{DIVISION}_line{i}_three.1'], disabled=True)
                col5.button('Remove', key=[f'{SHIFT}_{DIVISION}_line{i}_three.2'], on_click=update_vacation_line, args=[YEAR, SHIFT, DIVISION, i, number_of_days, quantity+1, current_index-1])
            else:
                col3.info('OPEN') # update_vacation_line(year, shift, division, line_number, number_of_days, name)
                col4.button('Bid', key=[f'{SHIFT}_{DIVISION}_line{i}_three.3'], on_click=update_vacation_line, args=[YEAR, SHIFT, DIVISION, i, number_of_days, quantity-1, current_index+1])
                col5.button('Remove', key=[f'{SHIFT}_{DIVISION}_line{i}_three.4'],on_click=update_vacation_line, args=[YEAR, SHIFT, DIVISION, i, number_of_days, quantity+1, current_index-1])
        except TypeError:
            pass

        try:
            key = 'key'
            value = f'{YEAR}{SHIFT}{DIVISION}{i}four_days'
            line = next(filter(lambda d: d.get(key) == value, lines), None)
            line_number = line["LINE_NUMBER"]
            quantity = line["QUANTITIY"]
            number_of_days = line["NUMBER_OF_DAYS"]

            col1, col2, col3, col4, col5= st.columns([1,1,1,0.5,1])
            col1.subheader('4 Days ')
            col2.metric('Num of Picks Left', quantity)
            if quantity == 0:
                col3.warning('SOLD OUT!')
                col4.button('N/A', key=[f'{SHIFT}_{DIVISION}_line{i}_four.1'], disabled=True)
                col5.button('Remove', key=[f'{SHIFT}_{DIVISION}_line{i}_four.2'], on_click=update_vacation_line, args=[YEAR, SHIFT, DIVISION, i, number_of_days, quantity+1, current_index-1])
            else:
                col3.info('OPEN') # update_vacation_line(year, shift, division, line_number, number_of_days, name)
                col4.button('Bid', key=[f'{SHIFT}_{DIVISION}_line{i}_four.3'], on_click=update_vacation_line, args=[YEAR, SHIFT, DIVISION, i, number_of_days, quantity-1, current_index+1])
                col5.button('Remove', key=[f'{SHIFT}_{DIVISION}_line{i}_four.4'],on_click=update_vacation_line, args=[YEAR, SHIFT, DIVISION, i, number_of_days, quantity+1, current_index-1])
        
        except TypeError:
            pass

        try:
            key = 'key'
            value = f'{YEAR}{SHIFT}{DIVISION}{i}five_days'
            line = next(filter(lambda d: d.get(key) == value, lines), None)
            line_number = line["LINE_NUMBER"]
            quantity = line["QUANTITIY"]
            number_of_days = line["NUMBER_OF_DAYS"]

            col1, col2, col3, col4, col5= st.columns([1,1,1,0.5,1])
            col1.subheader('5 Days ')
            col2.metric('Num of Picks Left', quantity)
            if quantity == 0:
                col3.warning('SOLD OUT!')
                col4.button('N/A', key=[f'{SHIFT}_{DIVISION}_line{i}_five.1'], disabled=True)
                col5.button('Remove', key=[f'{SHIFT}_{DIVISION}_line{i}_five.2'], on_click=update_vacation_line, args=[YEAR, SHIFT, DIVISION, i, number_of_days, quantity+1, current_index-1])
            else:
                col3.info('OPEN')
                col4.button('Bid', key=[f'{SHIFT}_{DIVISION}_line{i}_five.3'], on_click=update_vacation_line, args=[YEAR, SHIFT, DIVISION, i, number_of_days, quantity-1, current_index+1])
                col5.button('Remove', key=[f'{SHIFT}_{DIVISION}_line{i}_five.4'], on_click=update_vacation_line, args=[YEAR, SHIFT, DIVISION, i, number_of_days, quantity+1, current_index-1])

        except:
            pass
          
def user_generate_lines(YEAR, SHIFT, DIVISION):

    lines = get_all_lines_filtered(YEAR, SHIFT, DIVISION)

    for i in range(1,42):
        try:
            key = 'key'
            value = f'{YEAR}{SHIFT}{DIVISION}{i}three_days'
            line = next(filter(lambda d: d.get(key) == value, lines), None)
            line_number = line["LINE_NUMBER"]
            quantity = line["QUANTITIY"]
            number_of_days = line["NUMBER_OF_DAYS"]

            st.subheader(f"[Line {i}](#line-{i})")

            col1, col2, col3, col4, col5= st.columns([1,1,1,0.5,1])
            col1.subheader('3 Days')
            col2.metric('Num of Picks Left', quantity)
            if quantity == 0:
                col3.warning('SOLD OUT!')
            elif quantity == 1:
                col3.warning('ALMOST SOLD OUT!')    
            else:
                col3.info('OPEN')
        except TypeError:
            pass

        try:
            key = 'key'
            value = f'{YEAR}{SHIFT}{DIVISION}{i}four_days'
            line = next(filter(lambda d: d.get(key) == value, lines), None)
            line_number = line["LINE_NUMBER"]
            quantity = line["QUANTITIY"]
            number_of_days = line["NUMBER_OF_DAYS"]

            col1, col2, col3, col4, col5= st.columns([1,1,1,0.5,1])
            col1.subheader('4 Days')
            col2.metric('Num of Picks Left', quantity)
            if quantity == 0:
                col3.warning('SOLD OUT!')
            elif quantity == 1:
                col3.warning('ALMOST SOLD OUT!')    
            else:
                col3.info('OPEN')
        except TypeError:
            pass  

        try:
            key = 'key'
            value = f'{YEAR}{SHIFT}{DIVISION}{i}five_days'
            line = next(filter(lambda d: d.get(key) == value, lines), None)
            line_number = line["LINE_NUMBER"]
            quantity = line["QUANTITIY"]
            number_of_days = line["NUMBER_OF_DAYS"]

            col1, col2, col3, col4, col5= st.columns([1,1,1,0.5,1])
            col1.subheader('5 Days')
            col2.metric('Num of Picks Left', quantity)
            if quantity == 0:
                col3.warning('SOLD OUT!')
            elif quantity == 1:
                col3.warning('ALMOST SOLD OUT!')    
            else:
                col3.info('OPEN')
        except TypeError:
            pass    
            



