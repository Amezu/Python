#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce

print("Zad 1.")
# Proszę napisać program testujący alternatywne sposoby budowania list wyników
from time import time
from sys import version

powt=1000
N=10000

def forStatement():
	l=[]
	for i in range(N):
		l.append(i**3)
	return l

def listComprehension():
	l=[i**3 for i in range(N)]
	return l

def mapFunction():
	l=map(lambda i: i**3, range(N))
	return l

def generatorExpression():
	l=(i**3 for i in range(N))
	return l

def tester(fun):
	t=time()
	fun()
	t=time()-t
	return t

print(version)
test=(forStatement, listComprehension, mapFunction, generatorExpression)
for testFunction in test:
 print(testFunction.__name__.ljust(20), '=>', tester(testFunction))



print("\n\nZad 2.")
# Proszę napisać funkcję obliczającą wartość całki metodą trapezów korzystając z funkcji map (funkcja podcałkowa, granice całkowania oraz liczba kroków jako parametry wywołania funkcji)

def calka(fun, a, b, n):
	dx=(b-a)/n
	x = (a+i*dx for i in range(n))
	y = sum(map(fun, x))*dx
	print(y)

calka(lambda w: w, 0, 1, 100)
calka(lambda w: w, 0, 1, 100000)



print("\n\nZad 3.")
# Proszę wyznaczyć wartość liczby pi metodą Monte-Carlo korzystając z funkcji filter

from random import uniform

def pi(n):
	k = sum(1 for _ in filter(lambda x: x[0]*x[0]+x[1]*x[1]<=1, ((uniform(-1,1),uniform(-1,1)) for _ in range(n))))
	return 4*k/n

print(pi(10))
print(pi(10000))


print("\n\nZad 4.")

macierz = [[0,0,1],[0,2,3],[5,2,1]]

# największa wartość w każdym wierszu macierzy (map)
m = list(map(max, macierz))
print(m)

# największa wartość w każdej kolumnie macierzy
m = list(map(max, zip(*macierz)))
print(m)

macierz2 = [[1,2,1],[0,5,3],[5,2,1]]

# suma dwóch macierzy
m = [[macierz[i][j]+macierz2[i][j] for j in range(len(macierz[0]))] for i in range(len(macierz))]
print(m)

m = list((map(lambda x,y: x[i]+y[i], zip(*macierz), zip(*macierz2)) for i in range(len(macierz))))
print(m)


print("\n\nZad 5.")
# Proszę napisać funkcję przyjmującą dwa parametry - lista x-ów i y-ów. Korzystając z funkcji reduce i map proszę obliczyć (i zwrócić z funkcji) wartości dofitowanych współczynników prostej oraz ich niepewności 

from math import sqrt

def fun(x,y):
	from operator import add
	x_sr = reduce(add, x)/len(x)
	y_sr = reduce(add, y)/len(y)

	D = sum(map(lambda i: (i-x_sr)**2, x))
	print(D)
	a = 1/D * sum(map(lambda i: i[1]*(i[0]-x_sr), zip(x,y)))
	print(a)
	b = y_sr - a*x_sr
	print(b)

	dy = sqrt(sum(map(lambda i: (i[1]-(a*i[0]+b))**2, zip(x,y)))/(len(x)-2))
	print(dy)
	da = dy / sqrt(D)
	print(da)
	db = dy * sqrt(1/len(x) + x_sr**2/D)
	print(db)

fun([1,2,3],[100,122,331])
