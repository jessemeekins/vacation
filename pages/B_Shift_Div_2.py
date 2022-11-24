
import streamlit as st
from vacation_functions import *
from line_generator import *
import pandas as pd

SHIFT = 'B'
DIVISION = '2'
YEAR = '2023'

file = upload_data()
if 'last_pick' not in st.session_state:
    st.session_state.last_pick = 'No picks'

with st.sidebar:
    
    current, previous, counter = current_previous_bidders(file, SHIFT, DIVISION)
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
                names = get_people_on_line(YEAR, SHIFT, DIVISION, line, days)
                names = names.items
                for name in names:
                    try:
                        st.write(name["NAME"])
                    except:
                        st.write('Not Listed')
            except:
                st.write('No Picks.')
                
st.header('Bidding begins 11/26/22 @08:30')
st.write('Get that queso ready, baby!')
user_generate_lines(YEAR, SHIFT, DIVISION)

   
