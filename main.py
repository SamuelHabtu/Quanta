from portfolio import Portfolio

def main():
    holdings = {"RY": 10, "MSFT":10}
    test = Portfolio(holdings)
    print(test.value)

if __name__ == "__main__":
    main()
