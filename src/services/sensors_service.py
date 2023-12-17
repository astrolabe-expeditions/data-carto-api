from model.sensor import sensors
from flask import make_response


def get_sensors_service(id):
    sensors_list = []
    try:
        for sensor in sensors.objects(station_id=id):
            sensor_data = {}
            sensor_data['id'] = str(sensor.id)
            sensor_data['identifier'] = sensor.identifier
            sensor_data['nbr_measures'] = sensor.nbr_measures
            sensor_data['station_id'] = str(sensor.station_id)
            sensors_list.append(sensor_data)

        return {"sensors": sensors_list}
    except Exception as e:
        return make_response({'message' : str(e)}, 404)

def get_sensors_id_service(id):
    sensors_id_list = []
    try:
        for sensor in sensors.objects(station_id=id):
            sensors_id_list.append(str(sensor.id))

        return sensors_id_list
    except Exception as e:
        return make_response({'message' : str(e)}, 404)