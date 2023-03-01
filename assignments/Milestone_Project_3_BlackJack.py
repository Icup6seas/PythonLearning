"""
BLACK JACK
"""
import random
from pyfiglet import Figlet


# Deck Variables
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
         'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
          'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

# # While loop controller bool
# playing = True

# Player and Dealer wins count
p_wins_count = 0
d_wins_count = 0
push_count = 0


# Card Class - Forming a card
class Card():

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"


# While loop controller bool
playing = True


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
class Hand():

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        # Incrementing Ace counter if card added was an Ace
        if card.rank == "Ace":
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


# Chips Class
class Chips():

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


# Placing bets check
def place_bet(chips):
    while True:
        try:
            # Try to take the bet
            chips.bet = int(input("Place Bet: "))
        except ValueError:
            print("Sorry, please enter an Integer")
        else:
            # If player's total chips aren't enough to cover their bet
            if chips.total < chips.bet:
                print(f"Insufficient Funds, cannot exceed ${chips.total}")
            else:
                break


# Taking a Hit
def hit(deck,hand):
    # Adding a card to your hand from the deck
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


# Player to Hit or Stand
def hit_or_stand(deck,hand):
    global playing

    while True:
        # if player hits -> hit()
        result = input("HIT or STAND - Enter 'h' or 's': ")
        if result[0].lower() == 'h':
            hit(deck,hand)
        elif result[0].lower() == 's':
            # if player stands -> set playing variable to False
            print("Player STANDS. Dealer is playing")
            playing = False
        else:
            # Validation loop
            print("Invalid input, try again")
            continue
        break


# Partial display of hands
def show_some(player,dealer):
    print("\nDealer's Hand:")
    print("<hidden>")
    print('',dealer.cards[1])
    print("\nPlayers Hand:", *player.cards, sep='\n')
    print(f"{player.value}")


# Full display of hands
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n')
    print("Dealer's Card Value = ",dealer.value)
    print("\nPlayer's Hand:", *dealer.cards, sep='\n')
    print("Player's Card Value = ",player.value)


# Player Busts
def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()


# Player Wins
def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()


# Dealer Busts
def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()


# Dealer Wins
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()


# Player and Deal Push
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")



"""
Game Logic
"""

while True:

    # Game ascii banner title using PyFiglet
    custom_fig = Figlet(font="standard")
    print(custom_fig.renderText("BLACKJACK"))

    # Create and shuffle deck
    deck = Deck()
    deck.shuffle_deck()

    # Create player hand and deal two cards
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    # Create dealer hand and deal two cards
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Assign Chips
    player_chips = Chips()

    # Player Better
    # TODO - Develop a way to continually play with your stack
    place_bet(player_chips)

    # Show cards - Dealer cards are hidden
    show_some(player_hand,dealer_hand)

    # Hit or Stand
    while playing:
        # Prompt to Hit of Stand
        hit_or_stand(deck,player_hand)

        # Show cards - Dealer cards are hidden
        show_some(player_hand,dealer_hand)

        # Hand value check
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break

    # No Bust, play dealer until Dealer reaches a card value of 17
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)
        # Show all cards
        show_all(player_hand,dealer_hand)

        # Win scenarios
        if player_hand.value > 21:
            d_wins_count += 1
            player_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > 21:
            p_wins_count += 1
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            p_wins_count += 1
            player_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            d_wins_count += 1
            dealer_wins(player_hand,dealer_hand,player_chips)
        else:
            push_count += 1
            push(player_hand,dealer_hand)

    # Chip Totals
    print(f"\nPlayer's Chip Total: {player_chips.total}")

    # Play Again?
    new_game = input("Play again? Enter 'y' or 'n': ")
    if new_game[0].lower() == 'y':
        playing = True
    else:
        custom_fig = Figlet(font="standard")
        print(custom_fig.renderText("GAME     OVER"))
        print("** GAME STATS **")
        print(f"Player Wins: {p_wins_count}")
        print(f"Dealer Wins: {d_wins_count}")
        print(f"Pushes: {push_count}")
        break
