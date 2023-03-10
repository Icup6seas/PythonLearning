import os

"""
Tic,Tac,Toe
"""


# Clear display
def clear():
    # os.system('cls')
    print('\n' * 100)


# Displays the board
def display():
    row1 = [' ', ' ', ' ']
    row2 = [' ', ' ', ' ']
    row3 = [' ', ' ', ' ']
    print(row1)
    print(row2)
    print(row3)
    return


# Gets the users input
# Checks validation of input
# Returns input
def user_input_row():
    # Variables
    row = ''
    acceptable_range = range(1, 4)
    within_range_row = False

    # Two conditions to check for ROW and COLUMN
    while row.isdigit() == False or within_range_row == False:
        row = input("Please enter a ROW number (1-3): ")
        # Digit check
        if row.isdigit() == False:
            print("Sorry, that's not a digit!")
        elif row.isdigit() == True:
            if int(row) in acceptable_range:
                # Translate to an index ready integer
                within_range_row = True
            else:
                print("Sorry, that's not within 1-3")
    row_choice = int(row)-1
    return row_choice


def user_input_column():
    # Variables
    column = ''
    acceptable_range = range(1, 4)
    within_range_column = False

    # Two conditions to check for COLUMN

    while column.isdigit() == False or within_range_column == False:
        column = input("Please enter a COLUMN number (1-3): ")
        # Digit check
        if column.isdigit() == False:
            print("Sorry, that's not a digit!")
        # Range check
        elif column.isdigit() == True:
            if int(column) in acceptable_range:
                # Translate to an index ready integer
                within_range_column = True
            else:
                print("Sorry, that's not within 1-3")
    column_choice = int(column)-1
    return column_choice


# Function to see if the space is already taken
def space_check():
    pass


# Function to modify board with user input from user_input()
def replace_choice():
    pass


# Check to see if player won
def check_win():
    pass


# In order for this to work, I may need to remove this logic from this function
def main_game():
    result = ''
    quit_game = False
    within_range = False
    acceptable_result_range_list = [1, 2]

    # Title
    print("TIC - TAC - TOE")

    # Validation
    while quit_game == False:
        while result.isdigit() == False or within_range == False:
            result = input("Enter 1 to START or 2 to Quit: ")
            # Check if digit
            if result.isdigit() == False:
                # clear()
                print("Invalid Entry, please try again")
            # Range Check
            elif result.isdigit() == True and int(result) in acceptable_result_range_list:
                if int(result) == 1:
                    # Check for option 1
                    within_range = True
                    # TODO Does display have to be outside of this loop?!?
                    # Call Display()
                    display()
                    user_input_row()
                    user_input_column()

                elif int(result) == 2:
                    clear()
                    print("Thanks for playing!")
                    quit_game = True
                    quit()
                else:
                    quit()
            else:
                print("Invalid Entry, please try again")


# calling the game
main_game()