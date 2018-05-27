import re


pattern = '(#[a-fA-F\d]{6}|#[a-fA-F\d]{3})'

n = int(input().strip())

for _ in range(n):
    inp = input()
    if ':' in inp:
        matches = re.findall(pattern, inp)
        for hex in matches:
            print(hex)