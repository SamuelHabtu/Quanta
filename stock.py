
class Stock(object):

    def __init__(self, symbol, amount = 0):
        self.symbol = symbol
        self.amount = amount

    def __repr__(self):
        return self.symbol

    def getSymbol(self):
        return self.symbol

    def getAmount(self):
        return self.amount
    
    def setAmount(self, amount):
        self.amount= amount
    