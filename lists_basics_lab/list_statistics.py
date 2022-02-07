lines = int(input())
list_pos = []
list_neg = []

for i in range(1, lines+1):
    number = int(input())
    if number >=0:
        list_pos.append(number)
    else:
        list_neg.append(number)

print(list_pos)
print(list_neg)
print(f"Count of positives: {len(list_pos)}")
print(f"Sum of negatives: {sum(list_neg)}")