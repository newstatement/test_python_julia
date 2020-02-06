using Dates
function cputime(a,b,n)
	t0 = now()
	for i = 1:n
		a /= b
	end
	t1 = now()
	return [t1-t0, a]
end

function exhaust_heuristic_time(n,s)
	t1 = now()
	c = Array{Float64,1}(undef,factorial(big(n)))
	for i = 1:factorial(big(n))
		c[i] = 0.0
		for j = 1:s
			c[i] += rand()
		end
		c[i] /= s
	end
	t2 = now()
	return [t2-t1,c]
end
