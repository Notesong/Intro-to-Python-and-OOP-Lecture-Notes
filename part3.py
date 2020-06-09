# OOP - Object Oriented Programming

# Classes
# definition of an object
# holds data about the instaniated object
# contains attributes and methods

# instance of a class

from category import Category


class Store:
    # attributes
    # name
    # categories (departments)

    # constructor - the function that runs every time you create a new instance
    # self refers to the current instance of the class (in JS the word is "this")
    def __init__(self, name, categories):
        self.name = name
        self.categories = categories

    def __str__(self):
        # return a string representing the stored
        output = f"Welcome to {self.name}!"
        i = 1
        for category in self.categories:
            output += f"\n {i}. {str(category.name)}"
            i += 1
        return output

    def __repr__(self):
        # also a string representation
        return f"self.name = {self.name} ; self.categories = {self.categories}"


running_category = Category("Running", "All your running needs", [])
baseball_category = Category("Baseball", "Blue Jays Fans only", [])
basketball_category = Category("Basketball", "Indoor and outdoor products", [])

sports_store = Store("Gander Mountain", [
                     running_category, baseball_category, basketball_category])
# products_store = Store("Trader Joe's", ["Dairy", "Meat", "Bread", "Produce"])

# print(sports_store)
# print(products_store)
# print(repr(sports_store))
# print(repr(products_store))


# REPL <= Read Evaluate Print Loop

choice = -1
print(sports_store)
print("Type q to quit")

while True:
    # Read
    choice = input("Choose a category (#): ")
    try:
        # Evaluate
        if (choice == 'q'):
            break
        choice = int(choice) - 1
        if choice >= 0 and choice < len(sports_store.categories):
            chosen_category = sports_store.categories[choice]
            # Print
            print(chosen_category)
        else:
            print("The number is out of range")

        # Loop
    except ValueError:
        print("Please enter a valid number.")
