

# Guessing Game Challenge

randomNum = range(1,100)

print("\t\t\t\t\t\tGAME RULES")
print("*****************************************************")
print("1. If a player guess is < 1 or > 100, say 'OUT OF BOUNDS'")
print("2. On a player's turn, if their guess is")
print("\t- within 10 of the number, return 'WARM!'")
print("\t- further than 10 away from the number, return 'COLD!'")
print("3. On all subsequent turns, if a guess is")
print("\t- closer to the number than the previous guess return 'WARMER!'")
print("\t- farther from the number than the previous guess, return 'COLDER!'")
print("4. When the player's guess equals the number,")
print("   tell them they've guessed correctly and how many guesses it took!")

