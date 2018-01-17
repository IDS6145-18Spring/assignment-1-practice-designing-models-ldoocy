from transportation import transportation

class publicTransport(transportation):

    def __init__(self, num, r, n, cap, l):
        self.numVehicles = n
        self.capacity = cap
        self.stopLocations = l
        transportation.__init__(self, num, r)

    def start(self, t):
        '''record start time'''
        self.startTime = t
        return

    def stop(self, t):
        '''record stop time, record time running'''
        self.stopTime = t
        return stopTime - startTime
