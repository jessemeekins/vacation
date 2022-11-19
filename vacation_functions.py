import sqlite3
import streamlit as st
import pandas as pd

conn = sqlite3.connect('vaca.db', check_same_thread=False)
curs = conn.cursor()

class VacationFunctions:


    def edit_index_counter( index_number, shift, division):
        curs.execute("UPDATE counter SET count = (?) WHERE shift = (?) AND division = (?)", (index_number, shift, division))
        conn.commit()

    def get_index_counter(shift, division):
        count = curs.execute("SELECT count FROM counter WHERE shift = (?) AND division = (?)", (shift, division,))
        count = count.fetchall()[0][0]
        return count

    def current_previous_bidders( file, SHIFT, DIVISION):
        index = VacationFunctions.get_index_counter( SHIFT, DIVISION)

        df = pd.DataFrame(file)

        current_bidder = df[['Ordinal','RscMasterNameCh']].iloc[[index]]
        previous_bidder = df[['Ordinal','RscMasterNameCh']].iloc[[index-1]]

        return current_bidder, previous_bidder

    ######## EDIT PERSON FORM UNDER MANAGE ##############

    def remove_person_from_line(line, name):
        #try:
        curs.execute(f"DELETE FROM {line} WHERE name = '{name}'")
        conn.commit()
        st.success('Employee\'s bid removed.')
        #except:
        #    st.warning('Unable to remove bid.')
    def add_person_too_line(line, name):
        curs.execute(f"INSERT INTO {line} VALUES (?)", (name,))
        conn.commit()
        st.success('Employee added to line.')

    #### UPDATE VACATION LINES #####

    def update_vacation_line(quantitiy, shift, division, line_num, num_of_days,):
        curs.execute("UPDATE mfd_vacations SET QUANTITIY = (?) WHERE shift = (?) AND division = (?) AND line_number = (?) AND number_of_days = (?)", (quantitiy, shift, division, line_num, num_of_days))
        conn.commit()
        st.success(f'{shift} Shift D{division} Line {line_num} {num_of_days} updated.')
        


    def get_names(shift, division, line, days):
        concat = f'{shift}_{division}_{line}_{days}'
        data = conn.execute(f"SELECT * FROM {concat}")
        data = data.fetchall()
        return data

    def get_num( line):
        num = curs.execute("SELECT available FROM vacation_lines WHERE line=(?)", (line,))
        return num.fetchone()[0]
        #c.execute("SELECT available FROM vacation_lines WHERE line=line", {'line': num}):

    def new_bd_get_num(shift, division, line_num, type):
        string = f'{shift}_{division}_{line_num}_{type}'
        num = curs.execute("SELECT quantitiy FROM mfd_vacations WHERE shift = (?) AND division = (?) AND line_number = (?) AND number_of_days = (?)", (shift, division, line_num, type,))
        return num.fetchall()[0][0]

    def add_bid(  _line, _num, shift, div, line, num_of_days, name):
        curs.execute(f"CREATE TABLE IF NOT EXISTS {shift}_{div}_{line}_{num_of_days}(name)")
        curs.execute(f"INSERT INTO {shift}_{div}_{line}_{num_of_days} VALUES (?)", (name,))
        conn.commit()

    def new_db_add_bid( quantitiy, shift, division, line_number, num_of_days, name):
        quantitiy -= 1
        count = VacationFunctions.get_index_counter(shift, division)
        count += 1
        curs.execute("UPDATE mfd_vacations SET quantitiy = (?) WHERE shift = (?) AND division = (?) AND line_number = (?) AND number_of_days = (?)", (quantitiy, shift, division, line_number, num_of_days,))
        count = curs.execute("UPDATE counter SET count = (?) WHERE shift = (?) AND division = (?)", (count, shift, division,))
        curs.execute(f"CREATE TABLE IF NOT EXISTS {shift}_{division}_{line_number}_{num_of_days}(name)")
        curs.execute(f"INSERT INTO {shift}_{division}_{line_number}_{num_of_days} VALUES (?)", (name,))
        st.session_state.last_pick = f'Line {line_number} {num_of_days} day'
        conn.commit()
        
    
    def remove(_line, _num):
        _num += 1
        curs.execute("UPDATE vacation_lines SET available = (?) WHERE line = ?", (_num, _line,))
        conn.commit()

    def new_db_remove_bid( quantitiy, shift, division, line_number, num_of_days):
        quantitiy += 1
        count = VacationFunctions.get_index_counter(shift, division)
        count -= 1
        curs.execute("UPDATE mfd_vacations SET quantitiy = (?) WHERE shift = (?) AND division = (?) AND line_number = (?) AND number_of_days = (?)", (quantitiy, shift, division, line_number, num_of_days,))
        count = curs.execute("UPDATE counter SET count = (?) WHERE shift = (?) AND division = (?)", (count, shift, division,))
        conn.commit()

    def add_vacation_line(shift, division, line_number, number_of_days, qt, taken):
       
        curs.execute("INSERT INTO mfd_vacations VALUES( ?, ?, ?, ?, ?, ?);", (shift, division, line_number, number_of_days, qt, taken,))
        conn.commit()
            #check_line = curs.execute("SELECT * FROM mfd_vacations WHERE shift = ? AND division = ? AND line_number = ? AND number_of_days = ?", (shift, division, line_number, number_of_days,))
            #if check_line.fetchall() == None: 
             #   st.success("Vacation Line Added")
            #else:
             #   st.warning('Record Already Exists.')
        #except:
         #   st.warning('Unable to complete.')

    def new_db_delete_vacation_line(shift, division, line_number, number_of_days):
        curs.execute("DELETE FROM mfd_vacations WHERE shift = ? AND division = ? AND line_number = ? AND number_of_days = ?", (shift, division, line_number, number_of_days,))
        conn.commit()
        st.success("Vacation Line deleted.")