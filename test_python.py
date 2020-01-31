import datetime
def cputime(a,b,n):
	t0 = datetime.datetime.now()
	for i in range(n):
		a /= b
	t1 = datetime.datetime.now()
	return t1-t0
