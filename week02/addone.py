# addone.py
# This program will add one to a number the user reads in
# Author: Jonathon Grealish

# The string that the user's input returns must be converted into an integer, not text.
number = int(input('Please enter a number: '))
newNumber = number + 1
print ('{} + 1 = {}'.format(number, newNumber))