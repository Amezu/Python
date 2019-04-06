#!/usr/bin/env python3

import random

def fun(a,b=10,c=5):

	if not all((a>0,b>0,c>0,a<b)):
		raise

	n,p = 0,0
	for i in range(c):
		if random.randint(a,b)%2:
			n+=1
		else:
			p+=1
	if n==0:
		raise ZeroDivisionError

	return p/n

def tryfun(a):
	try:
		print(fun(a))
	except ZeroDivisionError:
		print('Dzielenie przez 0')	
	except:
		print('Zle wartosci')

tryfun(2)
tryfun(9)
tryfun(10)

#

class DlugoscError(Exception):
	pass

class OstatniaError(Exception):
	pass

def pitagorejskie(l,n):

	if len(l)%n:
		raise DlugoscError

	k = [l[i*n:i*n+n] for i in range(len(l)//n)]
	for i in k:
		s=0
		for a in i[:-1]: 
			if a>i[-1]:
				raise OstatniaError
			s+=a**2
		if s==i[-1]**2:
			print(i, "jest pitagorejskie")

try:
	pitagorejskie((1,2,2,3,4,5),3)
except DlugoscError:
	print('Zla dlugosc')	
except OstatniaError:
	print('Ostatnia liczba nie jest najwieksza')	

#

class BrakZerowego(Exception):
	pass

import math
def zero(f,p,k):
	if f(p)*f(k)>0:
		raise BrakZerowego
	while math.fabs(k-p)>1e-7:
		if math.fabs(f((k+p)/2))<1e-7:
			return (k+p)/2
		if f(p)*f((k+p)/2)<0:
			k=(k+p)/2
			print("k",k)
		else:
			p=(k+p)/2
			print("p",p)
	return p

try:
	print(zero(lambda x: x+1,-2,0))
	print(zero(lambda x: x+1,1,2))
except ZeroDivisionError:
	print('Funkcja nieokreslona')
except BrakZerowego:
	print('Brak m. zerowego w tym przedziale')

#

class WierszeError(Exception):
	pass

class KolumnyError(Exception):
	pass

class ZapisError(Exception):
	pass

class CzytError(Exception):
	pass

import os
import glob
def aver(filelist):

	if not os.access('aver.out',os.W_OK):
		raise ZapisError

	with open('aver.out','w') as out:
		for fn in filelist:

			if not os.access(fn,os.F_OK):
				raise FileNotFoundError
			if not os.access(fn,os.R_OK):
				raise CzytError

			with open(fn) as f:				
				l=f.readlines()
				if len(l)==0:
					raise WierszeError
				s=0
				for i in l:
					if len(i.split())<2:
						raise KolumnyError
					s += float(i.split()[0]) + float(i.split()[1])
				out.write(fn+": "+str(s/len(l)/2)+"\n")

try:
	aver(glob.glob('*.dat'))
except WierszeError:
	print('Za malo wierszy')	
except KolumnyError:
	print('Za malo kolumn')
except ValueError:
	print('Wartosc nieliczbowa')	
except FileNotFoundError:
	print('Plik nie istnieje')
except ZapisError:
	print('Nie da sie zapisywac')
except CzytError:
	print('Nie da sie czytac')	
