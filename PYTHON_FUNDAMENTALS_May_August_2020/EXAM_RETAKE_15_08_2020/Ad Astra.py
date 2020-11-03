import re

regex = r"(\\||#)(?<item>[A-Za-z\\s]+)\\1(?<expiration>[\\d]{2}\\/[\\d]{2}\\/[\\d]{2})\\1(?<calories>[\\d]+)\\1"

string = input()

match = re.match(regex, string)

total_calories = 0
total_calories += match[0]
days = 0

if total_calories == 0:
    print(f"You have food to last yoy for: {days}")

