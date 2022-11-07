
import streamlit as st

def add_bid(arg):
            st.session_state[f'{arg}'] -= 1
def remove(arg):
    st.session_state[f'{arg}'] += 1

for i in range(1,42):
    with st.sidebar:
        st.subheader(f"[Line {i}](#line-{i})")

    with st.container():

   
        st.subheader(f"[Line {i}](#line-{i})")

        if f"line_{i}_three" not in st.session_state:
            st.session_state[f'line_{i}_three'] = 25
        if f"line_{i}_four" not in st.session_state:
            st.session_state[f'line_{i}_four'] = 2
        if f'line_{i}_five' not in st.session_state:
            st.session_state[f'line_{i}_five'] = 6

        with st.container():
        
            col1, col2, col3, col4, col5 = st.columns([1,1,1,0.5,1])
            col1.write('3 days')
            col2.metric('Num of Picks Left', st.session_state[f'line_{i}_three'])
            if st.session_state[f'line_{i}_three'] == 0:
                col3.warning('SOLD OUT!')
                col4.button('N/A', key=[f'line_{i}_three'], disabled=True)
                col5.button('Remove', key=[f'line_{i}_three'], on_click=remove, args=[f'line_{i}_three'] )
            else:
                col3.info('OPEN')
                col4.button('Bid', key=[f'line_{i}_three'], on_click=add_bid, args=[f'line_{i}_three'])
                col5.button('Remove', key=[f'line_{i+0.5}_three'], on_click=remove, args=[f'line_{i}_three'] )

        with st.container():
        
            col1, col2, col3, col4, col5 = st.columns([1,1,1,0.5,1])
            col1.write('4 days')
            col2.metric('Num of Picks Left', st.session_state[f'line_{i}_four'])
            if st.session_state[f'line_{i}_four'] == 0:
                col3.warning('SOLD OUT')
                col4.button('N/A', key=[f'line_{i}_four'], disabled=True)
                col5.button('Remove', key=[f'line_{i+0.5}_four'], on_click=remove, args=[f'line_{i}_four'])
            else:
                col3.info('OPEN')
                col4.button('Bid', key=[f'line_{i}_four'], on_click=add_bid, args=[f'line_{i}_four'])
                col5.button('Remove', key=[f'line_{i+0.5}_four'], on_click=remove, args=[f'line_{i}_four'])

        with st.container():
         
            col1, col2, col3, col4, col5 = st.columns([1,1,1,0.5,1])
            col1.write('5 days')
            col2.metric('Num of Picks Left', st.session_state[f'line_{i}_five'])
            if st.session_state[f'line_{i}_five'] == 0:
                col3.warning('SOLD OUT')
                col4.button('N/A', key=[f'line_{i}_five'], disabled=True)
                col5.button('Remove', key=[f'line_{i+0.5}_five'], on_click=remove,args=[f'line_{i}_five'])
            else:
                col3.info('OPEN')
                col4.button('Bid', key=[f'line_{i}_five'], on_click=add_bid,args=[f'line_{i}_five'])
                col5.button('Remove', key=[f'line_{i+0.5}_five'], on_click=remove,args=[f'line_{i}_five'])


