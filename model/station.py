from mongoengine import Document, StringField


class stations(Document):
    description = StringField(required=True)
    image_url = StringField(required=True)
    latitude = StringField(required=False)
    longitude = StringField(required=False)
    name = StringField(required=True)
    type = StringField(required=True)