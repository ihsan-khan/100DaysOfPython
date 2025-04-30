# sum of even numbers from 1 to 100
sum = 0
for i in range(1, 101):
    if i % 2 == 0:
        sum += i
print("The sum of even numbers from 1 to 100 is:", sum)

total = 0
for i in range(1, 101, 2):
    total += i
print("The sum of odd numbers from 1 to 100 is:", sum)
