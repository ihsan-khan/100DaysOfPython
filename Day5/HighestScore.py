# Highest score in a list
scores = [90, 85, 78, 92, 88]
highest_score = 0
for score in scores:
    if score > highest_score:
        highest_score = score
print("The highest score is:", highest_score)