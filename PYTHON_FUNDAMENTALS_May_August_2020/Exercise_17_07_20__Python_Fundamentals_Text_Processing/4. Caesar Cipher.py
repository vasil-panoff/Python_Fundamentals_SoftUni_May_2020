text = input()
result = [chr(ord(x) + 3) for x in text] # LIST COMPREHENTION

print("".join(result))

#      ALT SOLUTION

# for ch in text:
#     print(chr(ord(ch) + 3), end="")