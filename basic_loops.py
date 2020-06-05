# Fizz Buzz Problem #
for num in range(101):
    if (num%3 == 0):
        print("Fizz")
    elif(num % 5 == 0):
        print("Buzz")
    elif (num%3 == 0 and num % 5 == 0):
        print("FizzBuzz")
    elif(num>1):
        for i in range(2,num//2):
            if (num % i)!=0:
                print("Prime")
                break
            else:
                print(num)
    else:
        print(num)