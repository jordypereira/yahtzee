class Scoreboard:
    _round = 1
    _players = 1
    _upperScore = 0
    _lowerScore = 0
    _totalScore = _upperScore + _lowerScore

    _optionsUpper = ["Count all 1's", "Count all 2's", "Count all 3's", "Count all 4's", "Count all 5's", "Count all 6's"]
    _optionsLower = ["3 of a kind", "4 of a kind", "Small Straight", "Large Straight", "Full House"]

    def __init__(self, players = _players):
        self._players = players

    def showScoreboard(self):
        print " ---------------"
        print "    Round #{}   ".format(self._round)
        print "    Score {}   ".format(self._totalScore)
        print " ---------------"
    def addScoreUpper(self, score):
        self._upperScore += score
        self._totalScore += score
        self._round += 1
    def addScoreLower(self, score):
        self._lowerScore += score
        self._totalScore += score
        self._round += 1
    def addScore(self, score):
        self._totalScore += score
        self._round += 1

    def upper(self, dice, rolls):
        count = rolls.count(dice)
        score = count * dice
        return score

    def ofAKind(self, kind, dice, rolls):
        count = rolls.count(dice)
        if count >= kind:
            score = count * dice
        else: score = 0
        return score

    def largeStraight(self, rolls):
        score = 0
        option1 = set([1, 2, 3, 4 ,5])
        option2 = set([2, 3, 4 ,5, 6])
        for i in range(1, 2):
            if option[i].issubset(rolls):
                score = 40
                break
        return score

    def smallStraight(self, rolls):
        score = 0
        options = [set([1, 2, 3, 4]), set([2, 3, 4 ,5]), set([3, 4 ,5, 6])]
        option2 = set([2, 3, 4 ,5])
        option3 = set([3, 4 ,5, 6])

        for i in range(1, len(options)):
            if options[i].issubset(rolls):
                score = 30
                break
        print options
        return score
    # def straight(self, rolls, options, ro)
    def fullHouse(self, rolls):
        check2 = check3 = False
        for i in range(1, 6):
            if rolls.count(i) == 3:
                check3 = True
            if rolls.count(i) == 2:
                check2 = True
        if check2 and check3:
            score = 25
        else: score = 0
        return score
