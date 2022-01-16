orders = int(input())
total_price = 0

for i in range(1, orders+1):
    price = float(input())
    days = int(input())
    capsules = int(input())
    total = price * days * capsules
    total_price += total
    print(f"The price for the coffee is: ${total:0.2f}")
# print(total)
print(f"Total: ${total_price:0.2f}")
