#!/usr/bin/env python3

def ifs(wsp, prawd):
	'''przeksztalca punkt na plaszczyznie,
	uzywajac podanej listy wspolczynnikow'''
	from random import random
	import matplotlib.pyplot as plt

	x=0
	y=0

	for _ in range(100):	
		los = random()
		print(los)
		suma = 0
		for i in range(len(prawd)):
			suma += prawd[i]
			if los <= suma:
				break
		# tu lepiej choices

		w = wsp[i]
		x,y = w[0]*x + w[1]*y + w[2], w[3]*x + w[4]*y + w[5]
		print(x,y)
		plt.plot(x,y,',',c='g')
	plt.axis('off')
	plt.savefig('ifs.png')

def lsystem(n=5):
	'''Przeksztalcenie wg schematu F → F+F−F−F+F'''
	string = 'F'
	for _ in range(n):
		string = string.replace('F','F+F-F-F+F')
	# print(string)

	from math import sin,cos,pi
	x=[0]
	y=[0]
	kat = 0
	for l in string:
		if l == 'F':
			x.append (x[-1]+cos(kat*pi/180))
			y.append (y[-1]+sin(kat*pi/180))
		elif l == '-':
			kat += 90
			kat %= 360
		elif l == '+':
			kat -= 90
			kat %= 360

	import matplotlib.pyplot as plt
	plt.plot(x,y,'.',c='g')
	plt.axis('off')
	plt.savefig('lsystem.png')

if __name__ == "__main__":
	pass