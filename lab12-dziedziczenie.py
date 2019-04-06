#!/usr/bin/env python3

import abc

class Calka (abc.ABC):

	def __init__ (self, xp, xk, n, fun):
		if xk<xp or n<=0:
			raise AttributeError
		self.xp = xp
		self.xk = xk
		self.n = n
		self.f = fun

	@abc.abstractmethod
	def oblicz ():
		pass

class CalkaTrapezy (Calka):
	def oblicz (self):
		'''Oblicza calke metoda trapezow'''
		s = 0
		for i in range(self.n):
			s += self.f((self.xk-self.xp)*i/self.n+self.xp)
			s += self.f((self.xk-self.xp)*(i+1)/self.n+self.xp)
		s *= (self.xk-self.xp)/self.n/2
		print(s)
		return s

class CalkaSimpson (Calka):
	def oblicz (self):
		'''Oblicza calke metoda Simpsona'''
		f1 = 0
		for i in range(1,2*self.n,2):
			f1 += self.f((self.xk-self.xp)*i/2/self.n+self.xp)

		f2 = 0
		for i in range(0,2*self.n,2):
			f2 += self.f((self.xk-self.xp)*i/2/self.n+self.xp)

		s = (self.xk-self.xp)/2/self.n / 3 * (self.f(self.xp) + 4*f1 + 2*f2 + self.f(self.xk))
		print(s)
		return s

c = CalkaSimpson(0, 1, 5, lambda x: x)
print(c.oblicz.__doc__)
c.oblicz()

c = CalkaTrapezy(0, 1, 1, lambda x: x)
print(c.oblicz.__doc__)
c.oblicz()


from copy import deepcopy

class Stos:
	def __init__ (self, stos = 0):
		if stos!=0:
			self.stos = deepcopy(self.stos)
		else:
			self.stos = []

	def dodaj (self, a):
		self.stos.append(a)

	def usun (self, a):
		self.stos.pop()

	def dodajstos (self, stos):
		self.stos.extend(stos.stos)

	def rozmiar (self):
		return len(self.stos)

	def wypisz (self):
		for i in self.stos:
			print (i, end=' ')
		print()

class StosPosortowany(Stos):
	'''Stos posortowany rosnaco'''
	def __init__ (self):
		super().__init__()

	def dodaj (self, a):
		if len(self.stos) == 0 or self.stos[-1] <= a:
			self.stos.append(a)

	def dodajstos (self, stos):
		for i in len(stos)-1:
			if stos[i]>stos[i+1]:
				break
		else:
			self.stos.extend(stos)

s = Stos()
s.dodaj(2)
s.dodaj(65)
s.wypisz()

z = Stos()
z.dodaj(3)
z.dodaj(4)
z.wypisz()

s.dodajstos(z)
s.wypisz()

from random import randint
rozmiary = 0
for _ in range(100):
	s = StosPosortowany()
	for _ in range(100):
		# print(randint(0,100))
		s.dodaj(randint(0,100))
	rozmiary += s.rozmiar()

print(rozmiary/100)

class Z:
	linie = 0
	slowa = 0
	znaki = 0

	def __init__ (self, fn):
		self.fn = fn

	@staticmethod
	def total ():
		print ('total', Z.linie, Z.slowa, Z.znaki)

	def zlicz (self):
		l = 0
		s = 0
		z = 0

		with open(self.fn) as file:
			for line in file:
				z += len(line)
				s += len(line.split())
				l += 1

		print (self.fn, l, s, z)
		Z.linie += l
		Z.slowa += s
		Z.znaki += z
		Z.total()

z = Z('wstep.py')
Z.total()
z.zlicz()
z.zlicz()
s = Z('zadania.py')
s.zlicz()
