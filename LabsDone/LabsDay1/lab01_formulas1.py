
"""
Calculate the profit from the sale of stock and calculate the
new price of a product going on sale.
"""

shares = 125
purch_price = 25.32
sale_price = 48.97
profit1 = shares * (sale_price - purch_price)
print 'Profit is', profit1  # unformatted

price = 127.99
discount = 0.16  # or 16%
sale_price = price - price * discount
print 'Sale price is', sale_price  # unformatted

