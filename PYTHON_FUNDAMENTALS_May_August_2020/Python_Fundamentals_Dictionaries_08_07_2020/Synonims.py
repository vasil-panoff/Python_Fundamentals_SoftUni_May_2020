from collections import defaultdict

synonyms = defaultdict(list)

n = int(input())

for _ in range (n):
    word = input()
    synonym = input()
    synonyms[word].append(synonym)

for word, synonyms in synonyms.items():
    normalized_synonyms = ', '.join(synonyms)
    print(f'{word} - {normalized_synonyms}')
