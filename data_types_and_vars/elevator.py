P = int(input())
N = int(input())

if P % N == 0:
    turns = int(P / N)
    print(turns)
else:
    turns = int(P / N + 1)
    print(turns)