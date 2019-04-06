#!/usr/bin/env python3.5

from math import sqrt
from cmath import sqrt as csqrt

# # POBIERANIE Z KLAWIATURY
# print('a*x^2 + b*x + c = 0')
# a=float(input('a='))
# b=float(input('b='))
# c=float(input('c='))

# # POBIERANIE ARGUMENTÓW WYWOŁANIA
# from sys import argv
# a=float(argv[1])
# b=float(argv[2])
# c=float(argv[3])

a=1
b=2
c=1

d=pow(b,2)-4*a*c

#WARUNKI
if d==0:
	print('x0 =',-b/2/a)
elif d>0:
	print('x1 =',-b-sqrt(d)/2/a)
	print('x2 =',-b+sqrt(d)/2/a)
else:
	#ZESPOLONE
	print('x1 =',-b-csqrt(d)/2/a)
	print('x2 =',-b+csqrt(d)/2/a)
	#c.real, c.imag

print()

#PĘTLE
for i in range(10,3,-2):
	print(i)

print()

l=[-7,100,3]
for i in l:
	i+=7
	print(i)
print('l =',l)

for i in range(len(l)):
	l[i]+=7
print('l =',l)

print()

l=([1,2],(3,4),[5,6],(7,8))
for i,j in l:
	print(i, j)
	if i==5:
		break
else: #ten else należy do fora
	print(i, j)

print()

for i,j in l:
	print(i, j)
	if i==9:
		break
else: #else wykonuje się, jeżeli break nie zostanie użyty
	print(i, j)