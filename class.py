class Calculator():
    def soma(self, x, y): # Needs to use self as first parameter as it is a method of the class Calculator
        return x + y

c = Calculator() # Instantiating the class in an object

print(c.soma(1, 2))

class Person():
    def __init__(self, name, age): # Constructor method
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"

people = [
    Person("Gabriel", 30),
    Person("Maria", 25),
    Person("João", 40)
]

people.sort(key=lambda person: person.age) # Sorting people by age and using lambda function

print(people)