import collections

number_of_balls = int(input())
weight = 0
time_needed = 0
quality = 0
list_of_balls = []
dict_balls = {}
sorted_dict = {}
ball_data = ""

for i in range(number_of_balls):
    weight = int(input())
    time_needed = int(input())
    quality = int(input())
    value = int(((weight / time_needed) ** quality))
    ball_data = f"{weight} : {time_needed} = {value} ({quality})"
    dict_balls[value] = ball_data

# sorted(dict_balls.values())
print(sorted(dict_balls.values())[0])

