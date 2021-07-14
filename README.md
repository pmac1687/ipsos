# ipsos
etl pipeline

clone repo

$ python3 -m venv venv

$ source venv/bin/activate

$ cd ipsos

$ pip install -r requirements.txt

### build db ###

create config.py with credentials for postgres db

$ python3 build_db.py

### load db ####

$ python3 insert_data_db.py

### run api  ###

$ python3 app.py

### query api ###

http://localhost:5000/todayStates

--> returns dict where keys=states  and dict[state] = [date , total_cases , todays_cases , total_deaths , todays_deaths]

http://localhost:5000/todayStatesTop5

--> returns top results dict:
    
    {"total_cases": ["California", 3845459], "todays_cases": ["", 0],   "total_deaths": ["California", 63918], "todays_deaths": ["", 0]}

http://localhost:5000//todayByCountry

----> return results for the country: [date , total_cases , todays_cases , total_deaths , todays_deaths]

["2021-07-13", 34807813, 0, 623435, 0]

##### results #####

I intended to round out the API so that it would return queries for percentge of change and bi weekly but ran out of time/had to go get my daughter from daycare. I included a .yml with a lambda function that would run the python scripts to load the db on a daily basis. Furthermore i had intended to wrap it all together with docker such that you could run the container and have it build the db and API and deploy it to a ec2 instance. following along to this:

https://github.com/davidmukiibi/docker-flask

https://medium.com/the-andela-way/docker-meets-flask-and-postgres-5259d4a87c03

I hope this is what you were looking for, and can get a sense of my thought process and coding ability from my work and this write up. Had i more time im confident i could get this functioning properly and contanerized for easy deployment to aws.




