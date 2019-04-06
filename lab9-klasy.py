#!/usr/bin/env python3

from copy import deepcopy
class Automat:

	def __init__ (self, N, n, iteracje):
		self.N = N
		self.i = iteracje
		self.siatka = [[0]*N for _ in range(N)]
		for i in range (n):
			for j in range (n):
				self.siatka[N//2-n//2+i][N//2-n//2+j] = 1
		self.wypisz()

	def wypisz (self):
		for i in range(self.N):
			for j in range(self.N):
				print('*' if self.siatka[i][j] else '-',end='')
			print()
		print()

	def ewolucja (self):
		for i in range (self.i):
			# siatka = [self.siatka[i][:] for i in range(self.N)]
			siatka = deepcopy(self.siatka)
			for i in range(self.N):
				for j in range(self.N):
					s = sum	(siatka [(i+k)%self.N] [(j+l)%self.N] for k in range(-1,2) for l in range(-1,2))
					s -= siatka[i][j]
					if self.siatka[i][j]:
						self.siatka[i][j] = 1 if s==2 or s==3 else 0
					else:
						self.siatka[i][j] = 1 if s==3 else 0
			self.wypisz()

	
a = Automat(20,5,4)
a.ewolucja()

from math import sqrt

class Wektor3D:

	def __init__ (self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	def __add__ (self, other):
		x = self.x + other.x
		y = self.y + other.y
		z = self.z + other.z
		return Wektor3D (x, y, z)

	def __sub__ (self, other):
		x = self.x - other.x
		y = self.y - other.y
		z = self.z - other.z
		return Wektor3D (x, y, z)

	def __mul__ (self, other):

		if isinstance(other,Wektor3D):
			a = self.x*other.x + self.y*other.y + self.z*other.z
			x = self.y*other.z - self.z*other.y
			y = self.x*other.z - self.z*other.x
			z = self.x*other.y - self.y*other.x
			return a, Wektor3D (x, y, z)

		x = self.x * other
		y = self.y * other
		z = self.z * other
		return Wektor3D (x, y, z)

	def __eq__ (self, other):
		return self.x == other.x and self.y == other.y and self.z == other.z		

	def __str__ (self):
		return "("+str(self.x)+","+str(self.y)+","+str(self.z)+")"

	def len (self):
		return sqrt(self.x**2+self.y**2+self.z**2)

v = Wektor3D(1,2,3)
w = Wektor3D(-1,2,0)
print(v)
print(v-w)
print(v+w)
print(v==w)
print(v==v)
print(v.len())
print(v*2)
l = v*w
print(l[0])
print(l[1])
