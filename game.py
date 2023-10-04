# IMPORTS

import random

import data.dog as dog
import data.cat as cat
import data.beaver as beaver
import data.fox as fox
import data.wolf as wolf
import data.mouse as mouse
import data.spider as spider
import data.scorpion as scorpion

# PRINT INFORMATION

def introduceQuest():
    print('You are an animal who is lost in the ' + getLocation(currentLocationIndex, playerRole) + '. Your home is at the ' + getLocation(len(getLocationList(playerRole)) - 1, playerRole) + '. You need to get back home.\n')

def printQuestInfo():
    print('The route back home is: ' + generateRouteString() + '. You are in the ' + getLocation(currentLocationIndex, playerRole) + ' right now.')
    print('To get to your next location, take', MAX_STEPS, 'steps. You may encounter enemies along the way.\n')

def printInstructions():
    print('INSTRUCTIONS\n')
    print('You can choose between two roles. The roles have different strengths and weaknesses in HEALTH, SPEED and STRENGTH.')
    print('There are three areas you must travel in (or \'challenges\').')
    print('For each step you take, you roll a die. There is a chance you will encounter an enemy, if your roll is WEAK (1 - 3).')
    print('The areas and enemies you encounter depend on what animal you chose.')
    print('The enemies\' attributes get increasingly stronger as you progress. Each animal has a specific strength, and together they will test all your attributes.')
    print('The first player to move in battle is decided by whoever has the greatest SPEED attribute.')
    print('There are three moves you can perform during battle: ATTACK, HEAL and RUN.')
    print('Attack damage and the amount healed can either be boosted, hindered, or left unchanged, determined by the strength of a die roll.')
    print('Running away will only succeed if your die roll is STRONG (8 - 10).')
    print('Enemies have a chance to miss their attacks.')
    print('Your health is reset after every battle.\n')

# GETTER FUNCTIONS

def getLocation(index, role):
    return getLocationList(role)[index]

def getLocationList(role):
    if role == 'DOG':
        return DOG_LOCATIONS_LIST
    elif role == 'CAT':
        return CAT_LOCATIONS_LIST

def getEnemiesList(role):
    if role == 'DOG':
        return DOG_ENEMIES_LIST
    elif role == 'CAT':
        return CAT_ENEMIES_LSIT

def generateRouteString():
    routeString = ''

    for i in getLocationList(playerRole):
        routeString += i

        if i < getLocationList(playerRole)[len(getLocationList(playerRole)) - 1]:
            routeString += ' -> '

    return routeString

def getResponse(message, options):
    global currentInput

    while (True):
        currentInput = input(message)
        if isValidResponse(currentInput, options):
            print('')
            return currentInput.upper()
    
        print('Invalid response.\n')

def isValidResponse(response, options):
    for i in options:
        if response.upper() == i:
            return True
    
    return False

def rollDice():
    input('Roll Dice (press enter to continue): ')
    rollNumber = random.randrange(DICE_MIN, DICE_MAX + 1)

    print('Number rolled:', rollNumber)
    print(getRollStrength(rollNumber) + '\n')
    return rollNumber

def getRollStrength(roll):
    if roll < 4:
        return 'WEAK'
    elif roll > 3 and roll < 8:
        return 'AVERAGE'
    elif roll > 7:
        return 'STRONG'

def generateHealthPoints(health):
    OFFSET = 3
    MULTIPLIER = 5

    return (health + OFFSET) * MULTIPLIER

def getHealIncrement(health):
    OFFSET = 3
    MULTIPLIER = 2

    return (health + OFFSET) * MULTIPLIER

def getAttackDamage(strength):
    OFFSET = 3
    OFFSET = 2

    return (strength + OFFSET) * OFFSET

def getDiceMoveStrengthOffset(roll):
    OFFSET = -5

    return roll + OFFSET

def isPlayerFaster():
    if playerSpeed > enemySpeed:
        return True
    
    return False

def isEnemyDead():
    if enemyHealthPoints <= 0:
        return True
    
    return False

def isPlayerDead():
    if playerHealthPoints <= 0:
        return True
    
    return False

# SETTER FUNCTIONS

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
    elif role == 'MOUSE':
        enemyHealth = mouse.HEALTH
        enemySpeed = mouse.SPEED
        enemyStrength = mouse.STRENGTH
    elif role == 'SPIDER':
        enemyHealth = spider.HEALTH
        enemySpeed = spider.SPEED
        enemyStrength = spider.STRENGTH
    elif role == 'SCORPION':
        enemyHealth = scorpion.HEALTH
        enemySpeed = scorpion.SPEED
        enemyStrength = scorpion.STRENGTH

    enemyHealthPoints = generateHealthPoints(enemyHealth)
    enemyAttackDamage = getAttackDamage(enemyStrength)

# GAME LOGIC

def takeStep():
    global stepsTaken, currentLocationIndex

    print('You have taken', stepsTaken, '/', MAX_STEPS, 'steps.\n')

    rollNumber = rollDice()

    if getRollStrength(rollNumber) == 'WEAK':
        onBattle()

        if gameDone:
            return

    stepsTaken += 1
    print('You took a step safely.\n')

    if stepsTaken == MAX_STEPS:
        stepsTaken = 0
        currentLocationIndex += 1

        print('You have left the ' + getLocation(currentLocationIndex - 1, playerRole) + ' and entered the ' + getLocation(currentLocationIndex, playerRole) + '!\n')

        if getLocation(currentLocationIndex, playerRole) == getLocationList(playerRole)[len(getLocationList(playerRole)) - 1]:
            onWin()
        else:
            printQuestInfo()

def onBattle():
    global currentEnemy, inBattle, playerTurn, playerHealthPoints

    inBattle = True
    print('Your roll is WEAK. You are now in battle.\n')

    currentEnemy = getEnemiesList(playerRole)[currentLocationIndex]
    assignEnemyRole(currentEnemy)
    print('You are fighting a ' + currentEnemy + '!\n')

    if isPlayerFaster():
        playerTurn = False
    else:
        playerTurn = True

    while (inBattle):
        playerTurn = not playerTurn

        print('Player health:', playerHealthPoints)
        print('Enemy health:', enemyHealthPoints, '\n')

        if (playerTurn):
            makeBattleMove(getResponse('What would you like to do (ATTACK/HEAL/RUN)? ', BATTLE_MOVES_LIST))
        else:
            enemyAttack()

        if isPlayerDead() or isEnemyDead():
            inBattle = False

        if isPlayerDead():
            onLose()

    playerHealthPoints = generateHealthPoints(playerHealth)
    print('You are no longer in battle.\n')

def makeBattleMove(move):
    if move == 'ATTACK':
        playerAttack()
    elif move == 'HEAL':
        playerHeal()
    elif move == 'RUN':
        playerRun()

def playerAttack():
    global enemyHealthPoints, currentEnemy
    
    rollNumber = rollDice()

    offsetAttackDamage = playerAttackDamage + getDiceMoveStrengthOffset(rollNumber)

    if offsetAttackDamage <= 0:
        offsetAttackDamage = 1

    enemyHealthPoints -= offsetAttackDamage
    print(currentEnemy + ' has lost', offsetAttackDamage, 'health points.\n')

def playerHeal():
    global playerHealthPoints

    rollNumber = rollDice()

    if playerHealthPoints < generateHealthPoints(playerHealth):
        healAmount = getHealIncrement(playerHealth) + getDiceMoveStrengthOffset(rollNumber)

        if playerHealthPoints + healAmount > generateHealthPoints(playerHealth):
            healAmount = generateHealthPoints(playerHealth) - playerHealthPoints

        if healAmount <= 0:
            healAmount = 1
        
        playerHealthPoints += healAmount
        print('You gained', healAmount, 'health points.\n')
    else:
        print('You are at maximum health.')

def playerRun():
    global inBattle, currentEnemy

    rollNumber = rollDice()
    
    if isPlayerFaster():
        if getRollStrength(rollNumber) == 'STRONG':
            inBattle = False
            print('You successfully ran away from the ' + currentEnemy + '.\n')
            return
    else:
        print(currentEnemy + ' is faster than you.')

    print('You cannot run away from the ' + currentEnemy + '.\n')

def enemyAttack():
    global playerHealthPoints

    attackAccuracy = random.randrange(0, 4)

    if attackAccuracy != 0:
        playerHealthPoints -= enemyAttackDamage
        print(currentEnemy + ' attacked!')
        print('You lost', enemyAttackDamage, 'health points.\n')
    else:
        print(currentEnemy + ' tried to attack, but missed!\n')

# GAME OUTCOMES

def onLose():
    global gameDone
    
    gameDone = True
    print('You ran out of health points! Game over.')

def onWin():
    global gameDone

    gameDone = True
    print('You have arrived at your home! Congratulations!')

# CONSTANTS

DICE_MIN = 1
DICE_MAX = 10

MAX_STEPS = 10

ROLES_LIST = ['DOG', 'CAT']
DOG_LOCATIONS_LIST = ['FIELD', 'FOREST', 'MOUNTAIN', 'VILLAGE']
CAT_LOCATIONS_LIST = ['MEADOW', 'CAVE', 'DESERT', 'VILLAGE']
DOG_ENEMIES_LIST = ['BEAVER', 'FOX', 'WOLF']
CAT_ENEMIES_LSIT = ['MOUSE', 'SPIDER', 'SCORPION']
BATTLE_MOVES_LIST = ['ATTACK', 'HEAL', 'RUN']

# VARIABLES

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
gameDone = False
