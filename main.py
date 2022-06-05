import random

def computerDecision():
    list_of_choices = ['Rock','Paper','Scissors']
    return random.choice(list_of_choices)

def convert_user_input(userInput):
    if userInput == 'r':
        return 'Rock'
    elif userInput == 's':
        return 'Scissors'
    else:
        return 'Paper'

def decideWinner(userInput,computerDecision):
    if userInput == 'Rock' and computerDecision == 'Scissors':
        print('User Won')
        return 1
    elif userInput == 'Scissors' and computerDecision == 'Paper':
        print('User Won')
        return 1
    elif userInput == 'Paper' and computerDecision == 'Rock':
        print('User won')
        return 1
    elif computerDecision == 'Rock' and userInput == 'Scissors':
        print('Computer Won')
        return 1
    elif computerDecision == 'Scissors' and userInput == 'Paper':
        print('Computer won')
        return 1
    elif computerDecision == 'Paper' and userInput == 'Rock':
        print('Computer won')
        return 1
    elif userInput == computerDecision:
        print('Try again, It is a draw')
        return 0

def checkUserInput(userInput):
    userInput = userInput.lower()
    command = ['r','s','p']
    if (userInput not in command):
        print('Invalid Selection, Enter another Option')
        return True
    return False

def collectInput():
    userInput = input('R, P, S:  ')
    return userInput

start = True
print('Welcome to the Rock Paper Scissors Game\n R means Rock, P means paper, S means scissors\n==========\n==========\n==========')
while(start):
    decisionChecking = True
    while(decisionChecking):
        userInput = collectInput()
        decisionChecking = checkUserInput(userInput)

    userInput = convert_user_input(userInput)
    computerPlay = computerDecision()
    print('Player:',userInput,'Computer:', computerPlay)
    continuity = decideWinner(userInput,computerPlay)

    if continuity == 1:
        start=False