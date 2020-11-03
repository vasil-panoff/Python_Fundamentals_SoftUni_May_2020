text = input()

occurences = {}

for ch in text:
    if ch == ' ':
        continue

    if ch in occurences:
        occurences[ch] += 1
    else:
        occurences[ch] = 1
for key, value in occurences.items():
    print(f'{key} -> {value}')