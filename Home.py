import sqlite3
import streamlit as st


st.set_page_config(layout='wide')

with st.container():
    COL1,COL2,COL3 = st.columns([1,0.5,1])

    with COL1:
        
        st.header('MFD Telestaff Vacation Tracker')
        st.markdown('_presented by..._')
        st.subheader('The MFD TeleStaff Team')

        st.write('''Please follow the link on the left side of the screen to your respective bidding area.
                    This web app was made in house my members of the Telestaff team. This is a simple tool 
                    for personnel to help track vacation line openeings and closings. Although accurate, if 
                    a descrpencie should arise, Telestaff will have final authority on line closure and openeings. 
                      ''')
        '---'
        st.subheader('Some house keeping...')

        st.write('''
                    - Please have your bids written down and given to a person who will keep up with picks
                    - Make picks on radio channel E10
                    - Read line number and days ONLY over the radio, no dates need to be transferred over the radio
                    - All picks are final. Once the next person enters their the bid, no changes will be made to the preceding bid 
                    - You can watch the actual bids being placed into telestaff in realtime via the teams link sent out this morning. 

        ''')


    with COL3:
        st.image('assets/mfd_logo copy.jpeg', width=350,)
        pass