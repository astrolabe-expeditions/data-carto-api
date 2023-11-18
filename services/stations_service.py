from app import mongo
def get_stations_service():
    stations = []
    db=mongo['data_caro']
    collecttion = db['stations']
    collecttion.find_one_or_404()
    for i in range (0,10):

        station_data = {}
        station_data['id'] = i
        station_data['name'] = 'name'
        station_data['type'] = 'type'
        station_data['latitude'] = 'latitude'
        station_data['longitude'] = 'longitude'
        station_data['description'] = 'description'
        station_data['image_url'] = 'image_url'
        station_data['sensors'] = 'sensors'
        
    
        stations.append(station_data)

    return {"stations": stations}

