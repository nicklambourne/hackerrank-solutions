import re


regex = '(7|8|9)[0-9]{9}'

n = int(input().strip())

for i in range(n):
    inp = input()
    if re.fullmatch(regex, inp):
        print('YES')
    else:
        print('NO')