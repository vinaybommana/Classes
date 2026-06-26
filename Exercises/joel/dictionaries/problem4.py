# Problem 4: Merging Dictionaries
# Given these two dictionaries:

# prices_store_a = {"apples": 1.50, "bananas": 0.75, "oranges": 2.00}
# prices_store_b = {"bananas": 0.60, "grapes": 3.00, "oranges": 1.80}
# Write code that creates a new dictionary best_prices containing the lowest price for each item across both stores.

prices_store_a = {"apples": 1.50, "bananas": 0.75, "oranges": 2.00}

prices_store_b = {"bananas": 0.60, "grapes": 3.00, "oranges": 1.80}

# prices_store_a.update(prices_store_b)

lowest_prices = dict() # {}

for k, v in prices_store_a.items():
    if k in prices_store_b:
        if v < prices_store_b[k]:
            lowest_prices[k] = v
        else:
            lowest_prices[k] = prices_store_b[k]
    else:
        lowest_prices[k] = v

for k, v in prices_store_b.items():
    if k not in prices_store_a:
        lowest_prices[k] = v

print(lowest_prices)