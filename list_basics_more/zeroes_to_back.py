nums = input().split(', ')
copy_nums = list(map(int, nums))
new_list = []
zeroes = []

for num in copy_nums:
    if num != 0:
        new_list.append(num)
    else:
        zeroes.append(num)

print(new_list+zeroes)
