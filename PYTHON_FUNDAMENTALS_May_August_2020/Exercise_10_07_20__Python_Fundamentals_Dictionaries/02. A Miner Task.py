product = input()

products = {}

while product != 'stop':
    quantuty = int(input())

    if product not in products:
        products[product] = 0

    products[product] += quantuty

    product = input()

for key, value in products.items():
    print(f'{key} -> {value}')
