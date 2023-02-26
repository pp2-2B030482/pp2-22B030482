import re

pattern = r'a[b]{2,3}'

string = input()

match = re.search(pattern, string)

if match:
    print('yes: ', match.group())
else:
    print('no(-_-)')
