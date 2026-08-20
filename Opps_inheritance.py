#Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class
#to inherit attributes and methods from another class (called a parent or base class).

#parent class Animal is created that has a method info(). Then a child class Dog is created that
# inherits from Animal and adds additional behavior.

class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        print("Animal name:", self.name)

class Dog(Animal):
    def sound(self):
        print(self.name, "barks")

d = Dog("Buddy")
# Inherited method
d.info()     
d.sound()

#Ssuper() function is used to call methods from a superclass following Python’s Method Resolution Order (MRO). In particular,
#  it is commonly used in the child class's __init__() method to initialize inherited attributes.
#  This way, the child class can leverage the functionality of the parent class

# Parent Class: Animal
class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        print("Animal name:", self.name)

# Child Class: Dog
class Dog(Animal):
    def __init__(self, name, breed):
        # Calls constructor based on MRO
        super().__init__(name)  
        self.breed = breed

    def details(self):
        print(self.name, "is a", self.breed)

d = Dog("Buddy", "Golden Retriever")
d.info()      # Parent method
d.details()   # Child method

#Method overriding allows a child class to provide its own implementation of a method 
# that already exists in the parent class.
#  This enables customized behavior while still maintaining the inheritance relationship.

class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

d = Dog()
d.sound()