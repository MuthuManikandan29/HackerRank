# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/swap-case
# Difficulty: Easy 
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================

def swap_case(s): 
    return   s.swapcase()
'''Swaps upper/lower-case letters to lower/upper-case letters'''    
    
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)