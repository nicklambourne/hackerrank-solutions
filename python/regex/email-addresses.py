import re
import email.utils


PATTERN = '[A-Za-z][\w\-\.\_]*@[A-Za-z]+\.[A-Za-z]{1,3}'

n = int(input().strip())

for _ in range(n):
    name, address = email.utils.parseaddr(input())
    if name and address and re.fullmatch(PATTERN, address):
        print(name, '<' + address + '>')
