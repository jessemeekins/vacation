import streamlit as st
from line_generator import LineGenerator as lines

SHIFT = 'C'
DIVISION = '1'

with st.sidebar:
    num =st.selectbox('Navigate to a Line', [i for i in range(1,42)])
    st.write('Click to navigate:', f'[Line {num}](#line-{num})')


lines.user_generate_lines(SHIFT, DIVISION)