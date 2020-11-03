import re

pattern = r">>([a-zA-Z]+)<<([0-9]+(\.[0-9]+)?)!([0-9]+)"

text = input()

print("Bought furniture:")
total_money = 0

while text != "Purchase":
    match = re.fullmatch(pattern, text)

    if match is None:
        text = input()
        continue

    print(match[1])
    price = float(match[2])
    quantity = int(match[4])
    total_money += price * quantity

    text = input()

print(f"Total money spend: {total_money:.2f}")