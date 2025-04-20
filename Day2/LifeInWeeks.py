# Suppose the reamining life of a person is 90 years. Write a program that calculates the number of days, weeks, and months in the remaining life of a person.
# The program should take the current age of the person as input and calculate the remaining life in days, weeks, and months.
# The program should also display the result in a formatted string.

age = int(input("Enter your current age: "))
remaining_life = 90 - age
remaining_days = remaining_life * 365
remaining_weeks = remaining_life * 52
remaining_months = remaining_life * 12
print(f"You have {remaining_days} days, {remaining_weeks} weeks, and {remaining_months} months left to live.")