import math
##Smallest number evenly divisible by all numbers from 1 to 20
##232792560
res=[i for i in range(1,300000000)if i%2==0 and i%10==0]
fac=[i for i in range(11,21)]

#print(len(res))

for i in res:
    k=0
    for j in fac:
        if i%j==0:
            k+=1
            if k>=10:
                print(i)
