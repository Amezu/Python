#!/usr/bin/env python3

import random

def fun1(wyrazenie):
	s={random.random():0 for _ in range(random.randrange(20))}
	for k in s:
		s[k] = '{:.3g}'.format(float(eval(wyrazenie.format(k))))
	return s

a='{0}/2-0.1'
s=fun1(a)
print(s)

def fun2(*a):
	l=[]
	for i in a[0]:
		for x in a:
			if i not in x:
				break
		else:
			l.append(i)
	return l

print(fun2([1,2,3,5],[2],[2,5]))

def fun3(s1, s2, p=True):
	if p:
		return [(s1[i], s2[i]) for i in range(min(len(s1), len(s2)))]
	else:
		return [(s1[i] if i<len(s1) else None, s2[i] if i<len(s2) else None) for i in range(max(len(s1), len(s2)))]
print(fun3([1,2],[3,5,3]))

def maksimum(a,b):
	return a if a>b else b
def fun4(cmp,a,b):
	return eval('{0}({1},{2})'.format(cmp,a,b))
print(fun4('maksimum', 5, 2))

def fun5(k, n=(10,5,2)):
	l=[i for i in n]
	l.sort(reverse=True)
	for i in l:
		while i<=k:
			print(i),
			k-=i
print("Rozmien 7 na:")
fun5(7)
print("Rozmien 11 na:")
fun5(11,(1,5))

def fun6(a, p, k, jak='r'):
	x=p-1
	while x!=a:
		x = random.randint(p,k) if jak=='r' else (p+k)//2
		if x>a:
			k = x-1
			print("k =", k)
		else:
			p = x+1
			print("p =", p)
	print("Znalazlem! a =",x)

fun6(2,0,10)
fun6(2,0,10, 'x')