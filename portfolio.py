import apicalls


class Portfolio(object):

    def __init__(self, holdings = dict({})):
        self.holdings = holdings
        self.value = self.updateValue()

    def addStock(self, stock):
        self.holdings[stock] = stock.getAmount()
        self.value = self.updateValue()

    def updateValue(self):
        sum = 0
        for stock in self.holdings:
            sum += apicalls.quoteEndPoint(stock.getSymbol(), "GLOBAL_QUOTE") * self.holdings[stock]
        return sum

    def getValue(self):
        return self.value




