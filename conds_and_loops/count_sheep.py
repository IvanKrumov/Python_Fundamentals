number_sheeps = int(input())

if number_sheeps == 1:
    print(f"{number_sheeps} sheep...")
else:
    for i in range(1, number_sheeps + 1):
        print(f"{i} sheep...", end="")
