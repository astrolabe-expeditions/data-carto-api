from model.record import records
from flask import make_response

def get_records_service(id_station,id_sensor):
    geojson ={}
    geojson["type"]= "FeatureCollection"
    features =[]
    line ={}
    line["type"]= "LineString"
    coordinates=[]
    try:
        for record in records.objects.filter(sensor_id=id_sensor).filter(latitude__ne=0.0).filter(longitude__ne=0.0):
            feature = {}
            feature["type"] = "Feature"
            geometry ={}
            geometry["type"]= "Point"
            geometry["coordinates"] = [float(record.longitude),float(record.latitude)]
            coordinates.append([float(record.longitude),float(record.latitude)])
            feature["geometry"] = geometry
            properies = {}
            properies["recorded_at"] = record.recorded_at
            properies["battery_voltage"] = float(record.battery_voltage)
            properies["battery_percentage"] =float(record.battery_percentage)
            properies["pression_ext"] =float(record.pression_ext)
            properies["temp_ext"] = float(record.temp_ext)
            properies["temp_int"] = float(record.temp_int)
            properies["temp_sea_mean"] = float(record.temp_sea_mean)
            properies["ec_sea_mean"] = float(record.ec_sea_mean)
            properies["salinity"] = float(record.salinity)
            feature["properties"] = properies
            features.append(feature)
        line["coordinates"] = coordinates
        line["properties"] = {}

        features.append(line)
        
        geojson["features"] = features
        return geojson
    except Exception as e:
        return make_response({'message' : str(e)}, 404)
   
