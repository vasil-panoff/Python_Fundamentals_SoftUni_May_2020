n = int(input())
pieces = {}
for i in range(n):
    data = input().split("|")
    pieces[data[0]] = [data[1], data[2]]
while True:
    command = input()
    if command == 'Stop':
        break
    args = command.split('|')
    event = args[0]
    if event == 'Add':
        piece = args[1]
        if piece in pieces:
            print(f"{piece} is already in the collection!")
            continue
        composer = args[2]
        key = args[3]
        pieces[piece] = [composer, key]
        print(f"{piece} by {composer} in {key} added to the collection!")
    elif event == 'Remove':
        piece = args[1]
        if piece not in pieces:
            print(f"Invalid operation! {piece} does not exist in the collection.")
            continue
        del pieces[piece]
        print(f"Successfully removed {piece}!")
    elif event == 'ChangeKey':
        piece = args[1]
        if piece not in pieces:
            print(f"Invalid operation! {piece} does not exist in the collection.")
            continue
        new_key = args[2]
        pieces[piece][1] = new_key
        print(f"Changed the key of {piece} to {new_key}!")

for key, values in sorted(pieces.items(), key=lambda z: (z[0], z[1][0])):
    print(f"{key} -> Composer: {values[0]}, Key: {values[1]}")