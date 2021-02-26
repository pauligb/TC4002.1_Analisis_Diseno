# profit({
#   "cost_price": 32.67,
#   "sell_price": 45.00,
#   "inventory": 1200}) -> 14796

def profit(data):
	total_profit = (data['sell_price'] - data['cost_price']) * data['inventory']
	return int(round(total_profit))

test_cases_cost_lower = [
	{"cost_price": 0.00,"sell_price": 2.00,"inventory": 100},
	{"cost_price": 1.00,"sell_price": 2.00,"inventory": 100},
	{"cost_price": 32.67,"sell_price": 45.00,"inventory": 1200}
]

test_cases_cost_higher = [
	{"cost_price": 1,"sell_price": 0.00,"inventory": 1200},
	{"cost_price": 2,"sell_price": 0.00,"inventory": 1200},
	{"cost_price": 2,"sell_price": 0.00,"inventory": 1200}
]

test_cases_same = [
	{"cost_price": 65.2,"sell_price": 65.2,"inventory": 1000},
	{"cost_price": 65.2,"sell_price": 65.2,"inventory": 453}
]


test_cases_no_inventory = [
	{"cost_price": 100,"sell_price": 1.00,"inventory": 0},
	{"cost_price": 1.5,"sell_price": 100.00,"inventory": 0}
]

index = 1

def printTestCases(test_cases):
	global index
	for test in test_cases:
		print('Testcase: {0}:'.format(index))
		print('Input: {0}:'.format(test))
		print('Output: {0}'.format(profit(test)))
		print('')
		index = index + 1

print('######################################')
print('Cost price is lower than sell price:')
printTestCases(test_cases_cost_lower)

print('######################################')
print('Cost price is higher than sell price:')
printTestCases(test_cases_cost_higher)

print('######################################')
print('Cost price is the same as sell price:')
printTestCases(test_cases_same)

print('######################################')
print('No inventory:')
printTestCases(test_cases_no_inventory)
