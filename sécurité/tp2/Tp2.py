from Crypto.Util.number import getPrime
from Crypto.Util.number import inverse
from math import gcd
import sys
import hashlib

def gen_rsa_key_pair(bits) :
	p = getPrime(int(bits/2))
	q = getPrime(int(bits/2))
	n = p * q
	phi_n = (p-1)*(q-1)
	e = 65537
	assert(gcd(e, phi_n) == 1)
	d = inverse(e, phi_n)
	return ((e,n) , (d,n))


def rsa(m, cle) :
	return pow(m, cle[0], cle[1])


def rsa_enc(message,cle) :
	b = int.from_bytes(message.encode('utf-8'),'big')
	return rsa(b, cle)

def rsa_dec(chiffre,cle) :
	m =rsa(chiffre,cle)
	return m.to_bytes((m.bit_length() + 7) // 8, 'big').decode('utf-8')


def h(entier):
    message = hashlib.sha256(entier.encode('utf-8')).hexdigest()
    return int(message,16)

def rsa_sign(m, cle):
    sign = rsa(h(m), cle)
    return (m,sign)

def rsa_verify(m, cle):
    sign = rsa(m[1],cle)
    if h(m[0]) ==sign:
      return True
    else:
      return False


