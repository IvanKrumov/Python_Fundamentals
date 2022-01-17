word = input()
list_index = []

for i in range(len(word)):
    if word[i].isupper():
        list_index.append(i)
print(list_index)
