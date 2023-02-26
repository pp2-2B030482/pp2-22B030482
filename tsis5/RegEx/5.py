import re

pattern = r'a.*b$'

string = input()

match = re.search(pattern, string)

if match:
    print('yes: ', match.group())
else:
    print('no')
