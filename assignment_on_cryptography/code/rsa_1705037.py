# -*- coding: utf-8 -*-
"""BitVectorDemo.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NoLVEBqkvrHwoYoEuxX0BeJvaJ5MtVrA
"""

# !pip install BitVector


"""Tables"""

from math import ceil,floor
import numpy as np
import copy
from BitVector import *
import time

import random

class RSA :
	def setPlainTextKeyLength(self,plaintext,key_length):
		self.plaintext = plaintext
		self.key_length = key_length
		
	def gcd(self,p,q):
		while q!=0:
			p,q=q,p%q
		return p

	def coprime(self,e,phi):
		return self.gcd(e,phi)==1

	def power(self,x, y, p):
		
		# Initialize result
		res = 1
		
		# Update x if it is more than or
		# equal to p
		x = x % p
		while (y > 0):
			
			# If y is odd, multiply
			# x with result
			if (y & 1):
				res = (res * x) % p

			# y must be even now
			y = y>>1 # y = y/2
			x = (x * x) % p
		
		return res


	def encrypt(self,P,e,n):
		return self.power(P,e,n)

	def decrypt(self,C,d,n):
		return self.power(C,d,n)
	
	def generateKeys(self) :
		iter = 4;
		primes = []
		k=int(self.key_length/2)

		for n in range(int(2**(k-1)),int((2**k)-1)):
			bv = BitVector(intVal = n)
			check = bv.test_for_primality()
			if check>0.7:
				primes.append(n)
				if len(primes)==2 :
					break
		self.p = primes[0]
		self.q = primes[1]
		self.n=self.p*self.q
		self.phi = (self.p-1)*(self.q-1)

		e = 2
		for i in range(2,self.phi):
			if self.coprime(i,self.phi):
				e=i
				break
		self.e = e

		ebv = BitVector(intVal=self.e)
		phibv = BitVector(intVal=self.phi)
		self.d = ebv.multiplicative_inverse(phibv).int_val()

		self.keys = {'public' : (self.e,self.n),'private': (self.d,self.n)}
	
	def createCipherText(self):
		self.ciphertext = []
		for i in range(len(self.plaintext)):
			self.ciphertext.append(self.encrypt(ord(self.plaintext[i]),self.e,self.n))
	
	def createDecryptedText(self):
		self.decryptedtext = ""
		for i in range(len(self.ciphertext)):
			self.decryptedtext += chr(self.decrypt(self.ciphertext[i],self.d,self.n))
	
	def EncryptionDecryption(self):
		self.generateKeys()
		self.createCipherText()
		self.createDecryptedText()




# Driver Code

# key_length = int(input("input key length :"))
# plaintext = input("plain text :")
# rsa = RSA() 
# rsa.setPlainTextKeyLength(plaintext,key_length)
# rsa.EncryptionDecryption()

# print("Generated keys")
# print(rsa.keys)

# print("Cipher Text:")
# print(rsa.ciphertext)

# print("Decrypted Text:")
# print(rsa.decryptedtext)

#time related performance
# plaintext = input("plain text :")
# key_lengths = [16,32,64,128]
# timetable = {16:{}, 32:{}, 64:{}, 128:{} }

# for key_length in key_lengths:
# 	rsa = RSA() 
# 	rsa.setPlainTextKeyLength(plaintext,key_length)
# 	times = {}

# 	start_time = time.time()
# 	rsa.generateKeys()
# 	end_time = time.time()
# 	times['Key Generation'] = end_time-start_time

# 	start_time = time.time()
# 	rsa.createCipherText()
# 	end_time = time.time()
# 	times['Encryption'] = end_time-start_time

# 	start_time = time.time()
# 	rsa.createDecryptedText()
# 	end_time = time.time()
# 	times['Decryption'] = end_time-start_time

# 	timetable[key_length] = times
# print(timetable)