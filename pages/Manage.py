import streamlit as st
from vacation_functions import VacationFunctions as vf
from line_generator import LineGenerator as gen
import sqlite3
import streamlit as st
import pandas as pd

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

        with st.form('Edit Index Counter'):
            st.subheader('Change Index of Turn')
            index_num = st.number_input('Input Starting Index.', step=1)
            edit_shift = st.selectbox('Shift', options=['A','B','C'])
            edit_division = st.selectbox('Division', options=['1', '2'])
            index_change = st.form_submit_button('Change Index', on_click=vf.edit_index_counter, args=[index_num, edit_shift, edit_division])
            if index_change:
                vf.edit_index_counter(index_num, edit_shift, edit_division)
                st.success(f'Index changed to {index_num}')
        with st.form('Edit Personal Pick', clear_on_submit=False):
            st.subheader('Add/Remove Persons From Lines')
            edit_person = st.text_input('Name')
            edit_shift = st.selectbox('Shift', options=['A','B','C'])
            edit_division = st.selectbox('Division', options=['1', '2'])
            edit_lines = st.selectbox('Select Line', options=[f'{i}' for i in range(1,42)])
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
            st.subheader('Add/Remove/Edit Lines')
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

        with st.sidebar:

            file = pd.read_csv('assets/BshiftbiddersExport.csv')

            current, previous = vf.current_previous_bidders(file, B_SHIFT, DIVISION_1)
            st.warning(f'CURRENT BIDDER: {current.values.any()}')
            st.success(f'{previous.values.any()} PICKED: ')

            num =st.selectbox('Navigate to a Line', [i for i in range(1,42)])
            st.write('Click to navigate:', f'[Line {num}](#line-{num})')


            st.write('Get Names on a Line:')
            col1, col2 = st.columns(2)
            select_shift = col1.selectbox('Shift', options=['A', 'B', 'C'])
            select_division = col2.selectbox('Division', options=['1','2'])
            line = col1.selectbox('Line', options=[i for i in range(1,42)])
            days = col2.selectbox('Days', options=['three', 'four', 'five'])
            click = st.button('Get Names')
            if click:
                try:
                    names = vf.get_names( select_shift, select_division, line, days)
                    for name in names:
                        st.write(name[0])
                    
                    #st.write([name for name in names])
                except sqlite3.OperationalError:
                    st.write('No Picks.')
        

        
        gen.manager_generate_lines(B_SHIFT, DIVISION_1)
        
    with tab5:

      pass


    with tab6:
    
        gen.manager_generate_lines(C_SHIFT, DIVISION_1)

