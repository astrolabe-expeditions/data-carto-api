from mongoengine import Document, StringField,FloatField,DateTimeField,ListField


class records(Document):
    latitude = StringField(required=False)
    longitude = StringField(required=False)
    recorded_at = DateTimeField(required=True)
    battery_voltage = FloatField(required=False)
    battery_percentage = FloatField(required=False)
    pression_ext = FloatField(required=False)
    temp_ext = FloatField(required=False)
    temp_int = FloatField(required=False)
    temp_sea = ListField(FloatField())
    temp_sea_mean = FloatField(required=True)
    ec_sea = ListField(FloatField())
    ec_sea_mean = FloatField(required=True)
    salinity = FloatField(required=True)
    depth = FloatField(required=False)
    sensor_id = StringField(required=True)