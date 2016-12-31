import math

def palindrome(x):
    return max(i*j for i in range(x) for j in range(x)
                if str(i*j) == str(i*j)[::-1])

print(palindrome(1000))                
