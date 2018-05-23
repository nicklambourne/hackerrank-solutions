string = input()

upper = []
lower = []
odd = []
even = []

chars = list(string)

for char in chars:
    if char.isupper():
        upper.append(char)
    elif char.islower():
        lower.append(char)
    elif int(char) % 2 == 0:
        even.append(char)
    else:
        odd.append(char)

ret = ''.join(sorted(lower) + sorted(upper) + sorted(odd) + sorted(even))

print(ret)