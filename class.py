class Calculator():
    def soma(self, x, y): # Needs to use self as first parameter as it is a method of the class Calculator
        return x + y

c = Calculator() # Instantiating the class in an object

print(c.soma(1, 2))