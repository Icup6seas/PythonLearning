
import random

randomNum = random.randint(1,100)
print("\t\tGUESSING GAME")
print("\t#####################")
print("1. If a player's guess is less than 1 or greater than 100, say 'OUT OF BOUNDS'")
print("2. On a player's first turn, if their guess is")
print(" - within 10 of the number, return 'WARM!'")
print(" - further than 10 away from the number, return 'COLD!'")
print("3. On all subsequent turns, if a guess is")
print(" - closer to the number than the previous guess return 'WARMER!'")
print(" - farther from the number than the previous guess, return 'COLDER!'")
print("4. When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!")

storedGuesses = [0]
while True:
    userGuess = int(input("Enter a guess: "))
    if userGuess < 1 or userGuess > 100:
        print("OUT OF BOUNDS: ")
        continue

    if userGuess == randomNum:
        print(f"Well done! You've guessed the number in {len(storedGuesses)} guesses!")
        break
    storedGuesses.append(userGuess)

    if storedGuesses[-2]:
        if abs(randomNum-userGuess) < abs(randomNum-storedGuesses[-2]):
            print('WARMER!')
        else:
            print('COLDER!')
    else:
        if abs(randomNum-userGuess) <= 10:
            print('Warm')
        else:
            print('Cold')