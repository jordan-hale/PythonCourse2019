#portfolio = Portfolio() #Creates a new portfolio
#portfolio.addCash(300.50) #Adds cash to the portfolio
#portfolio.withdrawCash(50) #Removes $50

#CODE:
class Portfolio:
    def __init__(self, cash, stock, mutualfund):
        self.cash = cash
        self.stock = stock
        self.mutualfund = mutualfund
    def addCash(self, a_cash):
        self.cash = self.cash + a_cash
    def withdrawCash(self, w_cash):
        self.cash = self.cash - w_cash

#COMMANDS:
portfolio = Portfolio(0, 0, 0)
print(portfolio.cash)
print(portfolio.stock)
print(portfolio.mutualfund)
portfolio.addCash(300.50)
print(portfolio.cash)
portfolio.withdrawCash(50)
print(portfolio.cash)


#s = Stock(20, "HFH") #Create Stock with price 20 and symbol "HFH"

#CODE:
class Stock:
    def __init__(self, price, s_symbol):
        self.price = price
        self.s_symbol = s_symbol

#COMMANDS:
s = Stock(20, "HFH")
print(s.price)
print(s.s_symbol)


#mf1 = MutualFund("BRT") #Create MF with symbol "BRT"
#mf2 = MutualFund("GHT") #Create MF with symbol "GHT"

#CODE:
class MutualFund:
    def __init__(self, mf_symbol):
        self.mf_symbol = mf_symbol

#COMMANDS:
mf1 = MutualFund("BRT")
print(mf1.mf_symbol)
mf2 = MutualFund("GHT")
print(mf2.mf_symbol)


#portfolio.buyStock(5, s) #Buys 5 shares of stock s
portfolio.buyStock(5, s)

#portfolio.buyMutualFund(10.3, mf1) #Buys 10.3 shares of "BRT"
#portfolio.buyMutualFund(2, mf2) #Buys 2 shares of "GHT"
portfolio.buyMutualFund(10.3, mf1) #Buys 10.3 shares of "BRT"
portfolio.buyMutualFund(2, mf2) #Buys 2 shares of "GHT"

#print(portfolio) #Prints portfolio
print(portfolio) #Prints portfolio
    #cash: $140.50
    #stock: 5 HFH
    #mutual funds: 10.33 BRT
    # 2 GHT

#portfolio.sellMutualFund("BRT", 3) #Sells 3 shares of BRT
portfolio.sellMutualFund("BRT", 3) #Sells 3 shares of BRT

#portfolio.sellStock("HFH", 1) #Sells 1 share of HFH
portfolio.sellStock("HFH", 1) #Sells 1 share of HFH

#portfolio.history() #Prints a list of all transactions
portfolio.history() #Prints a list of all transactions
    #ordered by time
