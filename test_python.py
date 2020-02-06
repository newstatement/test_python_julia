import datetime
import math
from random import random

def cputime(a,b,n):
	t0 = datetime.datetime.now()
	for i in range(n):
		a /= b
	t1 = datetime.datetime.now()
	return [t1-t0, a]

def exhaust_heuristic_time(n,s):
	t0 = datetime.datetime.now()
	p = math.factorial(n)
	c = [0.0] * p
	for i in range(p):
		c[i] = 0.0
		for j in range(s):
			c[i] += random()
		c[i] /= s
	t1 = datetime.datetime.now()
	return [t1-t0,c]
