import streamlit as st


col1, buff, col2 = st.columns([1,0.5,3])

options = ['meekins', 'farr', 'lewis', 'staten']

next = st.button('Next Bidder')
if next:
    if 'current_index' not in st.session_state:
        st.session_state.current_index = 0


st.session_state.current_index


st.session_state.current_index


options[0]
