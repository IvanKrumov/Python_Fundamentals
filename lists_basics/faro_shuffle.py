card_string = input()
shuffles_count = int(input())
new_list = []
first = []
second = []
card_list = card_string.split()
count_cards = len(card_list)
count_cards_half = int(len(card_list)/2)


for k in range(count_cards_half):
    first.append(card_list[k])

for j in range(count_cards_half, count_cards):
    second.append(card_list[j])

for i in range(count_cards_half):
    new_list.append(first[i])
    new_list.append(second[i])

print(new_list)



