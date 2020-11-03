def get_characters_in_range(start, end):
    sum = 0
    for i in range (ord(start), ord(end) - 1):
        sum = i + 1

        print (chr(sum), end=" ")


start = input()
end = input()
get_characters_in_range(start, end)
