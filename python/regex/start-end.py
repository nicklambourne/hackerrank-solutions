import re


string = input()
pattern = input()
indices = set()

for i in range(len(string)):
    match = re.search(pattern, string[i:])
    if match:
        indices.add((i + match.start(), i + match.end() - 1))

if len(indices) > 0:
    for m in sorted(indices):
        print(tuple(m))
else:
    print((-1, -1))