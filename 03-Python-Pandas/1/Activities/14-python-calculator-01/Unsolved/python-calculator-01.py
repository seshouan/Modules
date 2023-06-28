# Define a function `calculate` that takes in two numbers and adds, subtracts, multiplies, or divides the two numbers.
def calculate(num1,num2):

    # Create a variable `result` and set it to 0.
    result = 0

    # Prompt the user "What do you want to do: Add, Subtract, Multiply or Divide?" and assign the answer to a variable `choice`.
    choice = input("What do you want to do: Add, Subtract, Multiply or Divide?")

    # Create an if-else statement to perform the proper calculation with the two parameters based on the user's `choice`.
    if choice.lower() == "add":
        result = num1+num2
    elif choice.lower() == "subtract":
        result = num1-num2
    elif choice.lower() == "multiply":
        result = num1*num2
    elif choice.lower() == "divide":
        result = num1/num2
    else:
        result = "You didn't enter a valid operation"

    # Return the calculated `result` variable.
    return result

# Call the `calculate` function and print the results.
print(calculate(23, 8))
