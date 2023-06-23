# Define a function "warble" that takes in a string as an argument, adds " arglebargle" to the end of it, and returns the result.
def warble(entry):
    return entry+" arglebargle"

# Print the result of calling your "warble" function with the argument "hello".
warble("hello")

# Define a function "wibble" that takes a string as an argument, prints the argument, prepends "wibbly " to the argument, and returns the result
def wibble(entry):
    return "wibbly "+entry

# Print the result of calling your "wibble" function with the argument "bibbly"
wibble("bibbly")

# Define a function "print_sum" that takes in two numbers as arguments and prints the sum of those two numbers.
def print_sum(num1, num2):
    print(num1+num2)

# Define a function "return_sum" that takes in two numbers as arguments and returns the sum of those two numbers
def return_sum(num1, num2):
    return num1+num2

# Using either "return_sum" and no mathematical operators, define a function "triple_sum" that takes in 3 arguments and returns the sum of those 3 numbers.
def triple_sum(num1, num2, num3):
    return return_sum(return_sum(num1,num2),num3)
# print(triple_sum(1,3,5))

# Define a function "dance_party" that takes in a string as an argument, that prints "dance!", updates the string from calling "wibble" function with that argument, updates the string from calling "warble" function with that argument, returns the updated string
def dance_party(entry):
    print("dance!")
    entry = wibble(entry)
    entry = warble(entry)
    return entry

# Print the result of calling your "dance_party" function with your name as the argument
print(dance_party("Session Mwamufiya"))
