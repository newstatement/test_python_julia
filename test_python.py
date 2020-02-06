import time
import math
from random import random

def cputime(a,b,n):
	t0 = time.time_ns()
	for i in range(n):
		a /= b
	t1 = time.time_ns()
	return [t1-t0, a]

def exhaust_heuristic_time(n,s):
	t0 = time.time_ns()
	p = math.factorial(n)
	c = [0.0] * p
	for i in range(p):
		c[i] = 0.0
		for j in range(s):
			c[i] += random()
		c[i] /= s
	t1 = time.time_ns()
	return [(t1-t0)/1000,c]

def runbatch(n,p,s):
	f = open("time_python.csv","w")
	for i in range(n):
		for j in range(p):
			r = exhaust_heuristic_time(i+1,s)
			f.write(str(r[0])+",")
		f.write("\n")
	f.close()
