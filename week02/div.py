# This program reads two numbers and
# will output the integer answer
# and the remainder if applicable.

x = int(input("Enter first number: "))
y = int(input("Enter the number you want to divide by: "))

answer = int(x//y) # // gives the integer division
remainder = x%y # % gives the remainder

print("{} divided by {} is {} with remainder {}".format(x,y,answer,remainder))