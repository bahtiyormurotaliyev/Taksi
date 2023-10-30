from taxicompany import TaxiCompany
class Trip:
    def __init__(self, baslangich, bitis):
        self.baslangic = baslangich
        self.bitis = bitis

    def toString(self):
        return f"{self.baslangich},{self.bitis}"
