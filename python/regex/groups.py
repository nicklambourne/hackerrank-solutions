import re


PATTERN = r'([A-Za-z0-9])\1'
string = input()
matches = re.search(PATTERN, string)
if matches:
    print(matches.groups()[0])
else:
    print(-1)

