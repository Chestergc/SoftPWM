def primes(limit):      ##code based on the sieve of
    limitn = limit+1    ##Eratosthenes, generates an arbitrary sized list of primes.
    not_prime = [False] * limitn
    primes = []

    for i in range(2, limitn):
        if not_prime[i]:
            continue
        for f in range(i*2, limitn, i):
            not_prime[f] = True

        primes.append(i)
    return primes

lsp = primes(1000000) ##saves the list to memory
index = [i, dor i in range(1000000)] ##creates an index of natural numbers up to the list size
order = dict(zip(index, lsp)) ##creates a dictionary with the list and the index
order[10000] ##find the ten thousandth entry in the dictionary and prints it.

##Output = 104743
