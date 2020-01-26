import re

PATTERN_16 = r'[456][\d]{3}(-?[\d]{4}){3}'
PATTERN_REP = r'([0-9])(-?\1){3}'
n = int(input().strip())

for _ in range(n):
    number = input()
    if re.fullmatch(PATTERN_16, number) and not re.search(PATTERN_REP, number):
        print('Valid')
    else:
        print('Invalid')
