from random import shuffle


def shuffle_list(listtoshuffle):
    shuffle(listtoshuffle)
    return listtoshuffle


def player_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input("Pick a number - 0, 1, or 2: ")
    return int(guess)


def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print("You found the ball!")
    else:
        print("Wrong! Here it is: ")
        print(mylist)


myList = [' ','O',' ']
shuffled_list = shuffle_list(myList)
guess = player_guess()
check_guess(shuffled_list, guess)