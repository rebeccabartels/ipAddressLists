# The list of candies to print to the screen
itemList = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit",
             "Swedish Fish", "Skittles", "Hershey Bar", "Skittles", "Starbursts", "M&Ms"]

# The amount of item the user will be allowed to choose
allowance = 5

# Create an empty list to store all the candies selected
shopingCart = []

# Print all the candies to the screen and their index in brackets
for item in itemList:
    print("[" + str(itemList.index(item)) + "] " + item)

# Run through a loop which allows the user to choose which candies to take home with them!!!!
for x in range(allowance):
    selected = input("Which item would you like to bring home? ")

    # Add the item at the index chosen to the shoppingCart list, need to swtich back to int because it was merged to string before and needs to be int to go into list
    shoppingCart.append(itemList[int(selected)])

# Loop through the itemCart to print what candies were brought home
print("I brought home with me...")
for item in shoppingCart:
    print(item)
#test
