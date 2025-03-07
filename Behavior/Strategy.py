from abc import ABC, abstractmethod 
class Operation(ABC):
    @abstractmethod
    def calculate(self, a, b):
        pass

class Add(Operation):
    def calculate(self, a, b):
        return a + b

class Subtract(Operation):
    def calculate(self, a, b):
        return a - b

class Multiple(Operation):
    def calculate(self, a, b):
        return a * b
    
class Calculator():
    operation : Operation
    def __init__(self,operation : Operation):
        self.operation = operation
    def calculate(self,a,b):
        return self.operation.calculate(a,b)

calculator = Calculator(Add())
print(calculator.calculate(1,2))
calculator = Calculator(Subtract())
print(calculator.calculate(1,2))