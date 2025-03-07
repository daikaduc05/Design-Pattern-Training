class Charger:
    pass 

class AsiaCharger(Charger):
    def __init__(self,name):
        self.name = name
    def charge_with_two_pin(self):
        print("Charging with two pins")

class EuropeCharger(Charger):
    def __init__(self,name):
        self.name = name
    def charge_with_three_pin(self):
        print("Charging with three pins") 



#yes, i am in europe and power socket in here just have three pin
#but i only have 2 pin charger
#this is solution ->
class Adapter(Charger):
    def __init__(self,charger):
        print(f"This {charger.name} is charging into adapter")
        self.charger = charger
        self.name = charger.name
    def charge_with_three_pin(self):
        self.charger.charge_with_two_pin()


my_charger = AsiaCharger("my asia charger")
adapter = Adapter(my_charger)
adapter.charge_with_three_pin()

