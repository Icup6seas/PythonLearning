# Use for, .split(), and if to create a
# Statement that will print out words
# that start with 's':
st = 'Sam Print only the words that start with s in this sentence'
for word in st.split():
    if word[0].lower() == 's':
        print(word)
print('\n')

# Use range() to print all the even numbers from 0 to 10.
rangeNum = range(0,11)
for num in rangeNum:
    if num%2==0:
        print(num)
print('\n')

# Use a List Comprehension to create a list of all numbers between 1 and 50
# that are divisible by 3.
divisibleByThree = [num for num in range(1,51) if num%3==0]
print(divisibleByThree)
print('\n')

# Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
print(st)
for word in st.split():
    if len(word)%2 == 0:
        print(word + " is EVEN")
print('\n')

# Write a program that prints the integers from 1 to 100.
# But for multiples of three print "Fizz" instead of the number,
# and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

rangeList = range(1,101)
for num in rangeList:
    if num%3==0 and num%5==0:
        print(f"{num} is Divisible by both 3 and 5, evenly - FizzBuzz")
    elif num%3==0:
        print(f"{num} is Divisible by 3, evenly - Fizz")
    elif num%5==0:
        print(f"{num} is Divisible by 5, evenly - Buzz")
    else:
        print(num)
print('\n')


# Use List Comprehension to create a list of the first letters
# of every word in the string below:
st = 'Create a list of the first letters of every word in this string'
listComp = [word[0] for word in st.split()]
print(listComp)

