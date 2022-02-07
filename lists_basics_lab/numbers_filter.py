n = int(input())
list_numbers = []
list_even = []
list_odd = []
list_negative = []
list_positive = []

for i in range(n):
    number = int(input())
    list_numbers.append(number)

command = input()

if command == "even":
    for i in list_numbers:
        if i % 2 == 0:
            list_even.append(i)
    print(list_even)


if command == "odd":
    for i in list_numbers:
        if i % 2 != 0:
            list_odd.append(i)
    print(list_odd)

if command == "negative":
    for i in list_numbers:
        if i < 0:
            list_negative.append(i)
    print(list_negative)

if command == "positive":
    for i in list_numbers:
        if i >= 0:
            list_positive.append(i)
    print(list_positive)

