words = input().split(" ")
# 72olle 103doo 100ya
for word in words:
    new_word = ""
    first_letter_ascii = [ch for ch in word if ch.isdigit()]
    left_characters = [ch for ch in word if ch.isalpha()]
    left_characters[0], left_characters[-1] = left_characters[-1], left_characters[0]
    first_letter_ascii = chr(int("".join(first_letter_ascii)))
    new_word += first_letter_ascii + "".join(left_characters)
    print(new_word, end=" ")