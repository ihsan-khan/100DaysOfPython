# write a program that calculates the average age of a group of people
student_ages = input("Enter the ages of the students separated by spaces: ").split()
total_age = 0
count = 0
for age in student_ages:
    total_age += int(age)
    count += 1
average_age = total_age / count
print("The average age of the group is:", average_age)