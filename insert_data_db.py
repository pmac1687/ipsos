from pull_data_from_api import get_states_data, get_country_data
import psycopg2
import os
import config


DATABASE = os.getenv("DATABASE")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")


def insert_states_data(states_data):
    conn = psycopg2.connect(database=DATABASE, user=USER, password=PASSWORD, host=HOST, port=PORT)
    cur = conn.cursor()
    states = list(states_data.keys())
    for state in states:
        sd = states_data
        tbl = f'{state.replace(" ", "_").lower()}_table'
        #cur.execute(f"""insert into {tbl} (date, total_cases,todays_cases,
                        #total_deaths, todays_deaths) values ('{sd[state]['date']}',
                        #{sd[state]['total_cases']}, {sd[state]['todays_cases']},
                        #{sd[state]['total_deaths']}, {sd[state]['todays_deaths']}) ;""")

        cur.execute(f"""insert into  master_states_table values ('{state}') ;""")
        print(tbl)
        
    conn.commit()
    conn.close()


def insert_country_data(data):
    conn = psycopg2.connect(database=DATABASE, user=USER, password=PASSWORD, host=HOST, port=PORT)
    cur = conn.cursor()
    cur.execute(f"""insert into usa_totals (date , total_cases , todays_cases ,
                    total_deaths , todays_deaths) values ('{data['date']}', 
                    {data['total_cases']},{data['todays_cases']},
                    {data['total_deaths']}, {data['todays_deaths']}) ;""")
    conn.commit()
    conn.close()

def main():
    states_data = get_states_data()
    insert_states_data(states_data)
    #usa_data = get_country_data()
    #insert_country_data(usa_data)

if __name__ == '__main__':
    main()