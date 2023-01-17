
"""
Write a function that computes the volume of a sphere given its radius
"""

# def vol(rad):
#     radius = (4/3)*(3.14*(rad**3))
#     print(radius)
#
# vol(2)

"""
Write a function that checks whether a
number is in a given range (inclusive of high and low)
"""

# def ran_check(num,low,high):

#     if num in range(low, high+1):
#         print(f"{num} is in the range between {low} and {high}")
#     else:
#         print(f"{num} is NOT in the range between {low} and {high}")
#
#
# ran_check(5,2,7)


# def ran_bool(num,low,high):
#     if num in range(low,high+1):
#         print("True")
#     else:
#         print("False")
#
#
# ran_bool(3,1,10)

"""
Write a Python function that accepts a string and
calculates the number of upper case letters
and lower case letters.
"""

def up_low(mystring):
    uppercount = 0
    lowercount = 0
    for word in mystring:
        if word.isupper():
            uppercount+=1
        elif word.islower():
            lowercount+=1
        else:
            print("Something went wrong...")
    print(uppercount)
    print(lowercount)


mystring = "Hello Mr. Rogers, how are you this fine evening?"
up_low(mystring)

