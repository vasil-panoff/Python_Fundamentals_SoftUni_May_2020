data = input()
elements = data.split(' ')

products = {}

for index in range (0, len(elements), 2):
    product_name = elements[index]
    product_quantity = elements [index + 1]
    products[product_name] = int(product_quantity)

# products = {
#     elements[index]: int(elements[index + 1])
#     for index in range(0, len(elements), 2)
# }


# alternative solution:

# elements = input().split(" ")
# bakery = {}  # bakery = dict()
# for i in range(0, len(elements), 2):
#     key = elements[i]
#     value = elements[i + 1]
#     bakery[key] = int(value)
# print(bakery)


print(products)

