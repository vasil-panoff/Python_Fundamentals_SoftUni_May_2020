# def perform_operations (a, b, operation):
#     if operation == "add":
#         return a + b
#     if operation == "subtract":
#         return a - b
#     if operation == "divide":
#         return a / b
#     if operation == "multyply":
#         return a * b
#
# operation = input()
# a = int(input())
# b = int(input())
# print(perform_operations (a, b, operation))

import operator

operation = input()
a = int(input())
b = int(input())

def perform_operations (a, b, operation):
    operator_fn = None

    if operation == "add":
        operator_fn = operator.add
    elif operation == "subtract":
        operator_fn = operator.sub
    elif operation == "divide":
        operator_fn = operator.truediv
    elif operation == "multyply":
        operator_fn = operator.mul

    return operator_fn(a,b)

print(perform_operations (a, b, operation))