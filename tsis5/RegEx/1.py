import re

string = input("")

if re.search(r'a[b]*', string):
    print("yes")
else:
    print("no")
