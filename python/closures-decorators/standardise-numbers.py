import re


def wrapper(f):
    def fun(l):
        for i in range(len(l)):
            string = l[i]
            match = re.fullmatch("\+?((91)|0)?([0-9]{10})", string)
            number = match.groups()[2]
            l[i] = "+91 " + number[0:5] + " " + number[5:]
        return f(l)
    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)