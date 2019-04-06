#!/usr/bin/env python3

import math

print("Zad 1")

def gen1():
	x=0
	while True:
		x=x+1
		yield x

def gen2(seq):
	for i in seq:
		s = sum(j for j in range(1,i//2+1) if not i%j)
		if s==i:
			yield i

def gen3(seq, a):
	for i in seq:
		if i<=a:
			yield i
		else:
			break 

for i in gen3(gen2(gen1()),500):
	print(i)


print("\n\nZad 2")

def gen(kwota, nom):
	nom.sort()
	nom.insert(0,0)

	C = [i for i in range(kwota+1)]
	for i in range(1,len(nom)):
		Ct = C[:]
		for j in range(kwota+1):
			C[j] = Ct[j] if nom[i]>j else min(Ct[j], 1+C[j-nom[i]] if nom[i]<=j else Ct[j])
		yield C
		

n = [1,6,10]
for i in gen(12, n):
	print(i)


print("\n\nZad 3")

def gen():
	u,x,i=0,1,0
	while x<=1.5+10e-7:
		yield x,u,math.log(x)
		u=u+0.05/x
		i+=1
		x+=0.05

for i in gen():
	print(i)


print("\n\nZad 4")
def gen(n):
	for i in range(1,n//2+1):
		for j in range(n-i,i-1,-1):
			t=[1 for _ in range(n-j-i)]
			t.append(i)
			t.append(j)
			yield t	

for i in gen(7):
	print(i)

print("\n\nZad 5")

k=0

def sinus(x):
	war = 0
	while True:
		war += (-1)**k*x**(1+2*k)/math.factorial(1+2*k)
		yield war

true = math.sin(45*3.14/180)
print("Dokladna:", true)

for i in sinus(45*3.14/180):
	print(i)
	k+=1
	if math.fabs(i-true)<10e-8:
		print("Iteracji:", k)
		break