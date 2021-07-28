# report.py
#%%
import csv
def read_portfolio(filename):
    '''opens a given portfolio file and
    reads it into a list of tuples'''
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {
                headers[0]:row[0],
                headers[1]:int(row[1]),
                headers[2]:float(row[2])
                }
            portfolio.append(holding)
    return portfolio
#%%   
portfolio = read_portfolio('Data/portfolio.csv')
print(portfolio)
print(portfolio[0])
print(portfolio[1]['shares'])
total = 0.0
for s in portfolio:
    total += s['shares']*s['price']

print(total)
from pprint import pprint
pprint(portfolio)
    # Exercise 2.4

# %%
import csv
def read_prices(filename):
    '''reads a set of prices such as this into a dictionary
    where the keys of the dictionary are the stock names
    and the values in the dictionary are the stock prices.'''
    prices = {}

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            if row ==[]:
                pass
            else:
                prices[row[0]] = float(row[1])
    return prices

price = read_prices('Data/prices.csv')
# for k,v in price.items():
#     print(k,v,'\n')
print(price['IBM'])
print(price['MSFT'])
# %%
