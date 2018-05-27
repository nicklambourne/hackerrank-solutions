"""
M = 1000
D = 500
C = 100
L = 50
X = 10
V = 5
I = 1
"""

regex_pattern = r"^M{0,3}((CM)|((CD)|D?(C{0,3})))((XC)|((XL)|(L?(X{0,3}))))((IX)|((IV)|(V?I{0,3})))$"

import re
print(str(bool(re.match(regex_pattern, input()))))