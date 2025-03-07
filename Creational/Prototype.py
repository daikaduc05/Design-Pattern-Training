import copy

class Car():
    def __init__(self,corlor,engine):
        self.color = corlor
        self.engine = engine 

    def __str__(self):
        return f'Color: {self.color}, Engine: {self.engine}'

car1 = Car('red',['v1','v2','v3'])
car2 = copy.deepcopy(car1)
car2.color = 'blue'
car2.engine[0] = 'v100'
print(car2)
print(car1)