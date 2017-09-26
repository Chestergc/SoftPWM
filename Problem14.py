import math
import time
## The collatz conjecture goes as such:
## given a number n
## if N is even then n=n/2
## if N is odd then n=3n+1
## Given those rules, what is the number that
## generates the longest chain below 1000000

def even(x):
    x=x/2
    return x

def odd(x):
    x=3*x+1
    return x

start=time.time()
st=1000000
lst=[i for i in range(1,st)]
res=[0]

for i in lst:
    ctr=1
    while i!=1:
        ctr+=1
        if i%2==0:
            i=even(i)
        elif i%2!=0:
            i=odd(i)
    res.append(ctr)

index=[i for i in range(st)]
result=dict(zip(index,res))
getmax=max(result.keys(), key=(lambda key: result[key]))
elapsed=(time.time()-start)
print("Fount the number %s with %s steps in %s seconds" % (getmax, result[getmax],elapsed))

#This is slow. Am sad. Will try to optimize later on. Take away the damn dict for a start.
