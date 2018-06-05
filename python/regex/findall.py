import re


PATTERN = r'(?:[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]{1})([AEIOUaeiou]{2,})(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]{1})'

def get_substrings(string):
    matches = re.findall(PATTERN, string)
    if len(matches) == 0:
        return [-1, ]
    else:
        return matches


try:
    string = input()
    substrings = get_substrings(string)
    for match in substrings:
        print(match)
except EOFError:
    print(-1)