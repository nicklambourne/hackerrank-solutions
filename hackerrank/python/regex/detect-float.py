import re


n = int(input())
for i in range(n):
    s = input()
    if re.fullmatch("[+-]?\d*\.\d+", s):
        print(True)
    else:
        print(False)
