
import streamlit as st
from vacation_functions import VacationFunctions as vf
from line_generator import LineGenerator as gen

SHIFT = 'B'
DIVISION = '1'


with st.sidebar:
    num =st.selectbox('Navigate to a Line', [i for i in range(1,42)])
    st.write('Click to navigate:', f'[Line {num}](#line-{num})')

gen.user_generate_lines(SHIFT, DIVISION)
















