from abc import ABC
class MainIngredient(ABC):
    pass

class ExtraIngredient(ABC):
    pass

class Cacao(MainIngredient):
    def __str__(self):
        return 'Cacao'
class Coffe(MainIngredient):
    def __str__(self):
        return 'Coffe'

class Milk(ExtraIngredient):
    def __str__(self):
        return 'Milk'
class Cream(ExtraIngredient):
    def __str__(self):
        return 'Cream'
class Salt(ExtraIngredient):
    def __str__(self):
        return 'Salt'
    
class Bartender(): #this is bridge class
    def __init__(self,extra_ingredient,main_ingredient):
        self.main_ingredient = main_ingredient
        self.extra_ingredient = extra_ingredient
    def __str__(self):
        extra_names = ', '.join(str(x) for x in self.extra_ingredient)  # Chuyển object thành string
        return f'{self.main_ingredient} with {extra_names}'
    

cacao = Cacao()
milk = Milk()
coffe = Coffe()
cream = Cream()
salt = Salt()


milk_coffe = Bartender([milk,salt],coffe)
cacao_salt = Bartender([salt],cacao)

print(cacao_salt)
print(milk_coffe)