# bmi.py
# This program will calculate the user's Body Mass Index
# Author: Jonathon Grealish

height = float(input("Enter your height (in m): "))
weight = int(input("Enter your weight (in kg): "))

print ("Your calculated BMI is: ", round(weight / height**2,2))