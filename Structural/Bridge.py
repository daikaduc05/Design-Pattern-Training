from abc import ABC, abstractmethod

class Ingredient(ABC):
    @abstractmethod
    def prepare_ingredient(self):
        pass

class CoffeeIngredient(Ingredient):
    def prepare_ingredient(self):
        print("Chuẩn bị nguyên liệu cà phê")

class CacaoIngredient(Ingredient):
    def prepare_ingredient(self):
        print("Chuẩn bị nguyên liệu ca-cao")

class Drink(ABC):
    def __init__(self, ingredient: Ingredient):
        self.ingredient = ingredient

    @abstractmethod
    def serve(self):
        pass

class IcedDrink(Drink):
    def serve(self):
        print("Pha đồ uống kiểu đá (Iced).")
        self.ingredient.prepare_ingredient()

class HotDrink(Drink):
    def serve(self):
        print("Pha đồ uống kiểu nóng (Hot).")
        self.ingredient.prepare_ingredient()

iced_coffee = IcedDrink(CoffeeIngredient())
iced_coffee.serve()

print()

hot_cacao = HotDrink(CacaoIngredient())
hot_cacao.serve()
