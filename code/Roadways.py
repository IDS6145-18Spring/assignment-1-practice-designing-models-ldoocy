from transportation import transportation

class roadways(transportation):

    def __init__(self, num, r, n, a, s):
        self.numCars = n
        self.avgNumPassengers = a
        self.speedLimit = s
        transportation.__init__(self, num, r)

    def startDriving(self, t):
        '''record start time'''
        self.startTime = t
        return

    def stopDriving(self, t):
        '''record stop time, record time running'''
        self.stopTime = t
        return stopTime - startTime
