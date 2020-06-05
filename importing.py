# ******************** RANDOM LIBRARY *********************

import random as r

# for importing some features of the whole library: from random import "Name of the functions". Eg: from random import random,uniform,randint
# from random import * :  it imports all the functions in the library

# r.seed (1) 

randInt = r.randint(0,10) # start <= N <= end
print(randInt)

randFloat = r.random() # 0.0 <= N < 1.0
print(randFloat)

randUniform = r.uniform(1,1100) # start <= N <= end
print(randUniform)

# choose one element
lst = [1,3,5,7,11]
pickElement = r.choice(lst)
print(pickElement)

# shuffle list
print(lst)
r.shuffle(lst)
print(lst)

# ******************************************************************

# ******************** TIME LIBRARY *********************

import time

currentTime = time.time() # time.clock() --> time.time()
print("hello")
print("World")
pastTime = time.time() # time.clock() --> time.time()
print(pastTime-currentTime)

print("1")
time.sleep(3)
print("2")

for i in range (1,11):
    print(i)
    time.sleep(1)

# ******************************************************************

# ******************** MATH LIBRARY *********************

import math

val = 3.14

sqrtVal = math.sqrt(val)
print(sqrtVal)

expVal = math.exp(val)
print(expVal)

factVal = math.factorial(math.floor(val))
print(factVal)

sinVal = math.sin(val)
print(sinVal)

floorVal = math.floor(val)
print(floorVal)

ceilingVal = math.ceil(val)
print(ceilingVal)

# ******************************************************************
