import sqlite3
import streamlit as st


conn = sqlite3.connect('vaca.db')
c = conn.cursor()



def get_data():
    data = c.execute("SELECT line , available FROM vacation_lines")
    return data

data = get_data()


def get_num(line):
    num = c.execute("SELECT line, available FROM vacation_lines WHERE line=(?)", (line,))
    return num.fetchone()[1]
    #c.execute("SELECT available FROM vacation_lines WHERE line=line", {'line': num}):

def add_bid(line, num):
    num -= 1
    c.execute("UPDATE vacation_lines SET available = (?) WHERE line = (?) ", (num, line,))
    conn.commit()
  

def remove(line, num):
    num += 1
    c.execute("UPDATE vacation_lines SET available = (?) WHERE line = (?)", (num, line,))
    conn.commit()
    

st.subheader("[Line 1](#line-1)")

with st.container():
    col1, col2, col3, col4, col5 = st.columns([1,1,1,0.5,1])
    num = get_num('line_1_three')
    col1.write('3 days')
    col2.metric('Num of Picks Left', num)
    if num == 0:
        col3.warning('SOLD OUT!')
        col4.button('N/A', disabled=True)
        col5.button('Remove', on_click=remove, args=['line_1_three', num] )
    else:
        col3.info('OPEN')
        col4.button('Bid', key=['line_1_three.1'], on_click=add_bid, args=['line_1_three', num])
        col5.button('Remove', key=['line_1_three.2'],on_click=remove, args=['line_1_three', num] )


with st.container():
    col1, col2, col3, col4, col5 = st.columns([1,1,1,0.5,1])
    num = get_num('line_1_four')
    col1.write('4 days')
    col2.metric('Num of Picks Left', num)
    if num == 0:
        col3.warning('SOLD OUT')
        col4.button('N/A', disabled=True)
        col5.button('Remove', on_click=remove, args=['line_1_four', num])
    else:
        col3.info('OPEN')
        col4.button('Bid', key=['line_1_four'], on_click=add_bid, args=['line_1_four', num])
        col5.button('Remove', key=['line_1_four.5'], on_click=remove, args=['line_1_four', num])

with st.container():
    col1, col2, col3, col4, col5 = st.columns([1,1,1,0.5,1])
    num = get_num('line_1_five')
    col1.write('5 days')
    col2.metric('Num of Picks Left', num)
    if num == 0:
        col3.warning('SOLD OUT')
        col4.button('N/A', disabled=True)
        col5.button('Remove', on_click=remove, args=['line_1_five', num])
    else:
        col3.info('OPEN')
        col4.button('Bid', key=['line_1_five'], on_click=add_bid,args=['line_1_five', num])
        col5.button('Remove', key=['line_1_five.5'], on_click=remove, args=['line_1_five', num])


#get_all = c.execute("SELECT line, available FROM vacation_lines")
#print(get_all.fetchall()[0][0])


for i in range (2,41):

    st.subheader(f"[Line {i}](#line-{i})")

    with st.container():
        col1, col2, col3, col4, col5 = st.columns([1,1,1,0.5,1])
        num = get_num(f'line_{i}_three')
        col1.write('3 days')
        col2.metric('Num of Picks Left', num)
        if num == 0:
            col3.warning('SOLD OUT!')
            col4.button('N/A', key=[f'line_{i}_three.1'], disabled=True)
            col5.button('Remove', key=[f'line_{i}_three.2'], on_click=remove, args=[f'line_{i}_three', num] )
        else:
            col3.info('OPEN')
            col4.button('Bid', key=[f'line_{i}_three.3'], on_click=add_bid, args=[f'line_{i}_three', num])
            col5.button('Remove', key=[f'line_{i}_three.4'],on_click=remove, args=[f'line_{i}_three', num] )


    with st.container():
        col1, col2, col3, col4, col5 = st.columns([1,1,1,0.5,1])
        num = get_num(f'line_{i}_four')
        col1.write('4 days')
        col2.metric('Num of Picks Left', num)
        if num == 0:
            col3.warning('SOLD OUT')
            col4.button('N/A',key=[f'line_{i}_four.1'], disabled=True)
            col5.button('Remove',key=[f'line_{i}_four.2'], on_click=remove, args=[f'line_{i}_four', num])
        else:
            col3.info('OPEN')
            col4.button('Bid', key=[f'line_{i}_four.3'], on_click=add_bid, args=[f'line_{i}_four', num])
            col5.button('Remove', key=[f'line_{i}_four.4'], on_click=remove, args=[f'line_{i}_four', num])

    with st.container():
        col1, col2, col3, col4, col5 = st.columns([1,1,1,0.5,1])
        num = get_num(f'line_{i}_five')
        col1.write('5 days')
        col2.metric('Num of Picks Left', num)
        if num == 0:
            col3.warning('SOLD OUT')
            col4.button('N/A', key=[f'line_{i}_five.1'], disabled=True)
            col5.button('Remove',key=[f'line_{i}_five.2'], on_click=remove, args=[f'line_{i}_five', num])
        else:
            col3.info('OPEN')
            col4.button('Bid', key=[f'line_{i}_five.3'], on_click=add_bid,args=[f'line_{i}_five', num])
            col5.button('Remove', key=[f'line_{i}_five.4'], on_click=remove, args=[f'line_{i}_five', num])