from flask import Blueprint, request
from services.sensors_service import get_sensors_service
sensors_route = Blueprint('sensors_route', __name__)

@sensors_route.route("/api/v1/stations/<path:id_station>/sensors", methods=['GET'])
def get_sensors(id_station):
    return get_sensors_service(id_station)