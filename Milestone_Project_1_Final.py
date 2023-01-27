"""
TIC TAC TOE
"""
import random


# Display board with indexed positions
def display_board(board):
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print(' '+'---'+'---'+'---')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(' '+'---'+'---'+'---')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

# Get user input to assign markers to players
def player_input():
    player_marker = ''

    # if not X or O, keep asking
    while not (player_marker == 'X' or player_marker == 'O'):
        player_marker = input("Player 1: Please type which marker you'd like to be - 'X' or 'O': ").upper()
    if player_marker == 'X':
        return ('X','O')
    else:
        return ('O','X')


# Takes board object, marker, position, and assigns this to the board
def place_marker(board, player_marker, position):
    board[position] = player_marker


# Win Check
def win_check(board,player_marker):
    return ((board[7] == player_marker and board[8] == player_marker and board[9] == player_marker) or
            (board[4] == player_marker and board[5] == player_marker and board[6] == player_marker) or
            (board[1] == player_marker and board[2] == player_marker and board[3] == player_marker) or
            (board[7] == player_marker and board[4] == player_marker and board[1] == player_marker) or
            (board[8] == player_marker and board[5] == player_marker and board[2] == player_marker) or
            (board[9] == player_marker and board[6] == player_marker and board[3] == player_marker) or
            (board[1] == player_marker and board[5] == player_marker and board[9] == player_marker) or
            (board[3] == player_marker and board[5] == player_marker and board[7] == player_marker)
            )


# Randomly decide which player goes first
def random_first_player():
    if random.randint(0,1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


# Is the space available?
def space_free_check(board,position):
    return board[position] == ' '


# Is the board full? AKA - Stalemate
def board_full_check(board):
    for space in range(1,10):
        if space_free_check(board,space):
            return False
    return True


# Next position
def player_choice(board):
    position = 0
    board_list = [1,2,3,4,5,6,7,8,9]
    while position not in board_list or not space_free_check(board,position):
        position = int(input("Choose your next position: "))
    return position


# Play again?
def replay():
    return input("Would you like to play again? Enter Y or N: ").upper().startswith('Y')


# The game logic
while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = random_first_player()
    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Enter Y or N.')

    if play_game.upper()[0] == 'Y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            print("Player 1's turn!!!")
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if board_full_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            print("Player 2's turn!!!")
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if board_full_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break