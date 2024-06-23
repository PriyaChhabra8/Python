Lesson 3: Object-Oriented Programming (OOP)
Topic 7: Classes and Objects
Explanation:

Class: Blueprint for creating objects. It defines attributes (data) and methods (functions).
Object: Instance of a class. It encapsulates data and behavior.

# Example of a class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# Creating objects
alice = Person("Alice", 30)
print(alice.greet())  # Output: Hello, my name is Alice and I am 30 years old.

#Define a class for a Car with attributes like make, model, and year.
#Create an instance of the Car class and print its make.


class Car:
    def __init__(self, make,model,year):
        self.make = make
        self.model = model
        self.year = year

my_car = Car('Honda','Jazz',2024)
print(my_car.make)
    
Tips:

init() method initializes object attributes.
Use self to refer to the current instance within a class.

