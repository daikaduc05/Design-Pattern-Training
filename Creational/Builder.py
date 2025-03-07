from abc import ABC,abstractmethod


class Pizza():
    def __init__(self):
        self.cheese = "None"
        self.pepperoni = "None"
        self.mushrooms = "None"
        self.size = 0

    def show_pizza(self):
        print(f'Cheese: {self.cheese}, Pepperoni: {self.pepperoni}, Mushrooms: {self.mushrooms}, Size: {self.size}')

class UIPizzaBuilder(ABC):

    @abstractmethod
    def add_cheese():
        pass 
    @abstractmethod
    def add_pepperoni():
        pass
    @abstractmethod
    def add_mushrooms():
        pass
    @abstractmethod
    def construct_size(size):
        pass 

class NormalPizzaBuilder(UIPizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()
    
    def add_cheese(self):
        self.pizza.cheese = "Normal Cheese"
    
    def add_pepperoni(self):
        self.pizza.pepperoni = "Normal Pepperoni"
    
    def add_mushrooms(self):
        self.pizza.mushrooms = "Normal Mushrooms"
    
    def construct_size(self, size):
        self.pizza.size = size

class SpicyPizzaBuilder(UIPizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()
    
    def add_cheese(self):
        self.pizza.cheese = "Spicy Cheese"
    
    def add_pepperoni(self):
        self.pizza.pepperoni = "Spicy Pepperoni"
    
    def add_mushrooms(self):
        self.pizza.mushrooms = "Spicy Mushrooms"
    
    def construct_size(self, size):
        self.pizza.size = size

class PizzaDirector():
    def __init__(self, builder):
        self.builder = builder
    
    def make_full_topping_pizza_pizza(self):
        self.builder.add_cheese()
        self.builder.add_pepperoni()
        self.builder.add_mushrooms()
        self.builder.construct_size(12)
        return self.builder.pizza
    
    def make_pepperoni_less_pizza(self):
        self.builder.add_cheese()
        self.builder.add_mushrooms()
        self.builder.construct_size(12)
        return self.builder.pizza
    
    def make_large_pizza(self):
        self.builder.add_cheese()
        self.builder.add_pepperoni()
        self.builder.add_mushrooms()
        self.builder.construct_size(16)
        return self.builder.pizza


spicy_pizza_builder = SpicyPizzaBuilder()
normal_pizza_builder = NormalPizzaBuilder()
director_pizza = PizzaDirector(spicy_pizza_builder)
spicy_pizza = director_pizza.make_full_topping_pizza_pizza()
spicy_pizza.show_pizza()
director_pizza = PizzaDirector(normal_pizza_builder)
normal_pizza = director_pizza.make_pepperoni_less_pizza()
normal_pizza.show_pizza()