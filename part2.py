# define a doubling function that passes args by value
# a normal variable is passed value
def double(x):
    return x * 2


y = double(12)
print(y)


# define a doubing function for a list of variables
# a list is passed by reference
def mult2_list(l):
    for i in range(len(l)):
        l[i] *= 2


some_list = [1, 2, 3, 4]
print(some_list)
mult2_list(some_list)
print(some_list)


# U.P.E.R.
# 4 step way to problem solve

# Understand:
#   ask a ton of questions
#   figure out constraints like speed, time, money, design
#   determine inputs and outputs, edge cases, what input will break app

# Planning
#   can you describe an MVP or brute force approach
#   find data structure or algorithims that can improve the code
#   use pseudocode

# Execute
#   turn pseudocode into real code, etc.

# Repeat or Reflect or Refactor or Refine
#   go back to different stages to clean code or debug it
