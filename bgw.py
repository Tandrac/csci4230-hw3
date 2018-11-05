import math


def blumGEnc(m,p,q,x0):
    #work required by bgw
    n=p*q
    k = int(math.log(n,2))
    h = int(math.log(k,2))
    t = len(m)//h


    mi = [m[i*h:i*h+h] for i in range(t+1)]

    c = []

    for m in mi:
        x0 = (x0**2)%n

        #go h elements from the end, then traverse towards the end, getting the least bitmask
        #then turn it to a binary string, then a string
        b = str(bin(x0))[-h:]

        for i in range(len(m)):
            #xor plaintext with keystream
            if(b[i] != str(m[i])):
                c.append(1)
            else:
                c.append(0)
    return c,x0

#method for gcd, taken from https://stackoverflow.com/questions/11175131/code-for-greatest-common-divisor-in-python

def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


def blumGDec(m,p,q,a,b,x):
    #following algorithm
    n=p*q
    k = int(math.log(n,2))
    h = int(math.log(k,2))
    t = len(m)//h


    #these numbers got too large with regular exponetials and modding, had to use pow function
    #does this mean I have to change it for enc?
    d1 = pow(((p+1)//4), t+1, p-1)
    d2 = pow(((q+1)//4), t+1, q-1)
    u = pow(x, d1, p)
    v = pow(x, d2, q)

    x0 = (v*a*p + u*b*q) % n
    #same as enc
    mts = [m[i*h:i*h+h] for i in range(t+1)]
    c = []
    for m in mts:
        x0 = (x0**2)%n
        #go h elements from the end, then traverse towards the end, getting the least bitmask
        #then turn it to a binary string, then a string
        b = str(bin(x0))[-h:]
        for i in range(len(m)):
            #xor plaintext with keystream
            if(b[i] != str(m[i])):
                c.append(1)
            else:
                c.append(0)
    return c

def main():
    m=[1,0,0,1,1,1,0,0,0,0,0,1,0,0,0,0,1,1,0,0]
    p=499
    q=547
    x0=159201
    a=-57
    b=52
    print("m is: ", m)
    enc,x0 = blumGEnc(m,p,q,x0)
    print("enc is:", enc)
    dec = blumGDec(enc,p,q,a,b,x0)
    print("dec is: ", dec)
    if(m == dec):
        print("Succes, m and dec are the same!")
    
if __name__ == "__main__":
    main()
