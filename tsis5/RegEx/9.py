import re

def insert_spaces(text):
    words = re.findall('[A-Z][a-z]*', text)
    return ' '.join(words)

text = input()
result = insert_spaces(text)
print(result)
