def sumUp(x,i): ## This is stupid, first try and such
    sum=0
    mult=0
    y=0
    while y<=i:
        sum+=y
        y=x*mult
        mult+=1
    else:
        return sum

def gaussSum(m,d): ## This one is gauss's formula for sumation of sequences. 
    m //= d         ## m is the number up to, d is the divisor you want to use
    return d*m*(m+1) //2


if __name__ == "__main__":
    print(sumUp(5,999)+sumUp(3,999)-sumUp(5*3,999)) ## sum up to 999 and sub the multiples of 15
    print(sum(x for x in range(1000) if (x % 3 == 0 or x % 5 == 0)))    ##This is the one liner for it, with list comprehensions
    s = 0
    for i in range(1, 1000):
        if i%3==0 or i%5==0: s+= i
    print (s)
    print(gaussSum(999,5)+gaussSum(999,3)-gaussSum(999,15)) ## This one scales quite well if you need to.

#233168
#233168
#233168
#233168