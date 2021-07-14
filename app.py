# importing the flask library files
from flask import Flask
import simplejson as json
from flask_cors import CORS
import main



#create flask web app object
app = Flask(__name__)
CORS(app)

@app.route("/todayStates")
def get_States_today():
    data = main.get_states()

    return json.dumps(data)

@app.route("/todayStatesTop5")
def get_States_5():
    data = main.get_states()

    data = main.get_top_5(data)

    return json.dumps(data)

@app.route("/todayByCountry")
def get_table():
    data = main.get_today_country()

    return json.dumps(data)

#run the app
if __name__ == "__main__":
    app.run(debug=True)