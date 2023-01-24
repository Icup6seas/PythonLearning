import os

"""
Tic,Tac,Toe
"""


# Splash screen to see if the user wants to play or not
def welcome_screen():
    result = ''
    quit_game = False
    within_range = False
    acceptable_result_range_list = [1, 2]

    # Title
    print("TIC - TAC - TOE")

    # Validation
    while quit_game == False:
        while result.isdigit() == False or within_range == False:
            result = input("Enter 1 to START or ANY OTHER NUMBER to Quit: ")
            # Check if digit
            if result.isdigit() == False:
                # clear()
                print("Invalid Entry, please try again")
            # Range Check
            elif result.isdigit() == True and int(result) in acceptable_result_range_list:
                if int(result) == 1:
                    # Check for option 1
                    # clear()
                    within_range = True
                    display()
                elif int(result) == 2:
                    # clear()
                    print("Thanks for playing!")
                    quit_game = True
                    quit()
            else:
                print("Invalid Entry, please try again")


# Clear display
def clear():
    os.system('cls')


# Displays the board
def display():
    row1 = [' ', ' ', ' ']
    row2 = [' ', ' ', ' ']
    row3 = [' ', ' ', ' ']
    print(row1)
    print(row2)
    print(row3)

    user_input()


# Gets the users input
# Checks validation of input
# Returns input
def user_input():
    # Variables
    row = ''
    column = ''
    acceptable_range = range(1, 4)
    within_range_row = False
    within_range_column = False

    # Two conditions to check for ROW
    # TODO Maybe have to reconfigure these while loops into nested while loops...
    while row.isdigit() == False or within_range_row == False:
        row = input("Please enter a ROW number (1-3): ")
        # Digit check
        if row.isdigit() == False:
            print("Sorry, that's not a digit!")
        # Range check
        elif row.isdigit() == True:
            if int(row) in acceptable_range:
                within_range_row = True
            else:
                print("Sorry, that's not within 1-4")

    # Two conditions to check for COLUMN
    while column.isdigit() == False or within_range_column == False:
        column = input("Please enter a COLUMN number (1-3): ")
        # Digit Check - Is this a digit?
        if column.isdigit() == False:
            print("Sorry, that's not a digit")
        # Range Check - Is this Digit within Range?
        if column.isdigit() == True:
            if int(column) in acceptable_range:
                within_range_column = True
            else:
                print("Sorry, that's not within 1-3")
    row_choice = int(row)
    column_choice = int(column)
    return row_choice, column_choice


# Function to change input into correct array index, in prep for replace_choice()
def translate_user_choice(user_choice):
    pass
    # user_choice = list(user_input() + 1)
    # user_choice_translated = user_choice+1
    # print(user_choice_translated + ' ' + 'Translated!')
    # return user_choice_translated + ' ' + 'Translated!'


# Function to modify board with user input from user_input()
def replace_choice():
    pass


# Check to see if player won
def check_win():
    pass


def main_game():
    welcome_screen()
    print("After the user input function")


main_game()
