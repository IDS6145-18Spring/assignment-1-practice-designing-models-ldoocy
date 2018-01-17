from transportation import transportation
from roadways import roadways

class tollRoads(roadways):

    def __init__(self, num, r, n, a, s, t, att, m):
        self.numTollBooths = t
        self.numAttendants = att
        self.dailyMoney = m
        roadways.__init__(self, num, r, n, a, s)

    def chargeToll(self):
        return
