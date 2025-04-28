# Treasure map
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"] 

treasure_map = [row1, row2, row3]
print("Welcome to Treasure Map!")
print("The map is as follows:")
print(f"{row1}\n{row2}\n{row3}")
print("Where do you want to put the treasure?")
position = input("Enter the row and column number separated by a comma (e.g. 1,2): ")
row = int(position[0]) - 1
column = int(position[2]) - 1   
treasure_map[row][column] = "X" 
print("The map with the treasure is as follows:")
print(f"{row1}\n{row2}\n{row3}")
print("Congratulations! You have found the treasure!")