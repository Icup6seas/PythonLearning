

# Help Neeesh choose a game - Generator (in Python), with random Neeesh Reactions...

import random

print("\n")

games = ['PUBG.....', 'WoW......', 'Fortnite.', 'EoT......', 'CoD......', 'Apex.....', 'New World', 'Valheim..']
reactions = ["Nawwww", "That's FIIIIIIIRRREE!!!", "NO SHOT", "LET'S GOOOOOoooOOO!"]

print("What game sounds good to you, Neeesh!?")
print("\n")

gamesList = 0
while gamesList < 8:
    rngGames = random.choice(games)
    rngReactions = random.choice(reactions)
    rngTime = random.randrange(1, 10, 1)
    convertTimeToStr = f'{rngTime}'
    if rngReactions == "That's FIIIIIIIRRREE!!!" or rngReactions == "LET'S GOOOOOoooOOO!":
        print(rngGames + "\t" + "\t" + rngReactions +
              ", but will only last " + convertTimeToStr + " days!!!")
    else:
        print(rngGames + "\t" + "\t" + rngReactions)
    gamesList += 1

