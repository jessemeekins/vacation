import streamlit as st
from vacation_functions import VacationFunctions as vf
import pandas as pd

file = pd.read_csv('assets/BshiftbiddersExport.csv')

class LineGenerator:

    def manager_generate_lines(SHIFT, DIVISION):

        current, previous = vf.current_previous_bidders(file, SHIFT, DIVISION)

        
        for i in range (1,42):

            try:
                
                st.subheader(f"[Line {i}](#line-{i})")

                col1, col2, col3, col4, col5= st.columns([1,1,1,0.5,1])
                num = vf.new_bd_get_num(SHIFT, DIVISION, i, 'three')
                line = f'line{i}'
                num_of_days = 'three'
                col1.subheader('3 days')
                col2.metric('Num of Picks Left', num)
                if num == 0:
                    col3.warning('SOLD OUT!')
                    col4.button('N/A', key=[f'{SHIFT}_{DIVISION}_line{i}_three.1'], disabled=True)
                    col5.button('Remove', key=[f'{SHIFT}_{DIVISION}_line{i}_three.2'], on_click=vf.new_db_remove_bid, args=[num, SHIFT, DIVISION, i, num_of_days,])
                else:
                    col3.info('OPEN')
                    col4.button('Bid', key=[f'{SHIFT}_{DIVISION}_line{i}_three.3'], on_click=vf.new_db_add_bid, args=[num, SHIFT, DIVISION, i, num_of_days, current.values.any()])
                    col5.button('Remove', key=[f'{SHIFT}_{DIVISION}_line{i}_three.4'],on_click=vf.new_db_remove_bid, args=[num, SHIFT, DIVISION, i, num_of_days,])
            except:
                pass
            

            try:

                col1, col2, col3, col4, col5= st.columns([1,1,1,0.5,1])
                num = vf.new_bd_get_num(SHIFT, DIVISION, i, 'four')
                line = f'line{i}'
                num_of_days = 'four'
                col1.subheader('4 days')
                col2.metric('Num of Picks Left', num)
                if num == 0:
                    col3.warning('SOLD OUT!')
                    col4.button('N/A', key=[f'{SHIFT}_{DIVISION}_line{i}_four.1'], disabled=True)
                    col5.button('Remove', key=[f'{SHIFT}_{DIVISION}_line{i}_four.2'], on_click=vf.new_db_remove_bid, args=[num, SHIFT, DIVISION, i, num_of_days,])
                else:
                    col3.info('OPEN')
                    col4.button('Bid', key=[f'{SHIFT}_{DIVISION}_line{i}_four.3'], on_click=vf.new_db_add_bid, args=[num, SHIFT, DIVISION, i, num_of_days, current.values.any()])
                    col5.button('Remove', key=[f'{SHIFT}_{DIVISION}_line{i}_four.4'],on_click=vf.new_db_remove_bid, args=[num, SHIFT, DIVISION, i, num_of_days,])
            except:
                pass

            
            try:
                col1, col2, col3, col4, col5= st.columns([1,1,1,0.5,1])
                num = vf.new_bd_get_num(SHIFT, DIVISION, i, 'five')
                line = f'line{i}'
                num_of_days = 'five'
                col1.subheader('5 days')
                col2.metric('Num of Picks Left', num)
                if num == 0:
                    col3.warning('SOLD OUT!')
                    col4.button('N/A', key=[f'{SHIFT}_{DIVISION}_line{i}_five.1'], disabled=True)
                    col5.button('Remove', key=[f'{SHIFT}_{DIVISION}_line{i}_five.2'], on_click=vf.new_db_remove_bid, args=[num, SHIFT, DIVISION, i, num_of_days,])
                else:
                    col3.info('OPEN')
                    col4.button('Bid', key=[f'{SHIFT}_{DIVISION}_line{i}_five.3'], on_click=vf.new_db_add_bid, args=[num, SHIFT, DIVISION, i, num_of_days, current.values.any()])
                    col5.button('Remove', key=[f'{SHIFT}_{DIVISION}_line{i}_five.4'], on_click=vf.new_db_remove_bid, args=[num, SHIFT, DIVISION, i, num_of_days,])

            except:
                pass
    
           
    def user_generate_lines(SHIFT, DIVISION):
        
        for i in range (1,42):

            try:
                
                st.subheader(f"[Line {i}](#line-{i})")

                col1, col2, col3, col4, col5= st.columns([1,1,1,0.5,1])
                num = vf.new_bd_get_num(SHIFT, DIVISION, i, 'three')
                col1.subheader('3 days')
                col2.metric('Num of Picks Left', num)
                if num == 0:
                    col3.warning('SOLD OUT!')
                elif num == 1:
                    col3.warning('ALMOST SOLD OUT!')    
                else:
                    col3.info('OPEN')
                    
            except:
                pass
            
            try:

                col1, col2, col3, col4, col5= st.columns([1,1,1,0.5,1])
                num = vf.new_bd_get_num(SHIFT, DIVISION, i, 'four')
                col1.subheader('4 days')
                col2.metric('Num of Picks Left', num)
                if num == 0:
                    col3.warning('SOLD OUT!')
                elif num == 1:
                    col3.warning('ALMOST SOLD OUT!')     
                else:
                    col3.info('OPEN')
            except:
                pass

            try:
                col1, col2, col3, col4, col5= st.columns([1,1,1,0.5,1])
                num = vf.new_bd_get_num(SHIFT, DIVISION, i, 'five')
                col1.subheader('5 days')
                col2.metric('Num of Picks Left', num)
                if num == 0:
                    col3.warning('SOLD OUT!')
                elif num == 1:
                    col3.warning('ALMOST SOLD OUT!')
                else:
                    col3.info('OPEN')

            except:
                pass