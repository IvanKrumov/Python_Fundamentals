import re

word = input()
count = 0

word_lower = word.lower()

count = 0
beach = ['fish', 'sun', 'sand', 'water']
for pattern in beach:
    for match in re.finditer(pattern, word_lower):
        count += 1
print(count)
