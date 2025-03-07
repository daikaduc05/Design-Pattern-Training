
class Observer():
    def __init__(self):
        self.subcriber = []
        self.context = "" 
    def add_subcriber(self, subcriber):
        self.subcriber.append(subcriber)
    def remove_subcriber(self, subcriber):
        self.subcriber.remove(subcriber)
    def notify(self):
        for subcriber in self.subcriber:
            subcriber.update(self.context)

class User():
    def __init__(self, name):
        self.name = name
    def update(self,context):
        print(f'{self.name} is updated in {context}')
        
class Facebook(Observer):
    def __init__(self):
        self.context = "Facebook"
        self.subcriber = []
    

class Zalo(Observer):
    def __init__(self):
        self.context = "Zalo"
        self.subcriber = []


facebook = Facebook()
zalo = Zalo()
user1 = User('duc')
user2 = User('hoang')
user3 = User('thanh')
facebook.add_subcriber(user1)
facebook.add_subcriber(user2)
zalo.add_subcriber(user3)
facebook.notify()
zalo.notify()