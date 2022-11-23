
import streamlit as st
from vacation_functions import VacationFunctions as vf
from line_generator import LineGenerator as gen
import pandas as pd

SHIFT = 'B'
DIVISION = '2'
YEAR = '2023'

file = pd.read_csv('assets/BshiftbiddersExport.csv')
if 'last_pick' not in st.session_state:
    st.session_state.last_pick = 'No picks'


def B_Shift_Div2():
    with st.sidebar:
        
        current, previous = vf.current_previous_bidders(file, SHIFT, DIVISION)
        st.warning(f'CURRENT BIDDER: {current.values.any()}')
        st.success(f'{previous.values.any()} PICKED: {st.session_state.last_pick}')
        counter = vf.get_vacation_line_counter(SHIFT,DIVISION)

        st.subheader('Navigation')
        num =st.selectbox('Navigate to a Line', [i for i in range(1,42)])
        st.write('Click to navigate:', f'[Line {num}](#line-{num})')


        st.subheader('Get Names on a Line:')
        col1, col2 = st.columns(2)
        line = col1.selectbox('Line', options=[i for i in range(1,42)])
        days = col2.selectbox('Days', options=['three', 'four', 'five'])
        click = st.button('Get Names')
        if click:
                try:
                    names = vf.get_people_on_line(YEAR, SHIFT, DIVISION, line, days)
                    names = names.items
                    for name in names:
                        try:
                            st.write(name["NAME"])
                        except:
                            st.write('Not Listed')
                except:
                    st.write('No Picks.')


    lines = vf.get_lines()

    for i in range(1,42):
        try:
            
            
            with st.container():        

                key = 'key'
                value = f'2023B2{i}three'
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
                elif quantity == 1:
                    col3.warning('ALMOST SOLD OUT!')    
                else:
                    col3.info('OPEN')
        except TypeError:
            pass

    


        try:
            key = 'key'
            value = f'2023B2{i}four'
            line = next(filter(lambda d: d.get(key) == value, lines), None)
            line_number = line["LINE_NUMBER"]
            quantity = line["QUANTITIY"]
            number_of_days = line["NUMBER_OF_DAYS"]

            col1, col2, col3, col4, col5= st.columns([1,1,1,0.5,1])
            col1.subheader('4 Days ')
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
            value = f'2023B2{i}five'
            line = next(filter(lambda d: d.get(key) == value, lines), None)
            line_number = line["LINE_NUMBER"]
            quantity = line["QUANTITIY"]
            number_of_days = line["NUMBER_OF_DAYS"]

            col1, col2, col3, col4, col5= st.columns([1,1,1,0.5,1])
            col1.subheader('5 Days ')
            col2.metric('Num of Picks Left', quantity)
            if quantity == 0:
                col3.warning('SOLD OUT!')
            elif quantity == 1:
                col3.warning('ALMOST SOLD OUT!')    
            else:
                col3.info('OPEN')
        except TypeError:
            pass    
                    
if __name__ == "__main__":
    B_Shift_Div2()      
        













