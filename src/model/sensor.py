from mongoengine import Document, StringField, IntField, DateTimeField, ObjectIdField


class sensors(Document):
    identifier = StringField(required=True)
    type = StringField(required=True)
    nbr_measures = IntField(required=True)
    station_id = ObjectIdField(required=True)
    created_at = DateTimeField(required=True)
    created_by_id = StringField(required=False)
    updated_at = DateTimeField(required=True)
    updated_by_id = StringField(required=False)
    deleted_at = DateTimeField(required=False)
    deleted_by_id = StringField(required=False)
    deleted = StringField(required=False)