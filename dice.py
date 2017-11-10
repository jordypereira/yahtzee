import random
class Dice:
    _eyes = 6
    def __init__(self, eyes = _eyes):
        self._eyes = eyes

    def roll(self):
        roll = random.randint(0, self._eyes)
        return str(roll)
    def rollX(self, x = 1):
        rolls = []
        for i in range(0, x):
            rolls.append(random.randint(0, self._eyes))
        return rolls

    def printRoll(self, x = 1):
        rolls = self.rollX(x)
        print " -------------------"
        for i, val in enumerate(rolls):
            print "|  Roll #" + str(i+1) + "     " + str(val) + "    |"
        print " -------------------"
