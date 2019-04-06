#!/usr/bin/env python3

print("Zad 1")

def fun(fn, n):
	with open(fn) as f:
		l = f.readlines()
		print(*l[:n])
		print(*l[-n:])
		print(*l[::3])
		print( )
		print([i.split()[n-1] for i in l if n<len(i.split())])			
		print([i[n-1] for i in l if n<len(i)])

fun("plik.txt", 3)



print("\n\nZad 2")

import keyword
print(keyword.kwlist)
def fun(fn, wielkosc = True):
	if wielkosc == False:
		kw = []
		for i in keyword.kwlist:
			kw.append(i.upper())
	with open(fn) as f:
		for n,l in enumerate(f):
			if wielkosc == True:
				if any(map(lambda x: x in keyword.kwlist, l.split())):
					print(n,l)
			else:
				if any(map(lambda x: x.upper() in kw, l.split())):
					print(n,l)
# fun("zadania.py")
fun("zadania.py", False)

# IMPORT
# IN

print("\n\nZad 3")

import glob
s = {}
for fn in glob.glob("*.txt"):
	with open(fn) as f:
		for l in f:
			for w in l.split():
				if w[0] not in s:
					s[w[0]]=0
				s[w[0]]+=1
l=[(k,w) for k,w in s.items()]

l.sort()
print(l)

l.sort(key = lambda x: x[1])
print(l)



print("\n\nZad 4")
x=[]
y=[]
names = glob.glob("*.in")
print(names)
with open(names[0]) as f:
	for l in f:
		x.append(int(l.split()[0]))
		y.append([])

for fn in names:
	with open(fn) as f:
		for n,l in enumerate(f):
			y[n].append(float(l.split()[1]))

import numpy
with open('plik.out','w') as out:
	for i in x:
		out.write(str(i))
		out.write('\t')
		out.write(str(numpy.average(y[i])))
		out.write('\t')
		out.write(str(numpy.std(y[i])))
		out.write('\n')



print("\n\nZad 5")
def gnuplot():
	with open('gnuplot.sh','w') as g:
		g.write('set term png\n')
		g.write('set out \'plik.png\'\n')
		g.write('plot ')
		for i in names:
			g.write('\'')
			g.write(i)
			g.write('\', ')
		g.write('\'plik.out\' with errorbars\n')
gnuplot()