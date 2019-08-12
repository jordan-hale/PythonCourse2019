from random import uniform
class Portfolio:
      def __init__(self):
          self.cash = 0
          self.stock = {}
          self.mutualfund = {}
          self.bond = {}
          self.record = []
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
      def addCash(self, amount):
          self.cash = self.cash + amount
          self.record.append("You have added " + str(amount) + " dollar(s) to your portfolio")
      def withdrawCash(self, amount):
          self.cash = self.cash - amount
          self.record.append("You have removed " + str(amount) + " dollar(s) from your portfolio")
      def buyStock(self, shares, stock):
          self.cash = self.cash - (shares*stock.purchased)
          if stock.symbol in self.stock.keys():
              self.stock[stock.symbol] += shares
          else: self.stock[stock.symbol] = shares
          self.record.append("You have added " + str(shares) + " share(s) of " + stock.symbol + " to your portfolio")
          self.record.append("You have spent " + str(shares*stock.purchased) + " dollar(s) to do so")
      def buyMutualFund(self, shares, mutualfund):
          self.cash = self.cash - (shares*mutualfund.purchased)
          if mutualfund.symbol in self.mutualfund.keys():
              self.mutualfund[mutualfund.symbol] += shares
          else: self.mutualfund[mutualfund.symbol] = shares
          self.record.append("You have added " + str(shares) + " share(s) of " + mutualfund.symbol + " to your portfolio")
          self.record.append("You have spent " + str(shares*mutualfund.purchased) + " dollar(s) to do so")
      def sellStock(self, stock, shares):
          if stock.symbol in self.stock.keys():
              self.stock[stock.symbol] -= shares
              sold = uniform(0.5*stock.purchased, 1.5*stock.purchased)
              self.cash = self.cash + (shares*sold)
              self.record.append("You have sold " + str(shares) + " share(s) of " + stock.symbol + " from your portfolio")
              self.record.append("You have earned " + str(shares*sold) + " dollar(s) from doing so")
      def sellMutualFund(self, mutualfund, shares):
          if mutualfund.symbol in self.mutualfund.keys():
              self.mutualfund[mutualfund.symbol] -= shares
              sold = uniform(0.9, 1.2)
              self.cash = self.cash + (shares*sold)
          self.cash = self.cash + (shares*sold)
          self.mutualfund[mutualfund.symbol] -= shares
          self.record.append("You have sold " + str(shares) + " share(s) of " + mutualfund.symbol + " from your portfolio")
          self.record.append("You have earned " + str(shares*sold) + " dollar(s) from doing so")
      def history(self):
          for i in self.record:
              print(i)

class Stock:
      def __init__(self, purchased, symbol):
          self.symbol = symbol
          self.purchased = purchased

class MutualFund:
      def __init__(self, symbol):
          self.symbol = symbol
          self.purchased = 1

class Bonds:
      def __init__(self, purchased, symbol):
          self.symbol = symbol
          self.purchased = purchased
