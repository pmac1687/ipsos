import requests
import datetime


def get_states_data():
    r  = requests.get('https://disease.sh/v3/covid-19/states')
    data = {}
    for dat in r.json():
        dic = {
            'total_cases': dat['cases'],
            'todays_cases': dat['todayCases'],
            'total_deaths': dat['deaths'],
            'todays_deaths': dat['todayDeaths'],
            'date': datetime.datetime.now().strftime("%Y-%m-%d"),
        }
        data[dat['state']] = dic

    return data

def get_country_data():
    r  = requests.get('https://disease.sh/v3/covid-19/countries/usa')
    dat = r.json()
    data = {
            'total_cases': dat['cases'],
            'todays_cases': dat['todayCases'],
            'total_deaths': dat['deaths'],
            'todays_deaths': dat['todayDeaths'],
            'date': datetime.datetime.now().strftime("%Y-%m-%d")
    }
    
    return data

def main():
    states_data = get_states_data()
    usa_data = get_country_data()
    

if __name__ == '__main__':
    main()