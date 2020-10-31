import math

def fibgen(n): 
    """
    Return the nth number of the fibonacci sequence
    """
    return round((1/math.sqrt(5))*((1+math.sqrt(5))/2)**(n+1))

def listgen():
    """
    Return a list of numbers to be summed
    """
    lst=[]
    x=1
    while fibgen(x)<=4000000:
        if fibgen(x)%2==0:
            lst.append(fibgen(x))
            x+=1
        else:
            x+=1
            continue
    return lst

toSum=listgen()
print(sum(toSum))