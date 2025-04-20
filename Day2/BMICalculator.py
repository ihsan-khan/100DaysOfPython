# BMI Calculator
# This program calculates the Body Mass Index (BMI) based on user input for height and weight.
# It demonstrates the use of basic arithmetic operations and type conversion in Python.
# The BMI is calculated using the formula: weight (kg) / (height (m) ** 2)
# The result is rounded to two decimal places for better readability.

print("Welcome to the BMI Calculator")
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")
bmi = int(weight) / float(height) ** 2
bmi = round(bmi, 2)
print("Your BMI is " + str(bmi))