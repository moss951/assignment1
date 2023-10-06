import game as game

game.printInstructions()
game.assignPlayerRole(game.getResponse('Select animal (DOG/CAT): ', game.ROLES_LIST))
game.introduceQuest()
game.printQuestInfo()

while (not game.gameDone): # GAME LOOP
    game.takeStep()

input('Press enter to quit: ') # runs after the game has either been won or lost
quit()
