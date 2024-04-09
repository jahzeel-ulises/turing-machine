import Rule
class Parser():

    def __init__(self)->None:
        with open('turing_machine_rules.txt','r') as archivo:
            self.lines = archivo.readlines()
        
    def parseFile(self):
        for line in self.lines:
            if not line.startswith('#'):
                elementos = line.strip().split(' ')
                if len(elementos) != 5 and len(elementos) != 6:
                    raise SyntaxError("Numero de caracteres por regla incorrectos")
                if len(elementos[1]) != 1  or len(elementos[2]) != 1:
                    raise  SyntaxError("Simbolos no admitidos, deben ser caracteres")
                if elementos[3] not in ['l','r','*']:
                    raise SyntaxError("Movimiento invalido, debe ser l,r,*")
                if len(elementos) == 6:
                    if elementos[5] not in ['T','F']:
                        raise SyntaxError('Simbolo invalido, debe ser T o F') 
            

    def createRulesDictionary(self)->dict:
        rules = dict()
        for line in self.lines:
            if not line.startswith('#'):
                elementos = line.strip().split(' ')
                if elementos[0] in rules.keys():
                    rulesList = rules[elementos[0]]
                    for rule in rulesList:
                        if rule.getSymbolRead() == elementos[1]:
                            raise SyntaxError("Muchas funciones para un simbolo leido")
                else:
                    rules[elementos[0]] = []

                if len(elementos) == 5:
                    newRule = Rule.Rule(elementos[0],elementos[1],elementos[2],elementos[3],elementos[4])
                else:
                    newRule = Rule.Rule(elementos[0],elementos[1],elementos[2],elementos[3],elementos[4],True if elementos[5] == 'T' else False)
                rules[elementos[0]].append(newRule)
        return rules
            

            
            
