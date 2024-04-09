class Rule():
    def __init__(self,currentStatus,symbolRead,symbolWrite,mov,nextStatus,finalize = False):
        self.currentState = currentStatus
        self.symbolRead = symbolRead
        self.symbolWrite = symbolWrite
        self.mov = mov
        self.nextStatus = nextStatus
        self.finalize = finalize
    def getCurrentStatus(self):
        return self.currentState
    def getSymbolRead(self):
        return self.symbolRead
    def getSymbolWrite(self):
        return self.symbolWrite
    def getMov(self):
        return self.mov
    def getNextStatus(self):
        return self.nextStatus
    def getFinalize(self):
        return self.finalize
    def __str__(self) -> str:
        return self.currentState+' '+self.symbolRead+' '+self.symbolWrite+' '+self.mov+' '+self.nextStatus+' '+str(self.finalize)