#!/bin/python3

import math
import os
import random
import re
import sys

pairs = {
    '}': '{',
    ']': '[',
    ')': '(',
}


def evaluate_brackets(expression):
    stack = []
    chars = list(expression)
    for char in chars:
        if char in ['{', '[', '(']:
            stack.append(char)
        elif char in ['}', ']', ')']:
            if len(stack) > 0 and pairs[char] == stack[-1]:
                stack = stack[:-1]
            else:
                return 'NO'
    if len(stack) == 0:
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        expression = input()
        print(evaluate_brackets(expression))


