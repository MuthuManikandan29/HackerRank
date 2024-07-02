# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/python-string-split-and-join
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================


def split_and_join(line):
    a=line.split()
    b="-".join(a)
    return(b)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)