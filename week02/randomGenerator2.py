# Program that prints out a random number
# between a user's inputted range

import random

x = int(input("Enter first number in the range: "))
y = int(input("Enter last number in the range: "))

number = random.randint(x,y)
print("Here is a random number: {}".format(number))