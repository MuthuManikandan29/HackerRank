# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================

n = int(input())
s = set(map(int, input().split()))  # Set of n elements

for i in range(int(input())):  # Iterate in range of the number of commands
    s1 = input().split()
    if s1[0] == 'pop':
        if s:  # Check if the set is not empty
            s.pop()
    elif s1[0] == 'remove':
        if int(s1[1]) in s:  # Check if the element exists in the set
            s.remove(int(s1[1]))
    elif s1[0] == 'discard':
        s.discard(int(s1[1]))

print(sum(s))
