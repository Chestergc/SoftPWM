import math

def concat(x,y,b):
    return x*(b**(math.floor(math.log(y,b))+1))+y

if __name__=="__main__":
    print(concat(20,987,10))
