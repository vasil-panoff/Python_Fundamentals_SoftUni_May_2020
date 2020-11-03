import re

regex = r'(www\.)([a-zA-Z]{1,}?\-?[0-9[a-zA-Z]{1,})(\.[a-z]{1,})'

www_pattern = r"www\."
domain_pattern = r"[a-zA-Z]{1,}?\-?[0-9[a-zA-Z]{1,}"
ext_pattern = r"\.[a-z]{1,}"
pattern = fr"{www_pattern}{domain_pattern}{ext_pattern}"

while True: #multiline user input
    line = input()
    if not line:
        break
    matches = re.findall(pattern, line)
    for match in matches:
        print("".join(match))