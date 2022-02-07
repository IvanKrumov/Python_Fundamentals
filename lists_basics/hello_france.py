clothes = input().split('|')
budget = int(input())
total_spent = 0
profit = 0
condition = False
wallet = budget
list_prices = []

for cloth in clothes:
    cloth_info = cloth.split('->')
    type_of_cloth = cloth_info[0]
    value_of_cloth = float(cloth_info[1])
    condition = False

    if type_of_cloth == 'Clothes':
        if value_of_cloth <= 50:
            condition = True
    elif type_of_cloth == 'Shoes':
        if value_of_cloth <= 35:
            condition = True
    elif type_of_cloth == 'Accessories':
        if value_of_cloth <= 20.50:
            condition = True

    if condition:
        if wallet > value_of_cloth:
            wallet -= value_of_cloth
            total_spent += value_of_cloth
            new_cloth_price = value_of_cloth * 1.4
            list_prices.append(f'{new_cloth_price:.2f}')

total_profit = (total_spent * 1.4) - budget + wallet
profit = total_spent * 1.4
print(profit+wallet)

print(' '.join(list_prices))
print(f'Profit: {total_profit:.2f}')

if (wallet + profit) >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')
