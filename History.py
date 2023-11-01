from Date import getCurrentTime



class History:
    def __init__(self):
        self.history = []

    def getHistorySrting(self,str):
        return getCurrentTime() + " " + str
    def insert2History(self, str):
        string = self.getHistorySrting(str)
        self.history.insert(0, string)

    def getHistoryLength(self):
        return len(self.history)

    def showHistory(self, n):
        if (n > self.getHistoryLength()):
            n = self.getHistoryLength()
        for i in range(n):
            print(self.history[i])
