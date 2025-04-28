# Randomization program to simulate a coin flip
import random   

print("Welcome to the Coin Flip Simulator!")
user_input = input("Do you want to flip a coin? Type 'yes' or 'no': ").lower()
if user_input == "yes":
    flip = random.randint(0, 1)  # Generate a random number between 0 and 1
    if flip == 1:
        print("Heads")
    else:
        print("Tails") 
else:
    print("Thank you for using the Coin Flip Simulator!")
