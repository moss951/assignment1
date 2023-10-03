import data.game as game

game.introduceQuest()
game.assignRole(game.getResponse('Select animal (dog/cat): ', game.ROLES_LIST))
game.printQuestInfo()

while (not game.inBattle and game.stepsTaken < game.MAX_STEPS):
    game.takeStep()

print('next location')
