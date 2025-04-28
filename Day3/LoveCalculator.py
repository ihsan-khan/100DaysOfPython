# Love calculator
name1 = input("What is your name? ")
name2 = input("What is their name? ")

# Combine names and convert to lowercase
combined_names = name1 + name2
combined_names = combined_names.lower()

# Count occurrences of letters in "true love"
true_count = 0
love_count = 0

true_count += combined_names.count("t")
true_count += combined_names.count("r")
true_count += combined_names.count("u")
true_count += combined_names.count("e")

love_count += combined_names.count("l")
love_count += combined_names.count("o")
love_count += combined_names.count("v")
love_count += combined_names.count("e")

# Combine counts into a score
score = str(true_count) + str(love_count)
# Convert score to an integer
score = int(score)
# Check score and print result
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")