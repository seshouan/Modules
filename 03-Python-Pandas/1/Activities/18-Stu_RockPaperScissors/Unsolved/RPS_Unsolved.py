# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Possible result combiations
possibilities = {
    "r,r": "Tied",
    "r,p": "Lost",
    "r,s": "Won",
    "p,r": "Won",
    "p,p": "Tied",
    "p,s": "Lost",
    "s,r": "Lost",
    "s,p": "Won",
    "s,s": "Tied",
}

# Run Conditionals
print(possibilities[user_choice+","+computer_choice])
