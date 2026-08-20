n  = int(input("Enter a Divisor: "))
try:
    res = 10 / n
except ZeroDivisionError:
    print("Can't be divided by zero!")
else:
    print(res)


#1. Specific Exceptions
print(" Specific Exceptions")

try:
    # This will cause ValueError
    x = int("str") 
    inv = 1 / x   # Inverse calculation
    
except ValueError:
    print("Not Valid!")
    
except ZeroDivisionError:
    print("Zero has no inverse!")

#2. Multiple Exceptions

print(" Multiple Exceptions")

a = ["10", "twenty", 30]
try:
    # 'twenty' cannot be converted to int
    total = int(a[0]) + int(a[1])  
    
except (ValueError, TypeError) as e:
    print("Error", e)
    
except IndexError:
    print("Index out of range.")



#3. Catch-All Handlers and Their Risks
#Catch-all handler is used to call to catch any exception (similar to else statement). Use only except keyword to define it:

print("Catch-All Handlers and Their Risks")

try:
    # Risky operation: dividing string by number
    res = "100" / 20 
    
except ArithmeticError:
    print("Arithmetic problem.")
    
except:
    print("Something went wrong!")

#4 Raise an Exception
print("#4 Raise an Exception")

def set(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print(f"Age set to {age}")

try:
    set(-5)
except ValueError as e:
    print(e)