#!/usr/bin/env python3

def calka(f, xmin, xmax, n=1000):
	'''Calkowanie metoda Monte-Carlo'''
	c = 0
	ymax = -1000.0
	ymin = 1000.0
	x = xmin
	while x<xmax:
		if f(x)>ymax:
			ymax = f(x)
		if f(x)<ymin:
			ymin = f(x)
		x += 0.1

	from random import uniform
	for _ in range(n):
		x = uniform(xmin,xmax)
		y = uniform(ymin,ymax)
		if y>0 and 0<y<f(x):
			c += 1
		elif y<0 and 0>y>f(x):
			c -= 1

	print((ymax-ymin)*(xmax-xmin)*c/n)

def pi(n):
	'''Obliczanie pi metoda Monte-Carlo'''
	from random import uniform
	c = 0
	for _ in range(n):
		x = uniform(-1,1)
		y = uniform(-1,1)
		if x**2+y**2 <= 1:
			c += 1
	print(4*c/n)

if __name__ == "__main__":
	pass