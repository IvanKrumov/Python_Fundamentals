events = input().split('|')
energy = 100
coins = 100
event_counter = 0
close = False

for event in events:
    event_info = event.split('-')
    event_type = event_info[0]
    event_value = int(event_info[1])

    if event_type == 'rest':
        if energy < 100:
            energy += event_value
            print(f'You gained {event_value} energy.')
        else:
            print('You gained 0 energy.')
        print(f'Current energy: {energy}.')
        event_counter += 1
    elif event_type == 'order':
        if energy >= 30:
            energy -= 30
            coins += event_value
            print(f'You earned {event_value} coins.')
            event_counter += 1
        else:
            energy += 50
            print('You had to rest!')
    else:
        if coins < event_value:
            print(f'Closed! Cannot afford {event_type}.')
            event_counter += 1
            close = True
            break
        else:
            coins -= event_value
            print(f'You bought {event_type}.')


if not close:
    print('Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')

