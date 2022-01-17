list = input()
herd = list.split(", ")
number_of_animals = len(herd)


for animal in herd:
    if herd[-1] == "wolf":
        print("Please go away and stop eating my sheep")
    else:
        print(f"Oi! Sheep number {number_of_animals -1}! You are about to be eaten by a wolf!")

