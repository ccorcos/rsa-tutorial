##############################################################################
## RSA Public-Private-Key Encryption										##
## This script just shows the basic concept. 								##
## Chet Corcos Feb 20, 2014													##
## 																			##
## ref: http://en.wikipedia.org/wiki/RSA_%28algorithm%29#Key_generation  	##
##############################################################################	

import math

def wait():
	print ""
	x = raw_input("Press <enter> to continue...")

def oops(n):
	print "Oops! This is probably because your p and q were so small. Currently n = " + str(n) + ". This \
corresponds to " + str(int(math.log(n)/math.log(2))) + " bit encryption. The current standard for the \
internet is 128 bit encryption. That corresponds to a decimal number with 38 digits and requires some \
rather large prime numbers. Try another message."

# recursive extended euclidian algorithm
def egcd(a,b):
	if a == 0:
		return (b,0,1)
	else:
		g,y,x = egcd(b % a, a)
		return (g, x - (b // a)*y, y)

# multiplicative modular inverse
def modinv(a,m):
	g,x,y = egcd(a,m)
	if g != 1:
		return None
	else:
		return x%m

# modular exponentiation by squaring
def powmod(b,e,m):
	x=1
	bits = "{0:b}".format(e)
	for i,bit in enumerate(bits):
		if bit=='1':
			x = ((x**2)*b)%m
		elif bit=='0':
			x = (x**2)%m
	return x%m

## COMPUTING THE KEYS
# 1) Choose 2 distinct prime numbers, p and q.
print ""
print "RSA Public-Private-Key Encryption Demo"
print ""
print "RSA encryption is based on some complicated math involving prime numbers. If Alice wants to send Bob a message \
but their only means of communication is through a public channel, then Bob generates a public-private key pair and sends \
Alice the public key. Alice encrypts the message using the public key and sends it back to Bob over the public channel. The only way to \
decrpyt this message is with Bob's private key."
print ""
print "COMPUTING THE KEYS"
print "1) Choose 2 distinct prime numbers, p and q. If p and q are small, RSA always doesn't work well."
p = int(raw_input("p = "))
q = int(raw_input("q = "))
# 2) n is the modulus for both public and private keys. The bits of n is the key length
print ""
print "2) n is the modulus for both public and private keys. The bits of n is the key length."
n = p*q
print "n = p*q = " + str(n)
wait()
# 3) phi is Eulers totient function which is the amount of numbers less than n that are coprime with p and q.
print ""
print "3) phi(n) is Eulers totient function which is the amount of numbers less than n that are \
coprime with p and q. Two numbers a and b are coprime if the greatest common denomendator, gcd(a,b) = 1."
phi = (p-1)*(q-1)
print "phi(n) = (p-1)*(q-1) = " + str(phi)
wait()
# 4) Choose 1<e<phi such that phi and e are coprime. Choosing a prime number is an easy choice ;)
# e is released as the "public key exponent"
print ""
print "4) Choose 1 < e < phi(n) such that phi(n) and e are coprime (hint: a prime number is an easy \
choice ;). e is released as the public key exponent."
e = int(raw_input("e = "))
# 5) Find d by computing the multiplicative modular inverse.
# e.i. solve for d: e*d mod phi = 1
# d is keps as the "private key exponent"
print ""
print "5) Find d by computing the multiplicative modular inverse, that is, solve for d where: e*d mod \
phi = 1. d is kept as the private key exponent."
d = modinv(e,phi)
print ""
print "d = " + str(d)
wait()
# 6) the keys:
print ""
print "6) Each key is now a combination of 2 numbers:"
pubKey = (e,n)
privKey = (d,n)
print "the public key is (e,n) = " + str(pubKey)
print "the private key is (d,n) = " + str(privKey)
wait()

## MESSAGE ENCRYPTION
# 1) first choose a message
print ""
print ""
print "MESSAGE ENCRYPTION"
while True:
	print "1) Choose a message, m, represented as an integer such that m < n. In practice, if m > n, \
m will be broken up in to chunks."
	m = int(raw_input("m = "))
	if (m >= n):
		print ""
		print "Please choose m < n."
		print ""
		continue

	# 2) encrypt the message as m^e mod phi
	print ""
	print "2) Encrypt the message using the public key: eMsg = m^e mod n."
	eMsg = powmod(m,e,n)
	print "eMsg = " + str(eMsg)
	if (eMsg == m):
		print ""
		oops(n)
		wait()
		continue
	wait()
	# 3) dencrypt the message as eMsg^d mod phi
	print ""
	print "3) Deccrypt the message using the private key: dMsg = eMsg^d mod n."
	dMsg = powmod(eMsg,d,n)
	print "dMsg = " + str(dMsg)
	print ""
	if (m != dMsg):
		oops(n)
	x = raw_input("Shall we encrypt another? control-c to quit.")
	print ""

