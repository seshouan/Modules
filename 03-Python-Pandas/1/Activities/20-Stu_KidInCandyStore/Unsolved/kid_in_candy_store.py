# The list of candies to print to the screen
candyList = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish",
             "Skittles", "Hershey Bar", "Starbursts", "M&Ms"]

# The amount of candy the user will be allowed to choose
# allowance = 5

# The list used to store all of the candies selected inside of
candyCart = []

# Print out options
# for i in range(len(candyList)):
#     print("[" + str(i) + "] " + candyList[i])
for candy in candyList:
    print(f"[{candyList.index(candy)}] {candy}")

# Loop through the allowable number of items
continue_shopping = True
while continue_shopping:
    selection = input("What item would you like? Please enter the number (x to exit)")
    # check whether it's time to leave the shop
    if selection.lower() == "x": continue_shopping = False
    else: candyCart.append(candyList[int(selection)])

# Print out the items in the cart
for purchase in candyCart:
    print(purchase)
