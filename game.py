import random

import data.dog as dog
import data.cat as cat
import data.beaver as beaver
import data.fox as fox
import data.wolf as wolf

def introduceQuest():
    print('You are an animal who is lost in the ' + getLocation(currentLocationIndex) + '. Your home is at the ' + getLocation(len(LOCATIONS_LIST) - 1) + '. You need to get back home.\n')

def printQuestInfo():
    print('The route back home is: ' + generateRouteString() + '. You are in the ' + getLocation(currentLocationIndex) + ' right now.')
    print('To get to your next location, take', MAX_STEPS, 'steps. You may encounter predators along the way.\n')

def getLocation(index):
    return LOCATIONS_LIST[index]

def generateRouteString():
    routeString = ''

    for i in LOCATIONS_LIST:
        routeString += i

        if i < LOCATIONS_LIST[len(LOCATIONS_LIST) - 1]:
            routeString += ' -> '

    return routeString

def isValidResponse(response, options):
    for i in options:
        if response.upper() == i:
            return True
    
    return False

def getResponse(message, options):
    global currentInput

    while (True):
        currentInput = input(message)
        if isValidResponse(currentInput, options):
            print('\n')
            return currentInput.upper()
    
        print('Invalid response.\n')

def rollDice():
    input('Roll Dice (press any key to continue): ')
    rollNumber = random.randrange(DICE_MIN, DICE_MAX + 1)

    print('Number rolled:', rollNumber, '\n')
    return rollNumber

def assignPlayerRole(role):
    global playerRole, playerHealth, playerSpeed, playerStrength, playerHealthPoints, playerAttackDamage

    playerRole = role

    if role == 'DOG':
        playerHealth = dog.HEALTH
        playerSpeed = dog.SPEED
        playerStrength = dog.STRENGTH
    elif role == 'CAT':
        playerHealth = cat.HEALTH
        playerSpeed = cat.SPEED
        playerStrength = cat.STRENGTH
        
    playerHealthPoints = generateHealthPoints(playerHealth)
    playerAttackDamage = getAttackDamage(playerStrength)

def assignEnemyRole(role):
    global enemyRole, enemyHealth, enemySpeed, enemyStrength, enemyHealthPoints, enemyAttackDamage

    enemyRole = role

    if role == 'BEAVER':
        enemyHealth = beaver.HEALTH
        enemySpeed = beaver.SPEED
        enemyStrength = beaver.STRENGTH
    elif role == 'FOX':
        enemyHealth = fox.HEALTH
        enemySpeed = fox.SPEED
        enemyStrength = fox.STRENGTH
    elif role == 'WOLF':
        enemyHealth = wolf.HEALTH
        enemySpeed = wolf.SPEED
        enemyStrength = wolf.STRENGTH

    enemyHealthPoints = generateHealthPoints(enemyHealth)
    enemyAttackDamage = getAttackDamage(enemyStrength)

def generateHealthPoints(health):
    return (health + 3) * 5

def getAttackDamage(strength):
    return (strength + 3) * 2

def takeStep():
    global stepsTaken, currentLocationIndex

    print('You have taken', stepsTaken, '/', MAX_STEPS, 'steps.')

    if rollDice() == 1:
        onBattle()
    else:
        stepsTaken += 1

        print('You took a step safely.\n')

    if stepsTaken == MAX_STEPS:
        stepsTaken = 0
        currentLocationIndex += 1

        print('You have left the ' + getLocation(currentLocationIndex - 1) + ' and entered the ' + getLocation(currentLocationIndex) + '!\n')

        if getLocation(currentLocationIndex) == LOCATIONS_LIST[len(LOCATIONS_LIST) - 1]:
            onWin()

def onBattle():
    global currentEnemy, inBattle, playerTurn, playerHealth

    inBattle = True
    print('You rolled a 1. You are now in battle.\n')

    currentEnemy = ENEMIES_LIST[currentLocationIndex]
    assignEnemyRole(currentEnemy)
    print('You are fighting a ' + currentEnemy + '!\n')

    if isPlayerFaster():
        playerTurn = False
    else:
        playerTurn = True

    while (inBattle):
        playerTurn = not playerTurn

        if (playerTurn):
            makeBattleMove(getResponse('What would you like to do (ATTACK/HEAL/RUN)? ', BATTLE_MOVES_LIST))
        else:
            enemyAttack()

    playerHealth = generateHealthPoints(playerHealth)
    print('You are no longer in battle.\n')

def isPlayerFaster():
    if playerSpeed > enemySpeed:
        return True
    
    return False

def makeBattleMove(move):
    if move == 'ATTACK':
        playerAttack()
    elif move == 'HEAL':
        playerHeal()
    elif move == 'RUN':
        playerRun()

def playerAttack():
    global enemyHealthPoints, currentEnemy
    
    enemyHealthPoints -= playerAttackDamage
    print(currentEnemy + ' has lost', playerAttackDamage, 'health points.\n')

def playerHeal():
    global playerHealthPoints

    healAmount = (playerHealth + 3) * 2
    playerHealthPoints += healAmount
    print('You gained', healAmount, 'health points.\n')

def playerRun():
    global inBattle, currentEnemy

    if isPlayerFaster:
        inBattle = False
        print('You successfully ran away from the ' + currentEnemy + '.\n')

    print('You cannot run away from the ' + currentEnemy + '.\n')

def enemyAttack():
    global playerHealthPoints

    playerHealthPoints -= enemyAttackDamage
    print('You lost', enemyAttackDamage, 'health points.\n')

def onWin():
    print('You have arrived at your home! Congratulations!')
    input('Press any key to quit: ')
    quit()

DICE_MIN = 1
DICE_MAX = 10

MAX_STEPS = 10

ROLES_LIST = ['DOG', 'CAT']
LOCATIONS_LIST = ['FIELD', 'FOREST', 'MOUNTAIN', 'VILLAGE']
ENEMIES_LIST = ['BEAVER', 'FOX', 'WOLF']
BATTLE_MOVES_LIST = ['ATTACK', 'HEAL', 'RUN']

currentInput = None
currentEnemy = None

playerRole = None
playerHealth = None
playerSpeed = None
playerStrength = None
playerHealthPoints = None
playerAttackDamage = None

enemyRole = None
enemyHealth = None
enemySpeed = None
enemyStrength = None
enemyHealthPoints = None
enemyAttackDamage = None

currentLocationIndex = 0
stepsTaken = 0
inBattle = False
playerTurn = False