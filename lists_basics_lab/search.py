lines = int(input())
word = input()
my_list = []
temp_list = []

for i in range(1, lines+1):
    string = input()
    temp_list.append(string)
    if word in string:
        my_list.append(string)

print(temp_list)
print(my_list)




