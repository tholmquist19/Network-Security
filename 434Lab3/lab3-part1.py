#!/usr/bin/python3
from prime import *
import math

def main():

    public,private = make_key(int(sys.argv[1]))

    #public key = (n,e)
    print(f"public key is ({public[0]},{public[1]})")

    #private key = (n,d)
    print(f"private key is ({private[0]},{private[1]})")

    #message to encrypt
    msg = b'test,message'
    print (msg)
    print(int.from_bytes(msg))

    #cipher with public key
    x = cipher(msg,public[1],public[0])
    print(x)

    #decipher with private key
    y = dcipher(x, private[1], private[0])
    print(y.to_bytes(len(msg)))


def cipher(m,e,n):
    i = int.from_bytes(m)
    return pow(i,e,n)

def dcipher(c,d,n):
    return pow(c,d,n)
    #FINISH THIS FUNCTION
    
    

"""
FINISH THIS FUNCTION
You'll need a function from prime.py
"""
def make_key(bit_len):
    #pick two prime numbers using bit_len
    p1 = gen_prime(bit_len)
    p2 = gen_prime(bit_len)

    #compute n to be part of public key
    n = p1*p2

    l = math.lcm(p1-1,p2-1)

    #choose number 2<e<l
    #common e = 65537
    #       e = 17
    e = 65537

    #compute d = modular multiplicative inverse(e,l)
    d = modinv(e,l)

    return((n,e),(n,d))

#found this code somewhere
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q,r = b//a,b%a; m,n = x-u*q,y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    return b, x, y

"""
function to find modular multiplicative inverse in RSA
must give e and totient
stole this code too :)
"""
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        return None  # modular inverse does not exist
    else:
        return x % m

if __name__ == "__main__":
    main()
