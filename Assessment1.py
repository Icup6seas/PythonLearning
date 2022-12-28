# First assessment of the 2022 Complete Python Bootcamp From Zero to Hero in Python

s = 'hello'
# Print out 'e' using indexing

print(s[1])

s ='hello'
# Reverse the string using slicing
reversing = s[::-1]
print(reversing)




s ='hello'
# Print out the 'o'

# Method 1:
print(s[4])


# Method 2:
print(s[-1])

# Build this list [0,0,0] two separate ways
# Method 1:
methodList_1 = [0, 0, 0]
print(methodList_1)


# Method 2:
methodList_2 = [0]*3
print(methodList_2)

# Replace hello with goodbye
list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'
print(list3)


# Sort the list below
list4 = [5,3,4,6,1]
print(list4)
list4.sort()
print(list4)

# OR
sortedListSecondMethod = sorted(list4)
print(sortedListSecondMethod)


# Using keys and indexing, grab the 'hello' from the following dictionaries:

d = {'simple_key':'hello'}
# Grab 'hello'

print(d['simple_key'])


d = {'k1':{'k2':'hello'}}
# Grab 'hello'

print(d['k1']['k2'])


# Getting a little tricker
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
#Grab hello

print(d['k1'][0]['nest_key'][1][0])

# This will be hard and annoying!
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
# Grab hello

print(d['k1'][2]['k2'][1]['tough'][2][0])



# Use a set to find the unique values of the list below:
list5 = [1,2,2,33,4,4,11,22,3,3,2]
setList = set(list5)

print(setList)


x = (3.0 == 3)
print(x)

y = ((4**0.5) != 2)
print(y)


# Final Question: What is the boolean output of the cell block below?

# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# True or False?
result = l_one[2][0] >= l_two[2]['k1']

print(result)
