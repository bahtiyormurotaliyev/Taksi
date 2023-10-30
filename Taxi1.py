class Taxi:
    def __init__(self):
        self.yolchi = None

    def beginTrip(self, destination):
        self.yolchi = destination

    def terminateTrip(self):
        self.yolchi = None