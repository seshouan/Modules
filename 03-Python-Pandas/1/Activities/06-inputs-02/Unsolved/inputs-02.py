# Declare a variable of `name` with an input and a string of "Welcome to the Boba Shop! What is your name?".
name = input("Welcome to the Boba Shop! What is your name? ")

# Check if `name` is not an empty string or equal to `None`.
if name != "" and name != None:
    # If so, write a print with a string of "Hello" concatenated with the variable `name`.
    print(f"Hello {name}")

    # Then, declare a variable of `beverage` with an input and a string of "What kind of boba drink would you like?".
    beverage = input("What kind of boba drink would you like?")

    # Then, Declare a variable of `sweetness` with an input and a string of "How sweet do you want your drink: 0, 50, 100, or 200?".
    sweetness = input("How sweet do you want your drink: 0, 50, 100, or 200?")

    # If `sweetness` equals 50 print "half sweetened".
    if sweetness == "50":
        print("half sweetened")
    # Else if `sweetness` 100 print "normal sweet".
    elif sweetness == "100":
        print("normal sweetened")
    # Else if `sweetness` 200 print "super sweet".
    elif sweetness == "200":
        print("super sweetened")
    # Else print with a string of "non-sweet".
    else:
        print("non-sweet")

    # Then print the string of "Your order of " concatenated with the variable `beverage`, concatenated with " boba with a sweet level of ", concatenated with the variable `sweetness`
    print(f"Your order of {beverage} boba with a sweet level of {sweetness}")
# Else, print the string of "You didn't give us your name! Goodbye"
else:
    print("You didn't give us your name! Goodbye")

