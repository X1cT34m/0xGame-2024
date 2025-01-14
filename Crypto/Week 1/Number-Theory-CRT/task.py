from Crypto.Util.number import bytes_to_long, getPrime
from hashlib import md5
from random import randint
from gmpy2 import invert,gcd

#Hash Function:
def MD5(m):return md5(str(m).encode()).hexdigest()

#RSA AlgorithmParameter Generation Function:
def KeyGen():
	Factor_BitLength = 30
	q = getPrime(Factor_BitLength)
	p = getPrime(Factor_BitLength)
	N = p * q
	#Euler's totient function:
	phi = (p-1) * (q-1)

	#Generate Keys:
	e = randint(1,phi)

	#Generate Result:
	Pub_Key = (N,e)
	return Pub_Key

Pub = KeyGen()

N = Pub[0]
e = Pub[1]

#RSA Encrypt:
m = randint(1,N)
c = pow(m,e,N)

print(f'Pub_Key = {Pub}')
print(f'Encrypt_msg = {c}')

'''
Pub_Key = (1022053332886345327, 294200073186305890)
Encrypt_msg = 107033510346108389
'''

flag = '0xGame{'+ MD5(m) +'}'