
function cputime(a,b,n)
	t0 = time_ns()
	for i = 1:n
		a /= b
	end
	t1 = time_ns()
	return [t1-t0, a]
end

function exhaust_heuristic_time(n,s)
	t0 = time_ns()
	c = Array{Float64,1}(undef,factorial(big(n)))
	for i = 1:factorial(big(n))
		c[i] = 0.0
		for j = 1:s
			c[i] += rand()
		end
		c[i] /= s
	end
	t1 = time_ns()
	return [Float64((t1-t0)/1000),c]
end

function runbatch(n,p,s)
	f = open("time_julia.csv","w")
	for i =1:n
		for j = 1:p
			r = exhaust_heuristic_time(i,s)
			write(f,string(r[1],","))
		end
		write(f,"\n")
	end
	close(f)
end
