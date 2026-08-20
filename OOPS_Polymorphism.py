#Polymorphism means "many forms" and allows the same method, function or operator to
#behave differently depending on the object or data it works with. 
# This flexibility helps create more reusable, maintainable and scalable code.


#-Complie Time Poly - Overloading
#Compile-time polymorphism involves selecting a method or operation before program execution,
#  typically through method or operator overloading

class Calculator:
    def multiply(self, a=1, b=1, *args):
        result = a * b
        for num in args:
            result *= num
        return result

# Create object
calc = Calculator()

# Using default arguments
print(calc.multiply())            
print(calc.multiply(4))           

# Using multiple arguments
print(calc.multiply(2, 3))       
print(calc.multiply(2, 3, 4))


#RUNTIME POLY- Overriding 
#Runtime polymorphism means that the behavior of a method is decided while program is running,
#based on the object calling it.
#  This happens through Method Overriding a child class provides its own version of a 
# method already defined in the parent class

class Animal:
    def sound(self):
        return "Some generic sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

# Polymorphic behavior
animals = [Dog(), Cat(), Animal()]
for a in animals:
    print(a.sound())


#Polymorphism in Functions

class Pen:
    def use(self):
        return "Writing"

class Eraser:
    def use(self):
        return "Erasing"

def perform_task(tool):
    print(tool.use())

perform_task(Pen())
perform_task(Eraser())