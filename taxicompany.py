from taxi import Taxi
from invalidtaxiname import InvalidTaxiName
class TaxiCompany:
    def __init__(self):
        self._taxi_list:list[Taxi] = []

    def addTaxi(self, taxi:Taxi):
        for i in self._taxi_list:
            if i._id== taxi._id:
               raise InvalidTaxiName
               return
            
        self._taxi_list.append(taxi)

    def getAvailable(self):
        return self._taxi_list


company = TaxiCompany()
taxi1 = Taxi("123")
taxi2 = Taxi("456")
taxi3 = Taxi("123")

try:
    company.addTaxi(taxi1)
    company.addTaxi(taxi2)
    company.addTaxi(taxi3)
except InvalidTaxiName as e:
    print("Invalid taxi name:", str(e))

available_taxis = company.getAvailable()
for taxi in available_taxis:
    print(str(taxi))