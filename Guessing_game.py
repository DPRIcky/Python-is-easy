from random import randint

randVal = randint(0,100)

while(True):
    guess = int(input("Enter your guess: "))
    if guess == randVal:
        break
    elif guess<randVal:
        print("Your guess was too loo")
    else:
        print("Too high")
print("You guessed correctly with:",guess)

from random import random
from time import time

randVal = random()
upper = 1.0
lower = 0.0

startTime = time()

while(True):
    guess = (upper+lower)/2
    print(guess)  
    if guess == randVal:
        break
    elif guess<randVal:
        print("Guess was too loo")
        lower = guess
    else:
        print("Too high")
        upper = guess

endTime = time()
timerequired = endTime-startTime
print("Guessed correctly with:",guess,"in",timerequired,"seconds")
