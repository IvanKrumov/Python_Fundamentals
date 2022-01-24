lines = int(input())
brack_list = []
is_balanced = True

for symbol in range(lines):
    char = input()
    if char == "(" or char == ")":
        brack_list.append(char)

if len(brack_list) % 2 != 0:
    print("UNBALANCED")

else:
    for i in range(int(len(brack_list) / 2)):
        if brack_list[i] == "(" and brack_list[-i - 1] == ")":
            print("BALANCED")
            break
        else:
            print("UNBALANCED")
            break