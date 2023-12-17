from mongoengine import Document, StringField, BooleanField, DateTimeField


class stations(Document):
    description = StringField(required=True)
    image_url = StringField(required=True)
    latitude = StringField(required=False)
    longitude = StringField(required=False)
    name = StringField(required=True)
    type = StringField(required=True)
    created_at = DateTimeField(required=True)
    created_by_id = StringField(required=False)
    updated_at = DateTimeField(required=True)
    updated_by_id = StringField(required=False)
    deleted_at = DateTimeField(required=False)
    deleted_by_id = StringField(required=False)
    deleted = BooleanField(required=False)