# **nasdaq-dividend-parser**

### Purpose:
Display  important dividend information about a stock

### Function:
Parses latest dividend information from nasdaq.com

### Usage:

python3 pardiv.py [stock symbols...]

Multithreading Options [-m]

i.e: python3 pardiv.py -m AAPL GE IBM
>"Symbol: AAPL
Ex-dividend Date: 2/9/2018
Payment Date: 2/15/2018
Dividend: $0.63
===========
Symbol: GE
Ex-dividend Date: 2/23/2018
Payment Date: 4/25/2018
Dividend: $0.12
===========
Symbol: IBM
Ex-dividend Date: 2/8/2018
Payment Date: 3/10/2018
Dividend: $1.5
==========="

### Dependencies:
[BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)


