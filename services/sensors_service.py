
def get_sensors_service():
    sensors = []
    for i in range (0,1):
        sensor_data = {}
        sensor_data['id'] = i
        sensor_data['identifier'] = 'identifier'
        sensor_data['nbr_measures'] = 'nbr_measures'
        sensor_data['station_id'] = 'station_id'
    
        sensors.append(sensor_data)

    return {"sensors": sensors}