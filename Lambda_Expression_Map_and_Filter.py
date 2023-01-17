

# Lambda Expression Map and Filter
# Map applies the given function to each element in a list

# def square(num):
#     return num**2
#
#
# my_nums = [1,2,3,4,5]
#
# for item in map(square, my_nums):
#     print(item)
#
#
# def splicer(mystring):
#     if len(mystring)%2 == 0:
#         return "Even"
#     else:
#         # this would return odd numbered strings
#         return mystring[0]
#
# names = ['Chris','Nora']
#
# print(list(map(splicer,names)))


# Filter by a function that returns either True or False
# Filters based off the given functions condition

# def check_even(num):
#     return num%2 == 0
#
# mynums = [1,2,3,4,5,6]
#
# print(list(filter(check_even,mynums)))

# This is the LAMBDA expression, this replaces lines 31-36
# print(list(filter(lambda num:num%2==0, mynums)))

# First character of a string
# mystring = ['Chris','Nora']
#
# print(list(map(lambda fchar:fchar[0],mystring)))








