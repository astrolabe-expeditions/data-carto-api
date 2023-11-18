from mongoengine import Document, StringField,IntField


class sensors(Document):
    identifier = StringField(required=True)
    nbr_measures = IntField(required=True)
    station_id = StringField(required=True)