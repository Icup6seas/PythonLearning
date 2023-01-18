import string
"""
Write a function that computes the volume of a sphere given its radius
"""


def vol(rad):
    radius = (4/3)*(3.14*(rad**3))
    print(radius)


vol(2)

"""
Write a function that checks whether a
number is in a given range (inclusive of high and low)
"""


def ran_check(num,low,high):
    if num in range(low, high+1):
        print(f"{num} is in the range between {low} and {high}")
    else:
        print(f"{num} is NOT in the range between {low} and {high}")


ran_check(5,2,7)


def ran_bool(num,low,high):
    if num in range(low,high+1):
        print("True")
    else:
        print("False")


ran_bool(3,1,10)

"""
Write a Python function that accepts a string and
calculates the number of upper case letters
and lower case letters.
"""


def up_low(mystring):
    uppercase = []
    lowercase = []
    other = []
    for letter in mystring:
        if letter.isupper():uppercase.append(letter)
        # if letter.isupper() == True:
        #     uppercase.append(letter)
        elif letter.islower():lowercase.append(letter)
        # elif letter.islower() == True:
        #     lowercase.append(letter)
        elif letter != ' ':other.append(letter)
        # elif letter != ' ':
        #     other.append(letter)
        else:
            continue

    print(f"No. of Uppercase characters: {len(uppercase)}")
    print(f"No. of Lowercase characters: {len(lowercase)}")
    print(f"No. of Other characters: {len(other)}")


mystring = "Hello Mr. Rogers, how are you this fine Tuesday?"
up_low(mystring)


"""
Write a Python function that takes a list and 
returns a new list with unique elements of the first list.
"""


def unique_list(mylist):
    print(list(set(mylist)))


mylist = [1,1,1,1,2,2,3,3,3,3,4,5]
# mylist2 = ['1','1','1','1','1','1','1','2','3','3']
unique_list(mylist)


"""
Write a Python function to multiply all the numbers in a list.
"""


def multiply(numbers):
    total = 1
    for number in numbers:
        total*=number
    print(total)


multiply([1, 2, 3, -4])


"""
Write a Python function that checks whether a word or phrase is palindrome or not.
"""


def palindrome(mypalendrome):
    if mypalendrome == mypalendrome[::-1]:
        print("True")
    else:
        print("False")


mypalendrome = 'racecar'
palindrome(mypalendrome)


"""
Write a Python function to check whether a string is pangram or not. 
(Assume the string passed in does not have any punctuation)

String module has been imported to generate the list of letters
"""


def ispangram(mypangram, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    mypangram = mypangram.replace(' ', '')
    mypangram = mypangram.lower()
    mypangram = set(mypangram)
    print(mypangram == alphaset)


mypangram = "The quick brown fox jumps over the lazy dog"
ispangram(mypangram)


