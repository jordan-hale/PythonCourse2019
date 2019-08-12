#CODE:

#here I am importing the uniform function from random
from random import uniform
#now I am beginning the class "Portfolio"
class Portfolio:
    def __init__(self):
        self.cash = 0
        self.stock = {}
        self.mutualfund = {}
        self.bond = {}
        self.record = []
#this section creates a string representation of the portfolio to be printed
    def __str__(self):
        stocks = []
        for i in self.stock:
            stocks.append(str(i) + " : " + str(self.stock[i]))
        mutualfunds = []
        for i in self.mutualfund:
            mutualfunds.append(str(i) + " : " + str(self.mutualfund[i]))
        bonds = []
        for i in self.bond:
            bonds.append(str(i) + " : " + str(self.bond[i]))
        return """Your portfolio has:
        Cash: %s dollar(s)
        Stocks: %s
        Mutual Funds: %s
        Bonds: %s """ % (str(self.cash), str(stocks), str(mutualfunds), str(bonds))
#this section creates a function to add cash to the portfolio
    def addCash(self, amount):
        self.cash = self.cash + amount
        self.record.append("You have added " + str(amount) + " dollar(s) to your portfolio")
#this section creates a function to withdraw cash from the portfolio
    def withdrawCash(self, amount):
        self.cash = self.cash - amount
        self.record.append("You have removed " + str(amount) + " dollar(s) from your portfolio")
#this section creates a function to buy stocks to add to the portfolio
    def buyStock(self, shares, stock):
        self.cash = self.cash - (shares*stock.purchased)
        if stock.symbol in self.stock.keys():
            self.stock[stock.symbol] += shares
        else: self.stock[stock.symbol] = shares
        self.record.append("You have added " + str(shares) + " share(s) of " + stock.symbol + " to your portfolio")
        self.record.append("You have spent " + str(shares*stock.purchased) + " dollar(s) to do so")
#this section creates a function to buy mutual funds to add to the portfolio
    def buyMutualFund(self, shares, mutualfund):
        self.cash = self.cash - (shares*mutualfund.purchased)
        if mutualfund.symbol in self.mutualfund.keys():
            self.mutualfund[mutualfund.symbol] += shares
        else: self.mutualfund[mutualfund.symbol] = shares
        self.record.append("You have added " + str(shares) + " share(s) of " + mutualfund.symbol + " to your portfolio")
        self.record.append("You have spent " + str(shares*mutualfund.purchased) + " dollar(s) to do so")
#this section creates a function to sell stocks from the portfolio
    def sellStock(self, stock, shares):
        if stock.symbol in self.stock.keys():
            self.stock[stock.symbol] -= shares
            sold = uniform(0.5*stock.purchased, 1.5*stock.purchased)
            self.cash = self.cash + (shares*sold)
            self.record.append("You have sold " + str(shares) + " share(s) of " + stock.symbol + " from your portfolio")
            self.record.append("You have earned " + str(shares*sold) + " dollar(s) from doing so")
#this section creates a function to sell mutual funds from the portfolio
    def sellMutualFund(self, mutualfund, shares):
        if mutualfund.symbol in self.mutualfund.keys():
            self.mutualfund[mutualfund.symbol] -= shares
            sold = uniform(0.9, 1.2)
            self.cash = self.cash + (shares*sold)
        self.cash = self.cash + (shares*sold)
        self.mutualfund[mutualfund.symbol] -= shares
        self.record.append("You have sold " + str(shares) + " share(s) of " + mutualfund.symbol + " from your portfolio")
        self.record.append("You have earned " + str(shares*sold) + " dollar(s) from doing so")
#this section creates a function to reproduce the history of transactions contained in the record
    def history(self):
        for i in self.record:
            print(i)

#now I am beginning the class "Stock"
class Stock:
    def __init__(self, purchased, symbol):
        self.symbol = symbol
        self.purchased = purchased

#now I am beginning the class "MutualFund"
class MutualFund:
    def __init__(self, symbol):
        self.symbol = symbol
        self.purchased = 1

#now I am beginning the class "Bonds"
class Bonds:
    def __init__(self, purchased, symbol):
        self.symbol = symbol
        self.purchased = purchased


#COMMANDS:

portfolio = Portfolio()
portfolio.addCash(300.50)
s = Stock(20, "HFH")
portfolio.buyStock(5, s)
mf1 = MutualFund("BRT")
mf2 = MutualFund("GHT")
portfolio.buyMutualFund(10.3, mf1)
portfolio.buyMutualFund(2, mf2)
print(portfolio)
#Your portfolio has:
        #Cash: 188.2 dollar(s)
        #Stocks: ['HFH : 5']
        #Mutual Funds: ['BRT : 10.3', 'GHT : 2']
        #Bonds: []
portfolio.sellMutualFund(mf1, 3)
portfolio.sellStock(s, 1)
portfolio.withdrawCash(50)
portfolio.history()
#You have added 300.5 dollar(s) to your portfolio
#You have added 5 share(s) of HFH to your portfolio
#You have spent 100 dollar(s) to do so
#You have added 10.3 share(s) of BRT to your portfolio
#You have spent 10.3 dollar(s) to do so
#You have added 2 share(s) of GHT to your portfolio
#You have spent 2 dollar(s) to do so
#You have sold 3 share(s) of BRT from your portfolio
#You have earned 3.132603264938542 dollar(s) from doing so
#You have sold 1 share(s) of HFH from your portfolio
#You have earned 25.352798292261518 dollar(s) from doing so
#You have removed 50 dollar(s) from your portfolio
