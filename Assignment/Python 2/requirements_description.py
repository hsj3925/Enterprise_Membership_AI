
"""
Please complete the following API based on requirements. 

You will get the data from "price.csv" and "portfolio.csv" in order to save data we have to design Stock class
  The class should have name share price as property. 
  Also, it will have methodn sell and  cost method for the fucture. 

  1. Read data : 
				def read_portfolio(filename):
				def read_prices(filename):
  2. Report data:
				def make_report_data(portfolio, prices):
				def print_report(reportdata):
				def portfolio_report(portfoliofile, pricefile):  

In order to complete requirements, you should make your own packages:

1) Stock.py
2) Report.py
3) pcost.py

The usage will be like below procedure:
	
	read data from price.csv portfolio.csv
	+ portfolio.csv : it contains name shares and price (the unit price which is the cost at the time when I bought)
	+ price.csv : it contains the current stock price

	make data structure through stock classs
	
	then hold the portfolio information and compute the total cost and update status of my portfolio

After complete each API then you will get report as like following.
You should be able to run your functions the same as before:
however, you should run this function in python interpreter.

python
>>> import pcost
>>> pcost.portfolio_cost('portfolio.csv')
44671.15
>>> import report
>>> report.portfolio_report('portfolio.csv', 'prices.csv')
	  Name     Shares      Price     Change
---------- ---------- ---------- ----------
		AA        100       9.22     -22.98
	   IBM         50     106.28      15.18
	   CAT        150      35.46     -47.98
	  MSFT        200      20.89     -30.34
		GE         95      13.48     -26.89
	  MSFT         50      20.89     -44.21
	   IBM        100     106.28      35.84
>>> 
"""
import pcost
import Report

pcost.portfolio_cost("Assignment\A2 Stock\portfolio.csv")

Report.portfolio_report("Assignment\A2 Stock\portfolio.csv", "Assignment\A2 Stock\prices.csv")