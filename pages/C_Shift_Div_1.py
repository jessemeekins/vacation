import streamlit as st
from line_generator import *
import pandas as pd
import sqlite3
from vacation_functions import VacationFunctions as vf
from line_generator import LineGenerator as gen
SHIFT = 'C'
DIVISION = '1'
YEAR = 2023

file = upload_data()


with st.sidebar:
    
    current, previous = current_previous_bidders(file, SHIFT, DIVISION)
    st.warning(f'CURRENT BIDDER: {current.values.any()}')
    st.success(f'{previous.values.any()} PICKED: {st.session_state.last_pick}')

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
            names = get_people_on_line( SHIFT, DIVISION, line, days)
            for name in names:
                st.write(name[0])
            
            #st.write([name for name in names])
        except sqlite3.OperationalError:
            st.write('No Picks.')


user_generate_lines(YEAR, SHIFT, DIVISION)