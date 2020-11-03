list = ['fish', 'cat', 'dog']

for i in range(len(list)):
    print (list[i])

for i, v in enumerate(list):
    print(f'index = {i}, value = {v}')

while len(list) > 0:
    print (list.pop(0))

while len(list) > 0:
    e = list.pop(0)
    print (e)