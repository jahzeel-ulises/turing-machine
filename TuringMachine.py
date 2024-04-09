from Rule import Rule
class TuringMachine():
    def __init__(self,rules:dict,inputTape:list) -> None:
        self.rules = rules
        self.currentStatus = '0'
        self.index,self.symbolTape = self.initSymbolTape(inputTape)
    
    def getSymbolTape(self)->list:
        return self.symbolTape
    
    def getIndex(self)->int:
        return self.index
    
    def getStatus(self):
        return self.currentStatus

    def initSymbolTape(self,inputTape:list)->(int,list):
        symbolTape = []
        inicial  = int((25 - len(inputTape))/2)
        for i in range(0,25):
            if i < inicial:
                symbolTape.append('_')
            elif i >= inicial and i < inicial+len(inputTape):
                symbolTape.append(inputTape[i-inicial])
            else:
                symbolTape.append('_')
        return inicial,symbolTape

    def matchSymbolRule(self,rule:Rule,symbol)->bool:
        if rule.getCurrentStatus() == self.currentStatus and rule.getSymbolRead() == symbol:
                    if not rule.getSymbolWrite() == '*':
                        self.symbolTape[self.index] = rule.getSymbolWrite()
                    if not rule.getMov() == '*':
                        if rule.getMov() == 'r':
                            self.index = self.index + 1
                        else:
                            self.index -= 1
                    self.currentStatus = rule.getNextStatus()
                    return rule.getFinalize()
        return None

    def Next(self)->bool:
        symbol = self.symbolTape[self.index]
        try:
            rulesList = self.rules[self.currentStatus]
            rule = None
            for rule in rulesList:
                flag = self.matchSymbolRule(rule,symbol)
                if flag != None:
                    return flag
            for rule in rulesList:
                flag = self.matchSymbolRule(rule,'*')
                if flag != None:
                    return flag
            raise Exception('No hay regla para ese simbolo')
        except Exception as e:
            raise e