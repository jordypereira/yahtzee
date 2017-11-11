from dice import Dice
from scoreboard import Scoreboard
testRoll = [1,2,3,4]
# Make a class of dice
dice = Dice()
score = Scoreboard()

score.showScoreboard()

# Roll 5 dice and save it in the list rolls
rolls = dice.rollX(5)
dice.printRolls(rolls)
# Reroll 2 times
dice.rerollInput(rolls, 2)

# scoreOption = input("Choose which dice to count: ")
print testRoll
score.addScore(score.smallStraight(testRoll))
score.showScoreboard()
