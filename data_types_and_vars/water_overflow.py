num = int(input())
litters = 0
sum_litters = 0


for _ in range(num):
    litters = int(input())
    if litters > 255:
        print("Insufficient capacity!")
        break
    sum_litters += litters
    if sum_litters > 255:
        print("Insufficient capacity!")
        sum_litters -= litters
print(sum_litters)
