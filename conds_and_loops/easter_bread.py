budget = float(input())
price_flour = float(input())
eggs = 0
change = 0
price_eggs = 0.75 * price_flour
price_milk = (1.25 * price_flour) / 4

price_one_bread = price_flour + price_eggs + price_milk
breads = int(budget // price_one_bread)


for bread in range(1, breads+1):
    eggs += 3
    if bread % 3 == 0:
        eggs -= bread - 2
change = budget - breads*price_one_bread
print(f"You made {breads} loaves of Easter bread! Now you have {eggs} eggs and {change:0.2f}BGN left.")
