number = int(input())
is_prime = False

for i in range(2, number+1):
    if number % i == 0:
        print(is_prime)
        break
    else:
        print(not is_prime)
        break