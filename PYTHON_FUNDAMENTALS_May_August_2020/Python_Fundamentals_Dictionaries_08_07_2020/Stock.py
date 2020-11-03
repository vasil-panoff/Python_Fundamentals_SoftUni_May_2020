elements = input().split(" ")
stock = {}
# Fill in the products in the dictionary
searched_products = input().split(" ")
for product in searched_products:
    if product in stock:
        print(f"We have {stock[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")

# data = input()
# elements = data.split(' ')
# products = {
#     elements[index]: int(elements[index + 1])
#     for index in range(0, len(elements), 2)
# }
