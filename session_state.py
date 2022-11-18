import streamlit as st
import sqlite3

conn = sqlite3.connect('vaca.db')
curs = conn.cursor()


num = curs.execute("SELECT * FROM counter")

if 'index' not in st.session_state:
        st.session_state.index = -1

col1, buff, col2 = st.columns([1,0.5,3])

options = {0:'Meekins',1: 'Farr', 2:'Lewis', 3:'Staten'}


def get_next():
    st.session_state.index +=1
    name = options.get(st.session_state.index, 0)
    return name

def get_previous():
    i =st.session_state.index - 1
    name = options.get(i, 0)
    name = f'{name} Picked: Line 1-3 Days'
    return name

def put_next():
    st.session_state.index -= 1
    name = options.get(st.session_state.index, 0)
    return name

def put_previous():
    i = st.session_state.index - 2
    name = options.get(st.session_state.index, 0)
    name = f'{name} Picked Line 1-3 Days'
 

next = st.button('Next Bidder')
previous = st.button('Previous_ Bidder')

if next:
    name=get_next()
    prev = get_previous()
    st.success(f'{prev}')
    st.warning(f'next: {name}')

if previous:
    current_name = put_next()
    prev = put_previous()
    st.success(f'{prev}')
    st.warning(f'{current_name}')
