import re

PATTERN_OR = r'( \|\|(?= ))'
PATTERN_AND = r'( \&\&(?= ))'
n = int(input().strip())

for _ in range(n):
    line = input()
    line = re.sub(PATTERN_AND, " and", line)
    line = re.sub(PATTERN_OR, " or", line)
    print(line)