from scipy import optimize
import sympy as sp
import numpy as np

x = sp.symbols('x')

def allroots(f, a, b, N = 100):
	intervals = np.linspace(a, b, N)
	# print(intervals)

	f_lam = sp.lambdify(x, f)
	x_prev = 0
	roots = []
	for x_cur in intervals:
		if (f_lam(x_cur)*f_lam(x_prev) < 0):
			roots.append(optimize.brentq(f_lam, x_prev, x_cur))
		x_prev = x_cur
	return roots

f = sp.sqrt(x) - 4*sp.sin(x)

print(allroots(f,0.0,16))


