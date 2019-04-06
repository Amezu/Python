#!/usr/bin/env python3.6
from math import sqrt
from random import randrange

#1
def isprime(a):
	for i in range(2, int(sqrt(a))+1):
		if a%i == 0:
			return False
	return True

#2
s={}
while len(s)!=50:
	a=randrange(100)
	if a not in s:
		s[a]=isprime(a)
print(s)

#3
l=[randrange(20) for _ in range(100)]
print(l)

s1,s2={},{}
for i,x in enumerate(l):
	if not x%2:
		s1.setdefault(x,[]).append(i)
	else:
		s2.setdefault(x,[]).append(i)
print('s1 =',s1)
print('s2 =',s2)

s3={}
for k in s1:
	for x in s1.get(k):
		if not x%3:
			s3.setdefault(k,[]).append(x)
	if k not in s3:
		if len(s1.get(k))==1:
			s3[k]=(s1.get(k),)
		else:
			s3[k]=(max(s1.get(k)),min(s1.get(k)))

s3 = {k:w if [j for j in w if j%3] else (min(w), max(w)) for k,w in s1.items()}
print('s3 =',s3)

def podzielne(lista,a):
	for i in lista:
		if i%a==0:
			return True
	return False

s3 = {k:[j for j in w if not j%3] if podzielne(w,3) else (min(w), max(w)) for k,w in s1.items()}

print('s3 =',s3)

#4
# a=int(input("Podaj liczbe: "))
a=5
s={i:randrange(2,15) for i in range(a)}
l=[(w,k) for k,w in s.items()]

print('s =',s)
print('l =',l)

s={x:y for x,y in l}
print('s =',s)

#5
l=[randrange(11) for _ in range(100)]
print('\nl =',l)

s={k:[] for k in range(11)}

last=0
s0={j:[l.index(j, last+1) for i in l if i==j] for j in range(11)}
print('\ns0 =',s0)

for k in s:
	last=0
	for i in l:
		if i==k:
			last=l.index(i,last)+1
			s[k].append(last-1)

print('\ns =',s)


#6
s1={i:randrange(1,100) for i in range(10)}
s2={i:randrange(1,100) for i in range(10)}
print('s1 =',s1)
print('s2 =',s2)
s1={s1.get(k):k for k in s1}
s2={s2.get(k):k for k in s2}
print('s1 =',s1)
print('s2 =',s2)

s={k:(s1[k],s2[k]) for k in s1 if k in s2}
print('s =',s)