
import streamlit as st
import pandas as pd
from deta import Deta
from secrets import *


deta = Deta(st.secrets["project_key"])

counters = deta.Base('COUNTERS')
employee = deta.Base('EMPLOYEES')
vacation_lines = deta.Base('VACATION_LINES')
vacation_picks = deta.Base('VACATION_PICKS')

@st.cache
def upload_data():
    file = pd.read_csv('assets/BshiftbiddersExport.csv')
    df = pd.DataFrame(file)
    return df

### INDEX COUNTER CRUD ###
def put_vaction_line_counter(shift, division, count):
    counters.put({"DIVISION": division, "SHIFT": shift, "COUNT": count}, key=f'{shift}{division}')
    st.success(f' Line count updated to {count}')

def get_vacation_line_counter(shift, division):
    counter = counters.get(f'{shift}{division}') 
    return counter["COUNT"]

def update_vacation_line_counter(shift, division, count):
    counters.update({"COUNT": count}, key=f'{shift}{division}')
    st.session_state.index_counter = count


def delete_vacation_line_counter(shift, division):
    counters.delete(key=f'{shift}{division}')
    st.success(f'{shift} Shift Division {division} counter was deleted.')

### Employee CRUD ###
def put_update_employee(year, shift, division, seniority_date, name):
    employee.put({"YEAR": year, "SHIFT": shift, "DIVISION": division, "SENIORITY_DATE": seniority_date, "NAME": name, "PICKS": []}, key=f'{year}{shift}{division}{name}')
    st.success(f'{name} was added/updated to databse.')

def get_employee(year, shift, division, name):
    return employee.get(f'{year}{shift}{division}{name}')

def update_employee(year, shift, division, name, **kwargs):
    updates = {}        
    for kwarg in kwargs:
        key, value = kwarg
        updates.update(key, value)
    employee.update(updates, f'{year}{shift}{division}{name}')    

def delete_employee(year, shift, division, name):
    employee.delete({f'{year}{shift}{division}{name}'})
    st.success(f'{name} was deleted from database.')

def read_employee(**kwargs):
    employee_list = []
    for kwarg in kwargs:
        e = employee.fetch({"NAME": kwarg})
        employee_list.append(e.items)
    return employee_list
    
### VACATION LINES CRUD ###

def get_all_lines_filtered(year, shift, division):
    all_vacation_lines = vacation_lines.fetch([{"YEAR?gt": year}, {"SHIFT": shift}, {"DIVISION": division}])
    return all_vacation_lines.items

def create_vacation_line(year, shift, division, line_number, number_of_days, quantity):
    vacation_lines.put({"YEAR": year, "SHIFT": shift, 'DIVISION': division, "LINE_NUMBER": line_number, "NUMBER_OF_DAYS": number_of_days, "QUANTITIY": quantity,}, f'{year}{shift}{division}{line_number}{number_of_days}')
    st.success(f'{shift} {division} {line_number} {number_of_days} added.')

def update_vacation_line(year, shift, division, line_number, number_of_days, quantity, index):
    vacation_lines.update({"QUANTITIY": quantity}, key=f'{year}{shift}{division}{line_number}{number_of_days}')
    counters.update({"COUNT": index}, f'{shift}{division}')


def delete_vacation_line(year, shift, division, line_number, number_of_days):
    vacation_lines.delete({f'{year}{shift}{division}{line_number}{number_of_days}'})
    

def get_vacation_line(year, shift, division, line_number, number_of_days):
    vacation_line = vacation_lines.get(f'{year}{shift}{division}{line_number}{number_of_days}')
    return vacation_line

### VACATION PICK CRUD ###  
def create_update_vacation_pick(year, shift, division, line_number, number_of_days, num, index, name):
    vacation_picks.put({"YEAR": year, "SHIFT": shift, 'DIVISION': division, "LINE_NUMBER": line_number, "NUMBER_OF_DAYS": number_of_days, "NAME": name}, f'{year}{shift}{division}{line_number}{number_of_days}{name}')
    vacation_lines.update({"QUANTITIY": num} ,f'{year}{shift}{division}{line_number}{number_of_days}')
    counters.update({'COUNT': index}, f'{shift}{division}')
    st.session_state.last_pick = f'Line {line_number} {number_of_days} day.'
    
def add_person_too_line(year, shift, division, line_number, number_of_days, name):
    vacation_picks.put({"YEAR": year, "SHIFT": shift, 'DIVISION': division, "LINE_NUMBER": line_number, "NUMBER_OF_DAYS": number_of_days, "NAME": name}, f'{year}{shift}{division}{line_number}{number_of_days}{name}')
    st.success(f'{name} was added from Line {line_number} {number_of_days}')

def delete_vacation_pick(year, shift, division, line_number, number_of_days, name):
    vacation_picks.delete(f'{year}{shift}{division}{line_number}{number_of_days}{name}')
    st.success(f'{name} was deleted from Line {line_number} {number_of_days}')

def read_vacation_pick(year, shift, division, line_number, number_of_days):
    vacation_picks = vacation_picks.fetch({"YEAR?gt": year, "SHIFT": shift, 'DIVISION': division, "LINE_NUMBER": line_number, "NUMBER_OF_DAYS": number_of_days})
    return vacation_picks

def current_previous_bidders( df, shift, division):
    index = get_vacation_line_counter(shift, division)
    current_bidder = df[['Ordinal','RscMasterNameCh']].iloc[[index]]
    previous_bidder = df[['Ordinal','RscMasterNameCh']].iloc[[index-1]]
    return current_bidder, previous_bidder, index

@st.cache
def get_people_on_line(year, shift, division, line_number, number_of_days):
    names = vacation_picks.fetch({"YEAR": year,"SHIFT": shift, "DIVISION": division, "LINE_NUMBER": line_number, "NUMBER_OF_DAYS": number_of_days})
    return names

@st.cache
def get_lines():
    lines = vacation_lines.fetch()
    return lines.items

