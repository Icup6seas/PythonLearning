import os

"""
Tic,Tac,Toe
"""


# Splash screen to see if the user wants to play or not
def welcome_screen():
    result = ""
    within_range = False
    acceptable_result_range_list = [1, 2]

    # Title
    print("TIC - TAC - TOE")

    # Validation
    while result.isdigit() == False or within_range == False:
        result = input("Enter 1 to Start or 2 to Quit: ")
        # Check if digit
        if result.isdigit() == False:
            print("Invalid Entry, please try again: ")
        # Range Check
        if result.isdigit() == True:
            if int(result) in acceptable_result_range_list:
                within_range = True
                # Check for option 1
                if int(result) == 1:
                    # clear()
                    display()
                    user_input()
                else:
                    # clear()
                    print("Thanks for playing!")
            else:
                print("Invalid Entry, please try again: ")


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


# Gets the users input
# Checks validation of input
# Returns input
def user_input():
    # Variables
    row = ""
    column = ""
    acceptable_range = range(1, 4)
    within_range_row = False
    within_range_column = False

    # Two conditions to check for ROW
    while row.isdigit() == False or within_range_row == False:
        row = input("Please enter a ROW number (1-3): ")
        # Digit check
        if row.isdigit() == False:
            print("Sorry, that's not a digit!")
        # Range check
        if row.isdigit() == True:
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
    match user_choice:
        case 1:
            print(0)
            return 0
        case 2:
            print(1)
            return 1
        case 3:
            print(2)
            return 2
        case _:
            print("Something went wrong!")
            return "Something went wrong!"


# Function to modify board with user input from user_input()
def replace_choice():
    pass


# Check to see if player won
def check_win():
    pass


def main_game():
    welcome_screen()
    user_choice = user_input()
    translate_user_choice(user_choice)
    user_choice_translated = translate_user_choice(user_choice)



main_game()
