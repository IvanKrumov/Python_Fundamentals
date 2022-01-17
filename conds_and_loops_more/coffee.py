word = input()
events = ['cat', 'dog', 'coding', 'movie']
capital_events = ['CAT', 'DOG', 'CODING', 'MOVIE']
count = 0

while word != "END":

    if word in events:
        count += 1
    if word in capital_events:
        count += 2
    word = input()

if count >= 5:
    print("You need extra sleep")
else:
    print(count)
