# Make a BlackJack game!
# Bankroll = life pool
# When bankroll hits zero you lose

from random import shuffle

cards = ['A', 'K', 'Q', 'J', 10, 9, 8, 7, 6, 5, 4, 3, 2]
myHand = []

userName = input("Hello! What's your name? ")
print(f"Hi, {userName}! Get ready to play!")
bankroll = input("Please enter the amount you want to gamble with: ")
print(f"You've entered {bankroll}")


