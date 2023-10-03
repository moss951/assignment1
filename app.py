import game as game

game.introduceQuest()
game.assignPlayerRole(game.getResponse('Select animal (DOG/CAT): ', game.ROLES_LIST))
game.printQuestInfo()

while (game.stepsTaken < game.MAX_STEPS):
    game.takeStep()
