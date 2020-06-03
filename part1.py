# print hello world
print("Hello, world!")

# declare a variable
name = "Lee"

# print name
print(name)

# string concatenation
print("hello " + name)
# `Hello ${name}`
print(f'Hello {name}')

################################################################
################################################################
# data structures
################################################################

################################################################
# Lists
#
# (array in JS)
# can mix types

p = [10, 20, 20, 0, "hey"]
print(p)
# add an element to the end of p
p.append(77)
print(p)

# lets loop over the list p, and print every element
# for eery element in P, do some sore of code
for element in p:
    print(element)

# lets print the index and the element at the indes of p
# enumerate(p) => [(0, 10), (1, 20), (2, 20), (3, 0), (4, "hey")...]
for (index, element) in enumerate(p):
    print(f'Element at {index} is {p[index]} == {element}')

################################################################
# List comprehensions
#
# another way to create a list

numbers = [0, 2, 24, 33]
# new list of squares from the numbers list
# this is the verbose way:
squares = []
for num in numbers:
    squares.append(num*num)
print(squares)

# lets use the list comprehensions way
# for each element from numbers, mutlipy by istself and add to coolder_squares
# [ function(variable) for variable in some_list ]
cooler_squares = [num*num for num in numbers]
print(cooler_squares)

# lets create a list of just even numbers
evens = [num for num in numbers if num % 2 == 0]
print(evens)

# create a new list containing only names that start with s
# also all names should be capitalized
names = ['Sarah', "george", "sam", 'bob', "sandra"]

s_names = [name.capitalize() for name in names if name[0].lower() == 's']
print(s_names)

################################################################
# Dictionaries
#
# Otherwise known as maps/hashmaps/objects
# a key -> value data structure

new_dict = {}
# create a dictionary with some keys and values

food_dict = {
    'apple': 'is a fruit',
    'carrot': 'is a vegetable'
}
print(food_dict)

# lets add a new key -> value pair
food_dict['cucumber'] = 'is a vegetable'
print(food_dict)

# acces and print a specific element in food_dict
# food_dict.apple is not allowed in python (only JS)
chosen_food = 'apple'
print(food_dict[chosen_food])

# iterate through the keys and values of a dictionary
# for  element in dict, do some code
for (key, value) in food_dict.items():
    print(f'{key} : {value}')

# how can we check if an element exists in a dictionary?
# is apple in food_dict?
print('apple' in food_dict)
print('apple' in food_dict.keys())
print('apple' in food_dict.values())
print('banana' in food_dict)

################################################################
# Tuple
#
# they are immutable

tup = (1, 2, 3, 4)
for item in tup:
    print(item)

# access a partciular element
print(tup[1])

# you cannot modify tup in any way
# tup[1] = 'new_value'

################################################################
# Sets
#
# sets are UNORDERED
# dictionaries without values
# sets are fast for finding elements in the set - arrays are not fast

fruit = {'cucumber', 'apple', 'banana'}

for item in fruit:
    print(item)

if 'cucumber' in fruit:
    print("I don't think a cucumber is a fruit")
