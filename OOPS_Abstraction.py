#Abstract Base Class (ABC) is used to achieve data abstraction by defining a common interface for its subclasses.
#It cannot be instantiated directly and serves as a blueprint for other classes

from abc import ABC, abstractmethod

class Greet(ABC):
    @abstractmethod
    def say_hello(self):
        pass  # Abstract method

class English(Greet):
    def say_hello(self):
        return "Hello!"

g = English()
print(g.say_hello())


#static method in Python is a method defined inside a class that does not depend on any instance or class data.
class Calc:
    @staticmethod
    def add(a, b):
        return a + b

res = Calc.add(2, 3)
print(res)