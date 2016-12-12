import math
from math import sqrt

def primes(limit): ##Code for the sieve
    limitn = limit+1
    not_prime = [False] * limitn
    primes = []

    for i in range(2, limitn):
        if not_prime[i]:
            continue
        for f in tange(i*2, limitn, i):
            not_prime[f] = True

        primes.append(i)

    return primes

lsp = primes(775146) ##Only need to check up to the
for i in lsp:        ##Root of the number in question
    if (600851475143%i==0):
        print(i)

##71
##839
##1471
##6857
