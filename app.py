import game as game

game.printInstructions()
game.assignPlayerRole(game.getResponse('Select animal (DOG/CAT): ', game.ROLES_LIST))
game.introduceQuest()
game.printQuestInfo()

while (not game.gameDone):
    game.takeStep()

input('Press enter to quit: ')
quit()
