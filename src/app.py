import os
from flask import Flask
from flask_cors import CORS
from api.stations import stations_route
from api.sensors import sensors_route
from api.records import records_route
from mongoengine import connect
from dotenv import load_dotenv

load_dotenv() # load environment variables from .env file

DEFAULT_PORT = "8080"

app = Flask(__name__)

app.register_blueprint(stations_route)
app.register_blueprint(sensors_route)
app.register_blueprint(records_route)


connect(host=os.environ.get('MONGO_URI'))
CORS(app)


if __name__ == "__main__":
     port_env =  os.getenv("PORT", DEFAULT_PORT)
     port = int(port_env)
     app.run(host="0.0.0.0",port=port)