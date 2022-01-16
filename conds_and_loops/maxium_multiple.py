# My solution

# divisor = int(input())
# boundary = int(input())
# list = []

# for i in range(boundary+1):
#     if 0 < i <= boundary:
#         if i % divisor == 0:
#             list.append(i)
# print(list[-1])


# Official solution

divisor = int(input())
boundary = int(input())

result = int(boundary/divisor) * divisor
# result = (boundary//divisor) * divisor

print(result)
