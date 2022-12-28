

# A Magic 8-Ball for Neeesh

import random


choicesList = ['Yes', 'No', 'Maybe', 'I dare not say', 'Most Likely, no!']
choicesLog = []

numOfQuestions = 1
while numOfQuestions < 8:
    randomChoice = random.choice(choicesList)
    print(randomChoice)
    choicesLog.append(randomChoice)
    print(choicesLog)
    numOfQuestions += 1
