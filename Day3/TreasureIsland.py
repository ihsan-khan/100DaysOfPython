# Treasure island problem
print("Welcome to Treasure Island.You mission is to find the treasure.")
direction = input("You are at a crossroad. Where do you want to go? Type 'left' or 'right': ").lower()
if direction == "left":
    swim_or_wait = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across: ").lower()
    if swim_or_wait == "wait":
        door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose? ").lower()
        if door == "red":
            print("It's a room full of fire. Game over.")
        elif door == "yellow":
            print("You found the treasure! You win!")
        elif door == "blue":
            print("You enter a room of beasts. Game over.")
        else:
            print("You chose a door that doesn't exist. Game over.")
    else:
        print("You got attacked by an angry trout. Game over.")
else:
    print("You fell into a hole. Game over.")