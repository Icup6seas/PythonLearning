# Make a BlackJack game!
# Bankroll = life pool
# When bankroll hits zero you lose

import random

cards = ['A', 'K', 'Q', 'J', 10, 9, 8, 7, 6, 5, 4, 3, 2]
myHand = []

# userName = input("Hello! What's your name? ")
# print(f"Hi, {userName}! Get ready to play!")
# bankroll = input("Please enter the amount you want to gamble with: ")
# print(f"You've entered {int(bankroll)}")

# Shuffle the deck of cards and select 2 cards to be added to the myHand list
random.shuffle(cards)
# print(cards)

# Append the first 2 cards to myHand List after a shuffle of cards
inMyHand = 0
if inMyHand < 2:
    myHand.append(cards[0])
    myHand.append(cards[1])
else:
    print("You already have 2 cards")
print(myHand)

