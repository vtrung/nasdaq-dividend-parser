from sys import argv
from bs4 import BeautifulSoup
import requests
import threading

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


class reqthread(threading.Thread):
    def __init__(self,symbol):
        threading.Thread.__init__(self)
        self.symbol = symbol
    def run(self):
        self.stock = stock(self.symbol)
        self.stock.get()
    def getstock(self):
        return self.stock


if __name__ == "__main__":
	if len(argv) > 1:
                #multi define if program will run in parallel or sequentially
                multi = False;
                symbols = argv[1:]
                threads = []
                for symbol in symbols:
                    if symbol[0] == '-':
                        if symbol == "-m":
                            multi = True
                        continue
                    th = reqthread(symbol)
                    threads.append(th)
                
                #start threads: if multi is true, run parallel. if false, run sequentially
                for t in threads:
                    t.start()
                    if not multi:
                        t.join()

                if multi:
                    for t in threads:
                        t.join()
                
                for t in threads:
                    stock = t.getstock()
                    stock.print()
                    print("===========")


	else:
                print("No arguments found")
                print("Please pass in any number of stock symbol you wish to lookup")
                print("Example: python3 pardiv.py IBM AAPL GE")

