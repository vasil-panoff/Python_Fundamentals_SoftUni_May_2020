quantities_dict = {}
prices_dict = {}

while True:
    input_line = input()
    if input_line == "buy":
        break
    (product, price_str, quantity_str) = input_line.split(" ")
    price = float(price_str)
    quantity = int(quantity_str)

    prices_dict[product] = price

    if product not in quantities_dict:
        quantities_dict[product] = 0
    quantities_dict[product] += quantity

for (key, value) in prices_dict.items():
    total_sum = value * quantities_dict[key]
    print(f"{key} -> {total_sum:.2f}")

