number = int(input())

for i in range(1, number+1):
    digit_sum = 0
    for j in str(i):
        # print(f"digit is {j}")
        digit_sum += int(j)
    if digit_sum == 7 or digit_sum == 5 or digit_sum == 11:
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")

