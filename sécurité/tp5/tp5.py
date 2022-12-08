from Crypto.Util.number import getPrime, inverse
from math import gcd
from time import time
from random import randint

q = getPrime(512)
p = getPrime(512)
n = p * q
e = 65537
gcd(e, p-1)
gcd(e, q-1)
d = inverse(e, (p-1) - (q-1)) 
m = randint(0,e)

def time_rsa():
    begin = time()
    for s in range(1000):
        s = pow(m, d, n)
    end = time()
    return end - begin
    
print(time_rsa())

#qst3
dp = d % (p-1)
dq = d % (q-1)
iq = inverse(q,p)

def time_rsa_crt():
    begin = time()
    for scrt in range(1000):
        sp = pow(m, dp, p)
        sq = pow(m, dq, q)
        scrt = sq + q * (iq * (sp - sq) % p)
    end = time()
    return end - begin

print(time_rsa_crt())

#-----------------------------------------------------------------------------------

'''
EXERCICE 2:
'''

def attack():
    e =17
    N = 47775493106113804140 
    s = 4539922961076506169
    sf =  6262353196915623338
    q = gcd(N,s-sf)
    p = n//q
    phe_n = (p-1) * (q-1)
    d = inverse(e,phe_n)
    print(" q, p, d ",q,p,d)
    print("La clé privée",(p,q,dp,dq,iq))