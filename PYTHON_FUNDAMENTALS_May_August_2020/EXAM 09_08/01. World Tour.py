input_data = input()

old_string = input_data
new_string = ""
while input_data != "Travel":
    args = input_data.split(":")
    command = args[0]

    if command == "Add Stop":
        index = int(args[1])
        string = args[2]

        new_string = old_string[:index] + string + old_string[index:]
        print(new_string)
    elif command == "Remove Stop":
        index = int(args[1])
        string = int(args[2])

        new_string = new_string[:index] + new_string[string + 1:]
        print(new_string)
    elif command == "Switch":
        index = args[1]
        string = args[2]
        switch_1 = index
        switch_2 = string
        switch = string
        if new_string in old_string:
            switch_1 = switch_2
        print(new_string)

    input_data = input()

print(f"Ready for world tour! Planned stops: {new_string}")