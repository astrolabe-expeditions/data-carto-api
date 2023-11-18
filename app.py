from flask import Flask
from flask_pymongo import PyMongo
from api.stations import stations_route
from api.sensors import sensors_route
from api.records import records_route



app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb+srv://beni:zhNDcBpSao6XSYLt@cluster0.kchl1nq.mongodb.net/?retryWrites=true&w=majority"
mongo = PyMongo(app)

app.register_blueprint(stations_route)
app.register_blueprint(sensors_route)
app.register_blueprint(records_route)



if __name__ == "__main__":
     app.run(host="0.0.0.0")