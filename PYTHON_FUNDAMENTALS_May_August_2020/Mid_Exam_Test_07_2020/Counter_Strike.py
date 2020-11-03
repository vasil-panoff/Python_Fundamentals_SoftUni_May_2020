initial_energy = int(input())
distance = 0
left_energy = 0
battle_count = 0
list = []

while True:
    command = input()

    list = []
    list.append(command)
    battle_count = len(list)

    if command == "End of battle":
        break
    elif command != "End of battle":
        distance = int(command)
        left_energy = initial_energy - distance


if left_energy < 0:
    print(f"Not enough energy! Game ends with {battle_count} won battles and {left_energy} energy")
else:
    print(f"Won battles: {battle_count}. Energy left: {left_energy}")



