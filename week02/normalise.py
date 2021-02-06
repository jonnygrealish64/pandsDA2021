# This program reads in a string and will
# strip any leading or trailing spaces.
# It also converts all letters to lower case
# It also outputs the length of the
# original string and the normalised one.
# Author: Jonathon Grealish

rawString = input("Please enter a string: ")
normalisedString = rawString.strip().lower()

lengthOfRawString = len(rawString)
lengthOfNormalised = len(normalisedString)

print("That string normalised is : {}".format(normalisedString))
print("We reduced the input string from {} to {} characters".format(lengthOfRawString, lengthOfNormalised ))