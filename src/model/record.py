from mongoengine import Document, StringField,FloatField,DateTimeField,ListField


class records(Document):
    latitude = StringField(required=True)
    longitude = StringField(required=True)
    recorded_at = DateTimeField(required=True)
    battery_voltage = FloatField(required=True)
    battery_percentage = FloatField(required=True)
    pression_ext = FloatField(required=True)
    temp_ext = FloatField(required=True)
    temp_int = FloatField(required=True)
    temp_sea = ListField(FloatField())
    temp_sea_mean = FloatField(required=True)
    ec_sea = ListField(FloatField())
    ec_sea_mean = FloatField(required=True)
    salinity = FloatField(required=True)
    sensor_id = StringField(required=True)