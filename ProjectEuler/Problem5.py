import math
##Smallest number evenly divisible by all numbers from 1 to 20
##232792560
for i in range(3628800,300000000,2520):
    k=0
    for j in range(11,21):
        if i%j==0:
            k+=1
            if k>=10:
                print(i)
        else:
            break
