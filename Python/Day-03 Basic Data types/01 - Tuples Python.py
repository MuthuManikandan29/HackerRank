
# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/python-tuples
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================


n = int(input())
integer_list = map(int, input().split())
integer_tuple = (tuple(integer_list))
print(hash(integer_tuple))
