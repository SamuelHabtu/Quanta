from portfolio import Portfolio
from stock import Stock

def main():
    RY = Stock("RY.TO", 10)
    MRU = Stock("MRU.TO", 10)
    SMU = Stock("SMU-U.TO", 10)
    portfolio = Portfolio()
    portfolio.addStock(RY)
    portfolio.addStock(MRU)
    portfolio.addStock(SMU)

if __name__ == "__main__":
    main()
