lines = int(input())
brack_list = []

for symbol in range(lines):
    char = input()
    if char == "(" or char == ")":
        brack_list.append(char)

for i in range(int(len(brack_list) / 2)):
    if len(brack_list) % 2 != 0:
        print("UNBALANCED")
        break
    if brack_list[i] == "(" and brack_list[-i - 1] == ")":
        print("BALANCED")
    else:
        print("UNBALANCED")
