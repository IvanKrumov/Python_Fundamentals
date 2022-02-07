refer_notes = input()
refer_list = refer_notes.split()
players_out = set(refer_list)
refer_list = list(players_out)
counter_A = 11
counter_B = 11
terminated = False


for player in players_out:

    if player[0] == 'A':
        counter_A -= 1
    if player[0] == 'B':
        counter_B -= 1
    if counter_A < 7 or counter_B < 7:
        terminated = True
        break

print(f'Team A - {counter_A}; Team B - {counter_B}')

if terminated:
    print("Game was terminated")

