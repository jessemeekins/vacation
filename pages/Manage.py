import streamlit as st
from vacation_functions import VacationFunctions as vf
from line_generator import LineGenerator as gen
import sqlite3
import streamlit as st


conn = sqlite3.connect('vaca.db')
c = conn.cursor()

def check_password():

    def password_entered():
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Password incorrect")
        return False
    else:
        return True

if check_password():
    
    A_SHIFT = 'A'
    B_SHIFT = 'B'
    C_SHIFT = 'C'
    DIVISION_1 = '1'
    DIVISION_2 = '2'


    tab1, tab2, tab3, tab4, tab5, tab6, tab7 =  st.tabs(['Edit Lines', 'A Shift Div 1', 'A Shift Div 2', 'B Shift Div 1', 'B Shift Div 2', 'C Shift Div 1', 'C Shift Div 2'])

    with tab1:
     
        with st.form('Edit Personal Pick', clear_on_submit=False):
            edit_person = st.selectbox('Name', options=['Meekins Jesse'])
            edit_shift = st.selectbox('Shift', options=['A','B','C'])
            edit_division = st.selectbox('Division', options=['1', '2'])
            edit_lines = st.selectbox('Select Line', options=[f'Line{i}' for i in range(1,42)])
            edit_days = st.selectbox('Days', options=['three', 'four', 'five'])


            form_line = f'{edit_shift}_{edit_division}_{edit_lines}_{edit_days}'

            col1, col2, col3 = st.columns(3)

            add = col1.form_submit_button('Add')
            if add:
                vf.add_person_too_line(form_line, edit_person)

            remove = col3.form_submit_button('Remove')
            if remove:
                vf.remove_person_from_line(form_line, edit_person)


        with st.form('Add Vacation Line'):
            add_shift = st.selectbox('Shift', options=['A','B','C'])
            add_division = st.selectbox('Division', options=['1', '2'])
            add_line = st.selectbox('Select Line', options=[i for i in range(1,42)])
            add_days = st.selectbox('Days', options=['three', 'four', 'five'])
            add_quantitiy = st.number_input('Quantity', min_value=1)


            line = f'line_{add_line}_{add_days}'
            col1, col2, col3 = st.columns(3)
            add = col1.form_submit_button('Add Vacation')
            if add:
                vf.add_vacation_line(add_shift, add_division, add_line, add_days, add_quantitiy, taken=0)
        

            edit = col2.form_submit_button('Edit Vacation')
            if edit:
                vf.update_vacation_line(add_quantitiy, add_shift, add_division, add_line, add_days,)
                

            remove = col3.form_submit_button('Remove Vacation')
            if remove:
                vf.new_db_delete_vacation_line(add_shift, add_division, add_line, add_days)

    with tab4:

        gen.manager_generate_lines(B_SHIFT, DIVISION_1)
        
    with tab5:

      pass


    with tab6:
    
        gen.manager_generate_lines(C_SHIFT, DIVISION_1)

