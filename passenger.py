from place import Place
from taxicompany import TaxiCompany
class Passenger:
    def __init__(self, place, isim):
        self.place = place
        self.isim = isim

    def __str__(self):
        return f"{self.isim}, {self.place}"


joy = Place("Zangiota", "   Xarakat")
passenger = Passenger(joy, "Ali")

print(passenger)
print(joy)