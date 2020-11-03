def repeat_lenth(word):
    return word * len(word)

words = input().split(' ')
print(''.join(map(repeat_lenth, words)))