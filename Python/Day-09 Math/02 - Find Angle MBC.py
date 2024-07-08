# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/find-angle/problem
# Difficulty: Medium
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================

from math import degrees, atan

AB = int(input())
BC = int(input())

RESULT = round(degrees(atan(AB/BC)))
print(RESULT, chr(176), sep = '')