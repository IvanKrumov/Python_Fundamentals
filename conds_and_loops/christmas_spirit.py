quantity = int(input())
days = int(input())
sum_money = 0
spirit = 0

for i in range(1, days + 1):

    if i % 11 == 0:
        quantity += 2

    if i % 2 == 0:
        sum_money += quantity * 2
        spirit += 5

    if i % 3 == 0:
        sum_money += quantity * (5 + 3)
        spirit += 13

    if i % 5 == 0:
        sum_money += 15 * quantity
        spirit += 17

    if i % 5 == 0 and i % 3 == 0:
        spirit += 30

    if i % 10 == 0:
        spirit -= 20
        sum_money += 15 + 5+3

    if i == days and i % 10 == 0:
        spirit -= 30

print(f"Total cost: {sum_money}")
print(f"Total spirit: {spirit}")
