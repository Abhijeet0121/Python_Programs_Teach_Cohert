import math as m
print(m.pi)

#random.randint() method is used to generate random integers between the given range.

import random
print(random.randint(1, 5))

#Selects a single random item from a list using random.choice()

a = [1, 2, 3, 4, 5, 6]
print(random.choice(a))

#Random numbers depend on the seeding value. For example, 
#if the seeding value is 5 then the output of the below program will always be the same. 
# Therefore, it must not be used for encryption.

#A random.random() method is used to generate random floats between 0.0 to 1.

import random
random.seed(5)
print(random.random())
print(random.random())



#Syntax - random.sample(sequence, length)

from random import sample

a = [1, 2, 3, 4, 5]
print(sample(a,3))

b = (4, 5, 6, 7, 8)
print(sample(b,3))

c = "45678"
print(sample(c,3))


random.shuffle(a)
print("After shuffle : ")
print(a)

random.shuffle(a)
print("\nSecond shuffle : ")
print(a)