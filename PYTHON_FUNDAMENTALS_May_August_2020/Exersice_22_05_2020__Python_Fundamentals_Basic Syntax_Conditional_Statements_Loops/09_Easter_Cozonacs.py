budget = float(input())
flour_price = float(input())

eggs_pack_price = flour_price * 0.75
milk_one_liter_price = flour_price * 1.25
milk_price = milk_one_liter_price / 4

cozonac_price = eggs_pack_price + milk_price + flour_price
cozonacs_made = 0
coloured_eggs = 0

while budget >= cozonac_price:
    cozonacs_made += 1
    coloured_eggs += 3

    if cozonacs_made % 3 == 0:
        coloured_eggs -= cozonacs_made - 2

    budget -= cozonac_price

print(f"You made {cozonacs_made} cozonacs! Now you have {coloured_eggs} eggs and {budget:.2f}BGN left.")
