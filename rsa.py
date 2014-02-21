##############################################################################
## RSA Public-Private-Key Encryption										##
## This script just shows the basic concept. 								##
## Chet Corcos Feb 20, 2014													##
## 																			##
## ref: http://en.wikipedia.org/wiki/RSA_%28algorithm%29#Key_generation  	##
##############################################################################	

## COMPUTING THE KEYS
# 1) Choose 2 distinct prime numbers, p and q.
p = 5
q = 11
# 2) n is the modulus for both public and private keys. The bits of n is the key length
n = p*q
# 3) phi is Eulers totient function which is the amount of numbers less than n that are coprime with p and q.
phi = (p-1)*(q-1)
# 4) Choose 1<e<phi such that phi and e are coprime. Choosing a prime number is an easy choice ;)
# e is released as the "public key exponent"
e = 3 
# 5) find d by computing the multiplicative modular inverse.
# e.i. solve for d: e*d mod phi = 1
# d is keps as the "private key exponent"
d = 1
while int(divmod(e*d,phi)[1]) != 1:
	d = d+1
# 6) the keys:
pubKey = (e,n)
privKey = (d,n)

## MESSAGE ENCRYPTION
# 1) first choose a message
m = 13
# 2) encrypt the message as m^e mod phi
eMsg = int(divmod(pow(m,e),phi)[1])
# 3) dencrypt the message as eMsg^d mod phi
dMsg = int(divmod(pow(eMsg,d),phi)[1])

