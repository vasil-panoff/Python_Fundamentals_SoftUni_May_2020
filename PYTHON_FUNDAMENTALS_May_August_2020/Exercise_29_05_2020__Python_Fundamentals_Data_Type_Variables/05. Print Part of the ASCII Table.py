start = int(input())
end = int(input())

result = ''
for i in range (start, end + 1):
    result += chr(i) + ' '  #" " поставя спейс след всеки знак

print(result)  #print(chr(i), end= " " end - остани на същия ред със спейс