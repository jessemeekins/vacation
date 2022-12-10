import streamlit as st
from line_generator import *
st.header('Bidding begins 12/11/22 @08:30')


with st.sidebar:
    num =st.selectbox('Navigate to a Line', [i for i in range(1,42)])
    st.write('Click to navigate:', f'[Line {num}](#line-{num})')
user_generate_lines('2023','A','2')
