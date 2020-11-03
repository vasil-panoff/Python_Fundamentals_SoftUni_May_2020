import re

regex = r"(@|#)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1"

data = input()
mirror_words = []

match = re.findall(regex, data)

for m in match:
    first_word = m[1]
    second_word = m[2]
    if first_word == second_word[::-1]:
        mirror_words.append(first_word + " <=> " + second_word)

if len(match) == 0:
    print("No word pairs found!")
else:
    print(f"{len(match)} word pairs found!")

if len(mirror_words) == 0:
    print("No mirror words!")
else:
    print(f"The mirror words are:")
    print(", ".join(mirror_words))
