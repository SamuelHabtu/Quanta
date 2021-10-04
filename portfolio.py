import apicalls


class Portfolio(object):

    def __init__(self, holdings = {}):
        self.holdings = holdings
        self.value = self.getValue()

    def getValue(self):
        sum = 0
        for stock in self.holdings:
            sum += apicalls.quoteEndPoint(stock, "GLOBAL_QUOTE") * self.holdings[stock]
        return sum




