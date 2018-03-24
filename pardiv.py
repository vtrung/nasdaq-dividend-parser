from sys import argv
from bs4 import BeautifulSoup
import requests

class stock:
	symbol = ""
	div = ""
	exd = ""
	payd = ""
	
	def __init__(self, symbol):
		self.symbol = symbol
	
	## request dividend data from nasdaq.com
	def get(self):
		url = "https://www.nasdaq.com/symbol/" + self.symbol + "/dividend-history"
		r = requests.get(url)
		soup = BeautifulSoup(r.text, "html.parser")
		self.exd = self.getcontent(soup.select("#quotes_content_left_dividendhistoryGrid_exdate_0"))
		self.div = self.getcontent(soup.select("#quotes_content_left_dividendhistoryGrid_CashAmount_0"))
		self.payd = self.getcontent(soup.select("#quotes_content_left_dividendhistoryGrid_PayDate_0"))
	
	## get string from soup tag object	
	def getcontent(self, tag):
		for t in tag:
			return t.string
	
	## Print Values of Stock Object
	def print(self):
		print("Symbol:", self.symbol)
		print("Ex-dividend Date:", self.exd)
		print("Payment Date:", self.payd)
		print("Dividend: $", self.div, sep='')
		

if __name__ == "__main__":
	if len(argv) > 1:
                symbols = argv[1:]
                for symbol in symbols:
                    s = stock(symbol)
                    s.get()
                    s.print()
                    print("===========")
	else:
                print("No arguments found")
                print("Please pass in any number of stock symbol you wish to lookup")
                print("Example: python3 pardiv.py IBM AAPL GE")
		#tickers = ["GE","IBM", "AAPL"]
		#for sym in tickers:
		#	s = stock(sym)
		#	s.get()
		#	s.print()
		#	print("============")
	
