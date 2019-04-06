#!/usr/bin/env python3

from sys import argv
from sys import exit

if len(argv)==1:
	print("Wpisz argumenty programu")
	exit()

s = ''.join(argv[1:])
print(s)

############

male = [el for el in s if el.islower()]
print(male)

duze = [el for el in s if el.isupper()]
print(duze)

cyfry = [int(el) for el in s if el.isdigit()]
print(cyfry)

inne = [el for el in s if not el.isalpha()]
print(inne)

##############

bezp = [z for i,z in enumerate(male) if male.index(z)==i]
print(bezp)

##############

ilosc = [(z,sum(1 for y in male if y==z)) for z in bezp]
print(ilosc)

#############

ilosc.sort(key = lambda x: x[1])
print(ilosc)

##############

samo = 'aeouyiAEOUYI'
a = sum(1 for x in s if x in samo)
print('a =',a)
b = len(s) - a
print('b =',b)

krotki = [(x,a*x+b) for x in cyfry]

print(krotki)

###############

x_sr = sum(x for x in cyfry) / len(cyfry)
print('x_sr =', x_sr)
D = sum(pow(x-x_sr,2) for x in cyfry)
a = 1/D * sum(y*(x-x_sr) for x,y in krotki)
y_sr = sum(y for _,y in krotki) / len(cyfry)
print('y_sr =', y_sr)
b = y_sr - a*x_sr

print('a =', a)
print('b =', b)
print('D =', D)