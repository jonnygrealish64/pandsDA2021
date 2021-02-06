# This program prints out a random fruit

import random

fruits = ("Apple", "Orange", "Pear", "Banana", "Strawberry", "Raspberry", "Blueberry", "Pineapple", "Kiwi")

# We want a random number between 0 and length-1
index = random.randint(0,len(fruits)-1)

fruit = fruits[index]

print("Here is a random fruit: {}".format(fruit))