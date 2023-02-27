"""
BLACK JACK
"""
import random

# Deck Variables
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
         'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
          'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

# While loop controller bool
playing = True


# Card Class - Forming a card
class Card():

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"


# Deck Class - creates deck
class Deck():
    # Creating the Deck
    def __init__(self):
        # Empty deck
        self.deck = []
        # Create a deck
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.deck.append(created_card)

    # Gives ability to print the deck
    def __str__(self):
        deck_list = ''
        for card in self.deck:
            deck_list += '\n '+card.__str__()
        return "Deck Contents: " + deck_list

    # Shuffling the deck
    def shuffle_deck(self):
        random.shuffle(self.deck)

    # Deal the cards
    def deal(self):
        # one_card = self.deck.pop()
        return self.deck.pop()


# Cards in Hand Class
class InHand():

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]

    def adjust_for_ace(self):
        pass


test_deck = Deck()
test_deck.shuffle_deck()
test_player = InHand()
test_player.add_card(test_deck.deal())
test_player.add_card(test_deck.deal())
print(test_player.value)
