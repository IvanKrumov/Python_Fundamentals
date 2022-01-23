import collections

number_of_balls = int(input())
dict_balls = {}
ball_data = ""

for i in range(1, number_of_balls+1):
    weight = int(input())
    time_needed = int(input())
    quality = int(input())
    value = int((weight / time_needed) ** quality)
    ball_data = f'{weight} : {time_needed} = {value} ({quality})'
    dict_balls[value] = ball_data

# sorted(dict_balls.values())
od = collections.OrderedDict(sorted(dict_balls.items(), reverse=True))
first_value = list(od.values())[0]
print(first_value)

