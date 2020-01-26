import re


LENGTH = r'[A-Za-z0-9]{10}'
UPPER = r'[A-Z]'  # Length match >= 2
DIGIT = r'[0-9]'  # Length match >= 3
REPEAT = r'([A-Za-z0-9])[A-Za-z0-9]*\1'  # Match any repeat

n = int(input().strip())
for _ in range(n):
    string = input()
    if re.fullmatch(LENGTH, string) and len(re.findall(UPPER, string)) >= 2 and len(re.findall(DIGIT, string)) >= 3 and not re.findall(REPEAT, string):
        print('Valid')
    else:
        print('Invalid')