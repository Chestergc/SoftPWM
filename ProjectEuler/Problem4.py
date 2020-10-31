import math

def palindrome(x):
    return max(i*j for i in range(x) for j in range(x)
                if str(i*j) == str(i*j)[::-1])

print(palindrome(1000))

## Unfortuntately doesn't scale very well. Should look into it.
## The funcion actually means: Return the maximum value of the product 
## of two numbers such that the number itself reads the same as it's mirror (hence the [::-1])
## 906609