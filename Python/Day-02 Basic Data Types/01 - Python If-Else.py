# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/py-if-else
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================

if __name__ == '__main__':
    n = int(input().strip())

    if n % 2 != 0:
        print('Weird')
    elif n % 2 == 0:
        if 2 <= n <= 5:
            print("Not Weird")
        elif 6 <= n <= 20:
            print("Weird")
        elif n > 20:
            print("Not Weird")