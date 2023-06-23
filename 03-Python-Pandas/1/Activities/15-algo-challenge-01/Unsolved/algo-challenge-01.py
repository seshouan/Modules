# Import the `random` library.
import random

# Answer each question with the correct coding solution.

# QUESTION 1: Create a function called `number_guess` that takes in an integer as an argument.
# If the number is 42, print(true). If it isn't 42, print(false)
def number_guess(guess):
    return True if guess == 42 else False

# This code is to help you test your function
# print(number_guess(42))

# QUESTION 2: Write a function that takes in a list of numbers. the function should print the smallest number in the given list
def min_number(entry):
    return min(entry)

# This code is to help you test your function
# print(min_number([3,6,34,23,1,-3]))

# QUESTION 3: Write a function which takes in a list of strings. The function should print the shortest string in the list.
def min_string(entry):
    min_length = entry[0]
    for string in entry:
        if len(string) < len(min_length):
            min_length = string
    return min_length

# This code is to help you test your function
# print(min_string(["short","long list","sh"]))

#QUESTION 4: Write a function that takes in three arguments: a high value, a low value and a list of numbers.
# The function should print a new list of numbers where the elements are greater than the low value and less than the high value
def pincher(high, low, data):
    result = []
    for num in data:
        if num > low and num < high:
            result.append(num)
    return result

# This code is to help you test your function
print(f"Pinched list: {pincher(50, 23, [34, 25, 23, 8, 14, 199, 52, 25])}")
