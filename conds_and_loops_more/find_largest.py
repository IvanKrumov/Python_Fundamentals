number = input()
list_numbers = []

for i in number:
    list_numbers.append(int(i))

sorted_list = sorted(list_numbers, reverse=True)

for i in sorted_list:
    print(i, end="")




