#!/usr/bin/env python3

import z1

wsp = ((0,0,0,0,0.16,0), (0.2,-0.26,0,0.23,0.22,1.6), (-0.15,0.28,0,0.26,0.24,0.44), (0.85,0.04,0,-0.04,0.85,1.6))
prawd = (0.01,0.07,0.07,0.85)
# z1.ifs(wsp, prawd)

import z2
import math

z2.calka(lambda x: math.sin(x),0,2*math.pi)
z2.pi(10)
z2.pi(1000)

z1.lsystem()

print(z2.pi.__doc__)
print(help(z2.pi))