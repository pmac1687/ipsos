import psycopg2
import os
import config
from datetime import date
from datetime import timedelta


DATABASE = os.getenv("DATABASE")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")



def get_top_5(dic):
    top_5 = {}
    top_5['total_cases'] = ['',0]
    top_5['todays_cases'] = ['',0]
    top_5['total_deaths'] = ['',0]
    top_5['todays_deaths'] = ['',0]
    for state, dats in dic.items():
        print(state, dats)
        if dats[1] > top_5['total_cases'][1]:
            top_5['total_cases'] = [state, dats[1]]
        if dats[2] > top_5['todays_cases'][1]:
            top_5['todays_cases'] = [state, dats[2]]
        if dats[3] > top_5['total_deaths'][1]:
            top_5['total_deaths'] = [state, dats[3]]
        if dats[4] > top_5['todays_deaths'][1]:
            top_5['total_deaths'] = [state, dats[4]]

    return top_5
        


def get_states():
    conn = psycopg2.connect(database=DATABASE, user=USER, password=PASSWORD, host=HOST, port=PORT)
    cur = conn.cursor()
    cur.execute("select * from master_states_table;")
    states = cur.fetchall()
    conn.commit()
    today = date.today()
    yesterday = today - timedelta(days = 1)
    dic = {}
    for state in states:
        tbl = f'{state[0].replace(" ","_").lower()}_table'
        print(tbl)
        cur.execute(f"""select *  from {tbl} where date >= '{yesterday}';""")
        #print(cur.fetchone())
        dat = cur.fetchone()
        arr = []
        for d in dat:
            arr.append(d)
        arr[0] = arr[0].strftime("%Y-%m-%d")
        dic[state[0]] = arr

    conn.commit()
    conn.close()


    return dic


def get_today_country():
    conn = psycopg2.connect(database=DATABASE, user=USER, password=PASSWORD, host=HOST, port=PORT)
    cur = conn.cursor()
    today = date.today()
    yesterday = today - timedelta(days = 1)
    cur.execute(f"select * from usa_totals where date >='{yesterday}' ;")
    dats = cur.fetchone()
    conn.commit()
    conn.close()
    data = []
    for item in dats:
        data.append(item)
    data[0] = data[0].strftime("%Y-%m-%d")
    print(data)
    
    return data

def main():
    get_state_top_5()

if __name__ == '__main__':
    main()