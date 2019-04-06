#!/usr/bin/env python3

class Fib:
	def __init__ (self,n):
		self.f0 = 0
		self.f1 = 1
		self.n = 0
		self.N = n

	def __iter__ (self):
		return self

	def __next__ (self):
		self.f0, self.f1 = self.f1, self.f0+self.f1
		self.n += 1
		if self.n>self.N:
			raise StopIteration
		return self.f1

f=Fib(3)

print("jedna:")
for i in f:
	for j in f:
		print (i,j)

class Fib:
	def __init__ (self,n):
		self.N = n

	def __iter__ (self):
		return FibNext(self.N)

class FibNext:
	def __init__ (self,n):
		self.f0 = 0
		self.f1 = 1
		self.n = 0
		self.N = n

	def __next__ (self):
		self.n += 1
		if self.n>self.N:
			raise StopIteration
		self.f0, self.f1 = self.f1, self.f0+self.f1
		return self.f1


f=Fib(3)

print("\ndwie:")
for i in f:
	for j in f:
		print (i,j)

###############

from scipy.misc import derivative
from math import fabs

class Zero:
	def __init__ (self,f,x0,eps = 1e-5):
		self.f = f
		self.x = x0
		self.eps = eps

	def __iter__ (self):
		return self

	def __next__ (self):
		if fabs(self.f(self.x)) < self.eps:
			raise StopIteration
		self.x = self.x - self.f(self.x)/derivative(self.f,self.x,1e-5)
		return (self.f(self.x),self.x)

zero = Zero(lambda x: x**2, 1.5)
for i in zero:
	print(i)

class Pseudolosowe:
	def __init__ (self):
		self.m = 2**31 - 1
		self.a = 7**5
		self.c = 0

		self.x = 1

	def __iter__ (self):
		return self

	def __next__ (self):
		self.x = (self.a*self.x+self.c)%self.m
		return self.x/self.m

los = Pseudolosowe()

count1 = [0 for _ in range(10)]
for i in range(100000):
	x,y = next(los),next(los)
	for i in range(10):
		if (x<i*0.1+0.1 and y<i*0.1+0.1):
			count1[i] += 1

count2 = [0 for _ in range(10)]
from random import random
for i in range(100000):
	x,y = random(),random()
	for i in range(10):
		if (x<i*0.1+0.1 and y<i*0.1+0.1):
			count2[i] += 1

print(count1)
print(count2)