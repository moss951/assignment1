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
            print('')
            return currentInput.upper()
    
        print('Invalid response.\n')

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

def getHealIncrement(health):
    return (health + 3) * 2

def getAttackDamage(strength):
    return (strength + 3) * 2

def getDiceMoveStrengthOffset(roll):
    return roll - 5

def takeStep():
    global stepsTaken, currentLocationIndex

    print('You have taken', stepsTaken, '/', MAX_STEPS, 'steps.\n')

    rollNumber = rollDice()

    if getRollStrength(rollNumber) == 'WEAK':
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
    global currentEnemy, inBattle, playerTurn, playerHealthPoints

    inBattle = True
    print('Your roll is WEAK. You are now in battle.\n')

    currentEnemy = ENEMIES_LIST[currentLocationIndex]
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

    if getRollStrength(rollNumber) == 'STRONG':
        inBattle = False
        print('You successfully ran away from the ' + currentEnemy + '.\n')
        return

    print('You cannot run away from the ' + currentEnemy + '.\n')

def enemyAttack():
    global playerHealthPoints

    playerHealthPoints -= enemyAttackDamage
    print(currentEnemy + ' attacked!')
    print('You lost', enemyAttackDamage, 'health points.\n')

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

def onLose():
    print('You ran out of health points! Game over.')
    quitPrompt()

def onWin():
    print('You have arrived at your home! Congratulations!')
    quitPrompt()

def quitPrompt():
    input('Press enter to quit: ')
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
