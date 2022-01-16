quantity = int(input())
days = int(input())
sum_money = 0
spirit = 0

for i in range(days):
    if days % 2 == 0:
        sum_money += quantity * 2
        spirit += 5
    if days % 3 == 0:
        sum_money += quantity*(3*5 + 3*3)
        spirit += 13
print(sum_money)
print(spirit)
