import random
class Dice:
    _eyes = 6
    def __init__(self, eyes = _eyes):
        self._eyes = eyes

    def roll(self):
        roll = random.randint(0, self._eyes)
        return roll

dice = Dice()
print dice.roll()
