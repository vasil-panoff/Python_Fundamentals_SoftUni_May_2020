def sum_numbers(a, b):
    res = a + b
    return res


def subtract(a, b):
    res = a - b
    return res

a = int(input())
b = int(input())
c = int(input())


sum = sum_numbers(a, b)
res = subtract(sum, c)
print(res)
