# This programs rounds a number.
# It only rounds to the nearest even number
# ie. 4.5 to 4, 5.5 to 6, etc.
# Author: Jonathon Grealish

numberToRound = float(input("Enter a float number: "))
roundedNumber = round(numberToRound)

print("{} rounded is {}".format(numberToRound, roundedNumber))