# Random password generator
# This script generates a random password based on user-defined criteria.
import random

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
          'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
          'u', 'v', 'w', 'x', 'y', 'z']
characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
             '-', '_', '=', '+', '{', '}', '[', ']', '|', ':',
             ';', '"', "'", '<', '>', ',', '.', '?', '/']

# enter of letters, numbers and characters in password
password_length = int(input("Enter the length of the password: "))
num_letters = int(input("Enter the number of letters in the password: "))
num_numbers = int(input("Enter the number of numbers in the password: "))
num_characters = int(input("Enter the number of characters in the password: "))

# generate password
password = []
for i in range(num_letters):
    password.append(random.choice(letters))
for i in range(num_numbers):
    password.append(random.choice(numbers))
for i in range(num_characters):
    password.append(random.choice(characters))

for i in range(password_length):
    print(random.choice(password), end="")



