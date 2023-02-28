"""
WAR Game!
"""
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
         'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
          'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


class Card():

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck():

    def __init__(self):
        # Create empty list for all cards
        self.all_cards = []

        # Creating the cards and adding them to the all_cards list
        for suit in suits:
            for rank in ranks:
                # Create a Card Object
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


class Player():

    def __init__(self,name):
        self.name = name
        self.all_cards = []

    def __str__(self):
        return f"{self.name} has {len(self.all_cards)} cards"

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self,new_cards):
        # Adding a list of multiple cards to players hand
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            # Adding only one card to players hand
            self.all_cards.append(new_cards)


"""
Game Setup
"""

# Player setup
player_one = Player("One")
player_two = Player("Two")

# Deck setup
new_deck = Deck()
new_deck.shuffle()

# Dealing the FULL deck to both players
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())


game_on = True
round_num = 0

while game_on:
    round_num += 1
    print(f"Round {round_num}")

    # Check if someone has no cards
    if len(player_one.all_cards) == 0:
        print("Player ONE is out of cards, Player TWO is the winner!")
        game_on = False
        break
    elif len(player_two.all_cards) == 0:
        print("Player TWO is out of cards, Player ONE is the winner!")
        game_on = False
        break

    # Start a new round
    # Player_one_cards are cards ON THE TABLE from player one
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    # while playing logic
    at_war = True
    # war_count = 0

    while at_war:
        # Player One beats Player Two
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False
        # Player One beats Player Two
        elif player_two_cards[-1].value > player_one_cards[-1].value:
            player_two.add_cards(player_two_cards)
            player_two.add_cards(player_one_cards)
            at_war = False
        else:
            # War has started!
            print("WAR")
            # war_count += 1
            # print(war_count)
            # Check players card counts
            # makes sure players have enough cards to play with
            # Player One
            if len(player_one.all_cards) < 3:
                print("Player One cannot fund the War")
                print("Player Two WINS!")
                game_on = False
                break
            # Player Two
            elif len(player_two.all_cards) < 3:
                print("Player Two cannot fund the War")
                print("Player One WINS!")
                game_on = False
                break
            # Both players have at least the minimum allowed number of cards
            else:
                for num in range(3):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())