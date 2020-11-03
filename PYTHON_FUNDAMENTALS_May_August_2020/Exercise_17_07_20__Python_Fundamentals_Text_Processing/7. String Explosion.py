line = input()
total_strenght = 0

i = 0
while i < len(line):
    ch = line[i]

    if ch == ">":
        strength = int(line[i + 1])
        total_strenght += strength
    else:
        # abv>1>1>2>2asdasd
        if total_strenght > 0:
            line = line[:i] + line[i + 1:]
            i -= 1
            total_strenght -= 1

    i += 1

print(line)