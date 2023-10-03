import random

import data.dog as dog
import data.cat as cat

def isValidResponse(response, options):
    for i in options:
        if response.lower() == i:
            return True
    
    return False

def getResponse(message, options):
    global currentInput

    while (True):
        currentInput = input(message)
        if isValidResponse(currentInput, options):
            print('\n')
            return currentInput
    
        print('Invalid response.\n')

def assignRole(role):
    global playerRole, playerHealth, playerSpeed, playerStrength

    playerRole = role

    if playerRole == 'dog':
        playerHealth = dog.DOG_HEALTH
        playerSpeed = dog.DOG_SPEED
        playerStrength = dog.DOG_STRENGTH
    elif playerRole == 'cat':
        playerHealth = cat.CAT_HEALTH
        playerSpeed = cat.CAT_SPEED
        playerStrength = cat.CAT_STRENGTH

def getLocation(index):
    return LOCATIONS_LIST[index]

def generateRouteString():
    routeString = ''

    for i in LOCATIONS_LIST:
        routeString += i

        if i < LOCATIONS_LIST[len(LOCATIONS_LIST) - 1]:
            routeString += ' -> '

    return routeString

def introduceQuest():
    print('You are an animal who is lost in the ' + getLocation(currentLocationIndex) + '. Your home is at the ' + getLocation(len(LOCATIONS_LIST) - 1) + '. You need to get back home.\n')

def printQuestInfo():
    print('The route back home is: ' + generateRouteString() + '. You are in the ' + getLocation(currentLocationIndex) + ' right now.')
    print('To get to your next location, take', MAX_STEPS, 'steps. You may encounter predators along the way.\n')

def rollDice():
    input('Roll Dice (press any key to continue): ')
    rollNumber = random.randrange(DICE_MIN, DICE_MAX + 1)

    print('Number rolled:', rollNumber, '\n')
    return rollNumber

def takeStep():
    global fighting, stepsTaken

    print('You have taken', stepsTaken, '/', MAX_STEPS, 'steps.')

    if rollDice() == 1:
        fighting = True
        onBattle()
    else:
        stepsTaken += 1
        print('You took a step safely.\n')

def onBattle():
    global inBattle

    print('You rolled a 1. You are now in battle.\n')
    inBattle = False

    print('You are no longer in battle.\n')

DICE_MIN = 1
DICE_MAX = 10

MAX_STEPS = 10

ROLES_LIST = ['dog', 'cat']
LOCATIONS_LIST = ['FIELD', 'FOREST', 'MOUNTAIN', 'VILLAGE']

currentInput = None

playerRole = None
playerHealth = None
playerSpeed = None
playerStrength = None

currentLocationIndex = 0
stepsTaken = 0
inBattle = False
