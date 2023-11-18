from flask import Blueprint, request
from services.records_service import get_records_service

records_route = Blueprint('records_route', __name__)


@records_route.route("/api/v1/stations/<path:id_station>/sensors/<path:id_sensor>/records", methods=['GET'])
def get_records(id_station,id_sensor):
    return get_records_service()