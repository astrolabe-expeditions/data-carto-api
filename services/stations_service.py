from model.station import stations
from services.sensors_service import get_sensors_id_service
from flask import make_response

def get_stations_service():
    station_list=[]
    try:
        for station in stations.objects:
            station_data = {}
            station_data['id'] = str(station.id)
            station_data['description'] = station.description
            station_data['image_url'] = station.image_url
            station_data['latitude'] = station.latitude
            station_data['longitude'] = station.longitude
            station_data['name'] = station.name
            station_data['type'] = station.type
            station_data['sensors'] = get_sensors_id_service(str(station.id))

            station_list.append(station_data)

        return {"stations": station_list}
    except Exception as e:
        return make_response({'message' : str(e)}, 404)  
