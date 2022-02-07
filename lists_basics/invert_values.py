txt = input()               # nums = input().split(' ')
list_numbers = []
x = txt.split()

for i in x:
    number = int(i)
    list_numbers.append(-number)

print(list_numbers)

# nums = [-num if num > 0 else abs(num) for num in list(map(int, input().split(' ')))]          # how map() works?
# print(nums)

