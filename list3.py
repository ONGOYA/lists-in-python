prices = [102, 54, 2, 504, 1024, 569]
max = prices[0]
for price in prices:
    if price > max:
        max = price
        print(max)


prices = [102, 54, 2, 504, 1024, 569]
min = prices[0]
for price in prices:
    if price < min:
        price = min
        print(min)
