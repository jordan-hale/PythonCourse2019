#portfolio = Portfolio() #Creates a new portfolio
#portfolio.addCash(300.50) #Adds cash to the portfolio

class Portfolio:
    def __init__(self, cash, stock, mutualfund):
        self.cash = cash
        self.stock = stock
        self.mutualfund = mutualfund
    def addCash(self, cash):
        self.cash = int(self.cash) + cash

    #portfolio = Portfolio(26, 2, 18)
    #print(portfolio.cash)
    #print(portfolio.stock)
    #print(portfolio.mutualfund)
    #portfolio.addCash(300.50)
    #print(portfolio.cash)

s = Stock(20, "HFH") #Create Stock with price 20 and symbol "HFH"

portfolio.buyStock(5, s) #Buys 5 shares of stock s

mf1 = MutualFund("BRT") #Create MF with symbol "BRT"

mf2 = MutualFund("GHT") #Create MF with symbol "GHT"

portfolio.buyMutualFund(10.3, mf1) #Buys 10.3 shares of "BRT"

portfolio.buyMutualFund(2, mf2) #Buys 2 shares of "GHT"

print(portfolio) #Prints portfolio

#cash: $140.50
#stock: 5 HFH
#mutual funds: 10.33 BRT
# 2 GHT

portfolio.sellMutualFund("BRT", 3) #Sells 3 shares of BRT

portfolio.sellStock("HFH", 1) #Sells 1 share of HFH

portfolio.withdrawCash(50) #Removes $50

portfolio.history() #Prints a list of all transactions
#ordered by time
