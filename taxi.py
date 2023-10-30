class Taxi:
    def __init__(self, id):
        self._id = id
        
    def beginTrip(self, destination):
        self.yolchi = destination

    def terminateTrip(self):
        self.yolchi = None
    def __str__(self):
        return f"Taxi ID: {self._id}"