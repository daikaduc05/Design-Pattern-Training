from abc import ABC 
class Doll(ABC):
    def __str__(self):
        return f'{self.name}'

class OriginalDoll(Doll):
    def __init__(self):
        self.name = f"OriginalDoll()"

class DollDecorator1(Doll):
    def __init__(self,doll: Doll):
        self.name = f"DollDecorator1({doll.name})"

class DollDecorator2(Doll):
    def __init__(self,doll: Doll):
        self.name = f"DollDecorator2({doll.name})"

class DollDecorator3(Doll):
    def __init__(self,doll: Doll):
        self.name = f"DollDecorator3({doll.name})"

doll = OriginalDoll()
doll = DollDecorator1(doll)
doll = DollDecorator3(doll)
doll = DollDecorator2(doll)
print(doll)


