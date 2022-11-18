
import streamlit as st
from vacation_functions import VacationFunctions as vf
from line_generator import LineGenerator as gen
import pandas as pd
import sqlite3

SHIFT = 'B'
DIVISION = '1'


file = pd.read_csv('assets/BshiftbiddersExport.csv')




with st.sidebar:

    current, previous = vf.current_previous_bidders(file, SHIFT, DIVISION)

    num =st.selectbox('Navigate to a Line', [i for i in range(1,42)])
    st.write('Click to navigate:', f'[Line {num}](#line-{num})')

    st.warning(f'CURRENT BIDDER: {current.values.any()}')
    st.success(f'{previous.values.any()} PICKED: ')

    st.write('Get Names on a Line:')
    col1, col2 = st.columns(2)
    line = col1.selectbox('Line', options=[i for i in range(1,42)])
    days = col2.selectbox('Days', options=['three', 'four', 'five'])
    click = st.button('Get Names')
    if click:
        try:
            names = vf.get_names(SHIFT, DIVISION, line, days)
            for name in names:
                st.write(name[0])
            
            #st.write([name for name in names])
        except sqlite3.OperationalError:
            st.write('No Picks.')
gen.user_generate_lines(SHIFT, DIVISION)
















