import math

def digitalSum(x):
    i = str(x)
    lpl=len(i)-1
    sumtotal = 0
    while lpl>-1:
        sumtotal+=int(i[lpl])
        lpl-=1
    return sumtotal

for i in range(4, 10000):
    if digitalSum(i**2)==digitalSum(i**4) and i%10!=0:
            print(i)
