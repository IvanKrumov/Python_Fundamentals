def odd_even_sum(some_list):
    sum_even = 0
    sum_odd = 0
    for i in some_list:
        if i % 2 == 0:
            sum_even += i
        else:
            sum_odd += i

    print(f"Odd sum = {sum_odd}, Even sum = {sum_even}")


number = input()
some_list = map(int, number)
odd_even_sum(some_list)
