# LESSER OF TWO EVENS: Write a function that returns the lesser of two
# given numbers if both numbers are even,
# but returns the greater if one or both numbers are odd

# def lesseroftwoevens(num1, num2):
#     if num1%2==0 and num2%2==0:
#         # return min(num1,num2)
#         print(min(num1,num2))
#     else:
#         # return max(num1,num2)
#         print(max(num1,num2))
#
#
# lesseroftwoevens(2,5)


# ANIMAL CRACKERS: Write a function takes a two-word string
# and returns True if both words begin with same letter

# def animal_crackers(string):
#     stringlist = string.lower().split()
#     print(stringlist)
#     # return stringlist[0][0] == stringlist[1][0]
#     print(stringlist[0][0] == stringlist[1][0])
#
#
# animal_crackers('Levelheaded Llama')
# animal_crackers('Crazy Kangaroo')


# MAKES TWENTY: Given two integers,
# return True if the sum of the integers is 20 or if one of the integers is 20.
# If not, return False


# def makes_twenty(num1, num2):
#     if num1 + num2 == 20:
#         # return True
#         print("True")
#     elif num1 == 20 or num2 == 20:
#         # return True
#         print("True")
#     else:
#         # return False
#         print("False")
#
#
# def makes_twenty(n1,n2):
#     return (n1+n2)==20 or n1==20 or n2==20
#
#
# makes_twenty(6,15)


# OLD MACDONALD: Write a function that capitalizes the first
# and fourth letters of a name


# def old_macdonald(name):
#     if len(name) < 4:
#         print("Your name is too short!")
#     else:
#         # return name[:3].capitalize() + name[3:].capitalize()
#         # this print statement is saying to take the
#         # first position for the first 4 indexes (not counting the 4th)
#         # concatenate the capitalized, 4th position letter
#         print(name[:3].capitalize() + name[3:].capitalize())
#
#
# old_macdonald('macdonald')


# MASTER YODA: Given a sentence, return a sentence with the words reversed
# def masteryoda(string):
#     mystring = ' '.join(string.split()[::-1])
#     # return mystring
#     print(mystring)
#
# masteryoda('May the Force be with you')

# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200

# def almost_there(n):
#     if (abs(100-n)<=10) or (abs(200-n)<=10):
#         # return True
#         print('True')
#     else:
#         # return False
#         print("False")
#
# def almost_there(n):
#     return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))
#
#
# almost_there(104)
# almost_there(150)
# almost_there(209)


# FIND 33:
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

# def has_33(numbers):
#     for number in range(0,len(numbers)-1):
#         if numbers[number]==3 and numbers[number+1]==3:
#             # return True
#             print('True')
#         else:
#             # return False
#             print("False")
#
# has_33([1, 3, 3])
# has_33([1, 3, 1, 3])
# has_33([3, 1, 3])


# PAPER DOLL: Given a string, return a string where for
# every character in the original there are three characters

# def paper_doll(string):
#     string_list = ''
#     for letter in string:
#         string_list += letter*3
#     print(string_list)
#
#
# # paper_doll('Hello')
# paper_doll('Mississippi')

# BLACKJACK: Given three integers between 1 and 11, if their sum is
# less than or equal to 21, return their sum.
# If their sum exceeds 21 and there's an eleven,
# reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21,
# return 'BUST'

# def blackjack(a,b,c):
#     total = sum((a,b,c))
#     if total <= 21:
#         # return total
#         print(total)
#     elif total > 21 and a == 11 or b == 11 or c == 11:
#     # elif total > 21 and 11 in (a,b,c):
#         total = total-10
#         # return total
#         print(total)
#     elif total > 21:
#         # return "BUST"
#         print("BUST")
#     else:
#         print("Something's wrong!")
#
# # blackjack(5,6,7)
# # blackjack(9,9,9)
# blackjack(9,9,11)


# SUMMER OF '69: Return the sum of the numbers in the array,
# except ignore sections of numbers starting with a 6 and extending
# to the next 9 (every 6 will be followed by at least one 9).
# Return 0 for no numbers.

# def summer_69(arr):
#     total = 0
#     add = True
#     for number in arr:
#         while add:
#             if number != 6:
#                 total += number
#                 break
#             else:
#                 add = False
#         while not add:
#             if number != 9:
#                 break
#             else:
#                 add = True
#                 break
#     print(total)
#
#
# summer_69([1,3,5,6,9,10])
# summer_69([4,5,6,7,8,9])
# summer_69([2,1,6,9,11])


# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order

# def spy_game(numbers):
#     code = [0, 0, 7, 'x']
#
#     for num in numbers:
#         if num == code[0]:
#             code.pop(0)  # code.remove(num) also works
#
#     # return len(code) == 1
#     print(len(code) == 1)


# spy_game([1,2,4,0,0,7,5])
# spy_game([1,0,2,4,0,5,7])
# spy_game([1,7,2,0,4,5,0])


# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to
# and including a given number

# def count_primes(num):
#     primes = [2]
#     x = 3
#     if num < 2:
#         return 0
#     while x <= num:
#         for y in primes:
#             if x % y == 0:
#                 x += 2
#                 break
#         else:
#             primes.append(x)
#             x += 2
#     print(primes)
#     return len(primes)
#
#
# count_primes(100)
