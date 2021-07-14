import psycopg2
import os
import config
import requests

DATABASE = os.getenv("DATABASE")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")



def create_usa_totals_table():
    conn = psycopg2.connect(database=DATABASE, user=USER, password=PASSWORD, host=HOST, port=PORT)
    cur = conn.cursor()
    que = f"""create table usa_totals (date date, total_cases int, todays_cases int, total_deaths int, todays_deaths int);"""
    print(que)
    cur.execute(que)
    cur.execute("select * from information_schema.tables where table_name='usa_totals';")
    #####  check to see if table is created before commit  #### 
    if bool(cur.fetchone()[0]) == True:
        conn.commit()
        conn.close()
        print('successfully created usa_totals table')
    else:
        print('failed create: usa_totals')
    

def create_master_state_table():
    conn = psycopg2.connect(database=DATABASE, user=USER, password=PASSWORD, host=HOST, port=PORT)
    cur = conn.cursor()
    que = f"""create table master_states_table (state_name text);"""
    cur.execute(que)
    cur.execute("select * from information_schema.tables where table_name='master_states_table';")
    #####  check to see if table is created before commit  ####
    if bool(cur.fetchone()[0]) == True:
        conn.commit()
        conn.close()
        print('successfully created master_states_table')
    else:
        print('failed create: usa_totals')

def get_states_list():
    r  = requests.get('https://disease.sh/v3/covid-19/states')
    states_array = []
    for dat in r.json():
        ####  replace spaces with underscore for SQL  ####
        states_array.append(dat['state'].replace(' ','_'))
    
    return states_array

def create_individual_state_tables(states_arr):
    conn = psycopg2.connect(database=DATABASE, user=USER, password=PASSWORD, host=HOST, port=PORT)
    cur = conn.cursor()
    #######   build tables by state name for each individual state   ######
    query_str = f""
    verify_query_str = f''
    for state in states_arr:
        tbl_name = f'{state}_table'.lower()
        print(tbl_name)
        que = f"""create table {tbl_name} (date date, total_cases int, todays_cases int, total_deaths int, todays_deaths int);"""
        query_str += que
        verify_query_str += f"'{tbl_name}',"
    
    print(verify_query_str)
    cur.execute(query_str)
    verify_query_str = verify_query_str[0:-1].lower()
    print(verify_query_str)
    cur.execute(f"""select * from information_schema.tables where table_name in ({verify_query_str});""")
    if cur.rowcount == len(states_arr):
        conn.commit()
        conn.close()
        print('successfully created master_states_table')
    else:
        print('one or more tables failed creation')
    

def main():
    #create_usa_totals_table()
    create_master_state_table()
    states_arr = get_states_list()
    #create_individual_state_tables(states_arr)



if __name__ == '__main__':
    main()