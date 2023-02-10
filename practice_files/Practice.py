
# if, elif, else statements
# zoo = ['Tiger', 'Bear', 'Wolf', 'Kitty']
#
# for animal in zoo:
#     if animal == 'Bear':
#         print(f"Shit! It's a {animal}!")
#     elif animal == 'Tiger':
#         print(f"{animal}s - AKA - Danger Kittens")
#     elif animal == 'Wolf':
#         print(f"{animal}'s are related to Geralt?!")
#     else:
#         print(f"{animal}s are miniature Tigers")
#
#
# # For loops - Tuple unpacking
# myList = [(1,2), (3,4), (5,6), (7,8)]
# for a,b in myList:
#     print(a)
#     print(b)
#
# myList2 = [(1,2,3),(5,'Six',7),(8,'Nine',10)]
# for a,b,c in myList2:
#     print(a)
#     print(b)
#     print(c)
#
# # Iterate through a dictionary - .items() is the key to
# myDictionary = {'k1':1, 'k2':2, 'k3':3, 'k4':4, 'k5':5}
# for key, value in myDictionary.items():
#     print(value)

# While loops
x = 0
while x < 5:
    print("Nora!")
    x += 1

# Operators

# Break, Continue, Pass
x = 0
while x < 5:
    print("Nora - Break!")
    x += 1
    break

x = 0
while x == 5:
    print("Equals 5?!?!")
    x += 1
    # continue
else:
    print("Nora - Continue!")

# xs = " "
# for x in xs:
#     pass

# enumerate
myEnumList = [1,2,3,"Four"]
# for index,number in enumerate(myEnumList):
#     print(index)
#     print(number)
for item in enumerate(myEnumList):
    print(item)

# zip
myZipList1 = [1,2,3,"Four"]
myZipList2 = [1,'2','Three',4]
# for index,number in zip(myZipList1, myZipList2):
#     print(index)
#     print(number)
for item in zip(myZipList1, myZipList2):
    print(item)

# in
x = [1, '2', 'three']
y = 'three' in x
print(y)

x = [1, '2', 'three']
y = '1' in x
print(y)

# min
z = [1,10,3]
maximum = max(z)
print(maximum)

# max
z = [1,10,3]
minimum = min(z)
print(minimum)

# random
import random
cards = ['A', 'K', 'Q', 'J', 10, 9, 8, 7, 6, 5, 4, 3, 2]
random.shuffle(cards)
print(cards)


# input - user input
# result = input("Please select a card ")
# print(f"You've selected {result}")


# Create a list from another iterable, but in a more concise formate

mylist1 = [num for num in range(0,11)]
print(mylist1)

mylist2 = [num for num in range(0,11) if num%2 == 0]
print(mylist2)

mylist3 = [num**2 for num in range(0,11)]
print(mylist3)

mylist4 = [num**2 for num in range(0,11) if num%2==0]
print(mylist4)

# List Comprehension practice
# Calculating Fahrenheit from Celsius for each temperature in a list
# This also appends the results to another list
celsius = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
fahrenheit = [((9/5)*temp +32) for temp in celsius]
print(fahrenheit)

# The longer example of temperature conversions
f = []
for temp in celsius:
    f.append((9/5)*temp +32)
print(f)
