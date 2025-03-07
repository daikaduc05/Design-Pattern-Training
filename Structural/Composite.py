from abc import ABC, abstractmethod
class Role(ABC):
    def __str__(self):
        return f'{self.name}' 

class Tree(Role):
    def __init__(self,name):
        self.name = name 
        self.child = []
    def add(self,role : Role):
        self.child.append(role)
    def remove(self,role : Role):
        self.child.remove(role)
    def is_ok_to_delte(self,role : Role):
        if role in self.child:
            return True
        else:
            if(len(self.child) == 0):
                return False
            return any([x.is_ok_to_delte(role) for x in self.child])

# check this role can delete that role

ceo = Tree('CEO')
em = Tree('EM')
engineer = Tree('Engineer')
hr = Tree('HR')
ceo.add(em) 
em.add(engineer)
ceo.add(hr)
print(em.is_ok_to_delte(hr))
print(ceo.is_ok_to_delte(hr))
