rooms = input().split("|")

for room i range(len(rooms)):
    room = rooms[i]
    args = room.split()
    command = args[0]
    number = int(args[1])

    if command == "potion":
        temp = health
        health += number
        health = number
    elif command == "chest":
        total_bitcoins += number
        print(f"Yoy found {number} bitcoins.")
    else:
        health -= number

        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {i + 1}")
            break

