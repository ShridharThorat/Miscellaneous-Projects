hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Your solution below

# Prices and Cuts
total_price = 0

for price in prices:
    total_price += price

average_price = total_price/len(prices)

print(f"Average Haircut Pirce:\n{average_price}")

new_prices = [price-5 for price in prices]
print(new_prices)

# Revenue
total_revenue = 0

for i in range(0,len(hairstyles)):
    total_revenue += prices[i]*last_week[i]
print(f"Total Revenue: {total_revenue}")

average_daily_revenue = total_revenue/7

cuts_under_30 = []
for i in range (0,len(new_prices)-1):
    if new_prices[i] < 30:
        cuts_under_30.append(hairstyles[i])

print(cuts_under_30)