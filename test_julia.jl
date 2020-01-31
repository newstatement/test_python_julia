function cputime(a,b,n)
	t0 = now()
	for i = 1:n
		a /= b
	end
	t1 = now()
	return t1-t0
end
