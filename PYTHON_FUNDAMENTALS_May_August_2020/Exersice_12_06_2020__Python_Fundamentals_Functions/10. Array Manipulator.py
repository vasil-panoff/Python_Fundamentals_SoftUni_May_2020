items = input().split()
numbers = []

for item in items:
    numbers.append(int(item))


command_input = input()

while command_input != "end":
    tokens = command_input.split()
    comnand = tokens[0]

    if comnand == "excahnge":
        index = int(tokens)
    elif comnand == "max":
        pass
    elif comnand == "min":
        pass
    elif comnand == "first":
        pass
    elif comnand == "last":
        pass

