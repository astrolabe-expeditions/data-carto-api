from model.record import records
from flask import make_response
from datetime import datetime

def get_records_service(id_station,id_sensor,format):


    try:
        record_list=records.objects.filter(sensor_id=id_sensor).filter(latitude__ne="0.0").filter(longitude__ne="0.0").order_by('+recorded_at')

        if(format == "json"):
            return get_json_from_record(record_list)
        else:
            return get_geojson_from_record(record_list)
    except Exception as e:
        return make_response({'message' : str(e)}, 404)

def get_geojson_from_record(record_list):
    geojson ={}
    geojson["type"]= "FeatureCollection"
    features =[]
    line ={}
    line["type"]="Feature"
    coordinates=[]

    for record in record_list:
        feature = {}
        feature["type"] = "Feature"
        geometry ={}
        geometry["type"]= "Point"
        geometry["coordinates"] = [float(record.longitude),float(record.latitude)]
        coordinates.append([float(record.longitude),float(record.latitude)])
        feature["geometry"] = geometry
        properies = {}
        properies["recorded_at"] = record.recorded_at
        properies["battery_voltage"] = return_float_or_none(record.battery_voltage)
        properies["battery_percentage"] =return_float_or_none(record.battery_percentage)
        properies["pression_ext"] =return_float_or_none(record.pression_ext)
        properies["temp_ext"] = return_float_or_none(record.temp_ext)
        properies["temp_int"] = return_float_or_none(record.temp_int)
        properies["temp_sea_mean"] = return_float_or_none(record.temp_sea_mean)
        properies["ec_sea_mean"] = return_float_or_none(record.ec_sea_mean)
        properies["salinity"] = return_float_or_none(record.salinity)
        properies["depth"] = return_float_or_none(record.depth)
        feature["properties"] = properies
        features.append(feature)
    line_geometry ={}
    line_geometry["type"] = "LineString"
    line_geometry["coordinates"] = coordinates
    line["geometry"] = line_geometry
    line["properties"] = {}

    features.append(line)
    geojson["features"] = features
    return geojson

def get_json_from_record(record_list):

    json = []
    for record in record_list:
        record_data = {}
        record_data["longitude"] = return_float_or_none(record.longitude)
        record_data["latitude"] = return_float_or_none(record.longitude)
        record_data["recorded_at"] = record.recorded_at
        record_data["battery_voltage"] = return_float_or_none(record.battery_voltage)
        record_data["battery_percentage"] =return_float_or_none(record.battery_percentage)
        record_data["pression_ext"] =return_float_or_none(record.pression_ext)
        record_data["temp_ext"] = return_float_or_none(record.temp_ext)
        record_data["temp_int"] = return_float_or_none(record.temp_int)
        record_data["temp_sea_mean"] = return_float_or_none(record.temp_sea_mean)
        record_data["ec_sea_mean"] = return_float_or_none(record.ec_sea_mean)
        record_data["salinity"] = return_float_or_none(record.salinity)
        properies["depth"] = return_float_or_none(record.depth)
        json.append(record_data)
    return {"records":json}


def return_float_or_none(value):
    if(value is None):
        return None
    return float(value)

