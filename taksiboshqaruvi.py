from taxi import Taxi

class TaxiManager:
    def __init__(self):
        self.taksiler = []
        self.boshlar = []
        self.bekor_qilinganlar = []

    def callTaxi(self, passenger):
        if self.taksiler:
            taksi = self.taksiler.pop(0)
            taksi.beginTrip(passenger.place)
            return taksi
        else:
            self.boshlar.append(passenger)
            print("bo'shlar")

    def getLostTrips(self):
        return len(self.bekor_qilinganlar)

    def addTaxi(self, taxi):
        self.taksiler.append(taxi)
