# IMPORTS

import random

# import enemy information
import data.dog as dog
import data.cat as cat
import data.beaver as beaver
import data.fox as fox
import data.wolf as wolf
import data.mouse as mouse
import data.spider as spider
import data.scorpion as scorpion

# PRINT INFORMATION

def introduceQuest(): # make a string that describes the quest
    print('You are an animal who is lost in the ' + getLocation(currentLocationIndex, playerRole) + '. Your home is at the ' + getLocation(len(getLocationList(playerRole)) - 1, playerRole) + '. You need to get back home.\n')

def printQuestInfo(): # make a string that shows the progress of the game
    print('The route back home is: ' + generateRouteString() + '. You are in the ' + getLocation(currentLocationIndex, playerRole) + ' right now.')
    print('To get to your next location, take', MAX_STEPS, 'steps. You may encounter enemies along the way.\n')

def printInstructions(): # print instructions
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

def getLocation(index, role): # get a location string given an array index and the player's role
    return getLocationList(role)[index]

def getLocationList(role): # get the array that contains the player's role's locations they must go through
    if role == 'DOG':
        return DOG_LOCATIONS_LIST
    elif role == 'CAT':
        return CAT_LOCATIONS_LIST

def getEnemiesList(role): # get the array that contains the player's role's enemies they must encounter
    if role == 'DOG':
        return DOG_ENEMIES_LIST
    elif role == 'CAT':
        return CAT_ENEMIES_LSIT

def generateRouteString(): # make a string that displays all the locations the player must go through
    routeString = ''

    for i in getLocationList(playerRole):
        routeString += i

        if i < getLocationList(playerRole)[len(getLocationList(playerRole)) - 1]:
            routeString += ' -> '

    return routeString

def getResponse(message, options): # prompt the player with a message given a message string and an array of options
    global currentInput

    while (True): # loop until the player gives a valid response
        currentInput = input(message)
        if isValidResponse(currentInput, options):
            print('')
            return currentInput.upper()
    
        print('Invalid response.\n')

def isValidResponse(response, options): # checks if the player's response is valid, given their response and an array of options
    for i in options: 
        if response.upper() == i:
            return True
    
    return False 

def rollDice(): # prompt the user to roll a die, then rolls the die
    input('Roll Dice (press enter to continue): ')
    rollNumber = random.randrange(DICE_MIN, DICE_MAX + 1)

    print('Number rolled:', rollNumber)
    print(getRollStrength(rollNumber) + '\n')
    return rollNumber

def getRollStrength(roll): # categorizes a roll as either WEAK, AVERAGE or STRONG depending on the number rolled
    if roll < 4:
        return 'WEAK'
    elif roll > 3 and roll < 8:
        return 'AVERAGE'
    elif roll > 7:
        return 'STRONG'

def generateHealthPoints(health): # generate the total number of health points for a player or enemy based on their health attribute
    OFFSET = 3 # the weakest value for an attribute is -2, so this constant will offset the value so it always becomes positive, ready to be used correctly
    MULTIPLIER = 5

    return (health + OFFSET) * MULTIPLIER

def getHealIncrement(health): # generate the number of health points to be healed by the player, when the HEAL move is used 
    OFFSET = 3 # the weakest value for an attribute is -2, so this constant will offset the value so it always becomes positive, ready to be used correctly
    MULTIPLIER = 2 

    return (health + OFFSET) * MULTIPLIER

def getAttackDamage(strength): # generate the nummber of damage an attack deals, based on a player or enemy's strength attribute
    OFFSET = 3 # the weakest value for an attribute is -2, so this constant will offset the value so it always becomes positive, ready to be used correctly
    MULTIPLIER = 2

    return (strength + OFFSET) * MULTIPLIER

def getDiceMoveStrengthOffset(roll): # gets the amount gained or lost of a move based on a die roll
    OFFSET = -5 # the die ranges from 1 to 10. This function will return negative and positive values, which will be added to the value of a move

    return roll + OFFSET

def isPlayerFaster(): # checks if the player is faster than the enemy
    if playerSpeed > enemySpeed:
        return True
    
    return False

def isEnemyDead(): # checks if the enemy is dead (no more health points)
    if enemyHealthPoints <= 0:
        return True
    
    return False

def isPlayerDead(): # checks if the player is dead
    if playerHealthPoints <= 0:
        return True
    
    return False

# SETTER FUNCTIONS

def assignPlayerRole(role): # sets the player's attributes determined by the given role
    global playerRole, playerHealth, playerSpeed, playerStrength, playerHealthPoints, playerAttackDamage # allow these variables to be set inside this function

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

def assignEnemyRole(role): # sets the enemy's attributes determined by the given role
    global enemyRole, enemyHealth, enemySpeed, enemyStrength, enemyHealthPoints, enemyAttackDamage # allow these variables to be set inside this function

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

def takeStep(): # logic for the player to take a step
    global stepsTaken, currentLocationIndex # allow these variables to be edited inside this function

    print('You have taken', stepsTaken, '/', MAX_STEPS, 'steps.\n')

    rollNumber = rollDice()

    if getRollStrength(rollNumber) == 'WEAK':
        onBattle() # start battle sequence

        if gameDone: # checks if the game is finished, either by a win or loss
            return

    stepsTaken += 1 
    print('You took a step safely.\n')

    if stepsTaken == MAX_STEPS:
        stepsTaken = 0
        currentLocationIndex += 1

        print('You have left the ' + getLocation(currentLocationIndex - 1, playerRole) + ' and entered the ' + getLocation(currentLocationIndex, playerRole) + '!\n')

        if getLocation(currentLocationIndex, playerRole) == getLocationList(playerRole)[len(getLocationList(playerRole)) - 1]: # checks if the player is at the last location
            onWin()
        else:
            printQuestInfo() # new area quest info

def onBattle(): # battle sequence and loop
    global currentEnemy, inBattle, playerTurn, playerHealthPoints # allow these variables to be changed inside this function

    inBattle = True
    print('Your roll is WEAK. You are now in battle.\n')

    currentEnemy = getEnemiesList(playerRole)[currentLocationIndex] # get the enemy for the specified area and player role
    assignEnemyRole(currentEnemy)
    print('You are fighting a ' + currentEnemy + '!\n')

    if isPlayerFaster():
        playerTurn = False
    else:
        playerTurn = True

    while (inBattle): # battle turn-based loop
        playerTurn = not playerTurn # alternate between player's turn and enemy's turn

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

    playerHealthPoints = generateHealthPoints(playerHealth) # reset health points after battle is over
    print('You are no longer in battle.\n')

def makeBattleMove(move): # run battle move functions depending on the player's response
    if move == 'ATTACK':
        playerAttack()
    elif move == 'HEAL':
        playerHeal()
    elif move == 'RUN':
        playerRun()

def playerAttack(): # deal damage to the enemy
    global enemyHealthPoints, currentEnemy # allow these variables to be changed inside of this function
    
    rollNumber = rollDice()

    offsetAttackDamage = playerAttackDamage + getDiceMoveStrengthOffset(rollNumber) # change the default attack damage by the dice offset

    if offsetAttackDamage <= 0: # there may be some cases where the dice offsets too much and it becomes a negative number, so this makes these cases deal 1 damage instead
        offsetAttackDamage = 1

    enemyHealthPoints -= offsetAttackDamage
    print(currentEnemy + ' has lost', offsetAttackDamage, 'health points.\n')

def playerHeal(): # add a certain amount to the player's health points
    global playerHealthPoints # allow this variable to be changed inside this function

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
