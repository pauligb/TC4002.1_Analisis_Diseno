# profit({
#   "cost_price": 32.67,
#   "sell_price": 45.00,
#   "inventory": 1200}) ➞14796

def profit(data):
	total_profit = (data['sell_price'] - data['cost_price']) * data['inventory']
	return total_profit

print(profit({"cost_price": 32.67,"sell_price": 45.00,"inventory": 1200}))