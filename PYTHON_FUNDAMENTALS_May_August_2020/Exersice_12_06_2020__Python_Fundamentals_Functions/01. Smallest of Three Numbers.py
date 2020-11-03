def get_smallest_of_tree_numbers(a,b,c):
    smallest = c

    if a < b and a < c:
        smallest = a
    elif b < a and b < c:
        smallest = b

    return smallest

first_number = int(input())
second_number = int(input())
third_number = int(input())
result = get_smallest_of_tree_numbers(first_number, second_number, third_number)
print(result)