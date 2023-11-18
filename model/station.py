class Station :

    def __init__(self, id, name,type,latitude,longitude,description,image_url,sensors):
        self.id = id
        self.name = name
        self.type = type
        self.latitude = latitude
        self.longitude = longitude
        self.description = description
        self.image_url = image_url
        self.sensors = sensors