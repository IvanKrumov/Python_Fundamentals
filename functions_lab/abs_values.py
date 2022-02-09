def abs_value_func(list_values):
    new_list = list()
    for n in list_values:
        abs_value = abs(float(n))
        new_list.append(abs_value)
    return new_list


input_list = input().split(" ")
print(abs_value_func(input_list))





# input_list = input().split(" ")
# abs_list = list()
#
# for n in input_list:
#     current_abs = abs(float(n))
#     abs_list.append(current_abs)
#
# print(abs_list)