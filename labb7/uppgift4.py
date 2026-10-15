from scipy import optimize
import sympy as sp
from numpy import linspace


x = sp.symbols('x')

def allroots(f, a, b, N = 100):
	
	intervals = linspace(a, b, N)
	f_lam = sp.lambdify(x, f)
	x_left = a
	roots = []

	for x_right in intervals[1:]:
		if (f_lam(x_right)*f_lam(x_left) < 0):
			roots.append(optimize.brentq(f_lam, x_left, x_right))
		x_left = x_right
	return roots

f = sp.sqrt(x) - 4*sp.sin(x)

print(allroots(f,0.0,16))
print(allroots(f,0.01,16))
print(allroots(f,0.01,16,5))

# import matplotlib.pyplot as plt
# f_lam = sp.lambdify(x, f)
# x_values = linspace(0, 16)
# y_values = []
# for x in x_values:
# 	y_values.append(f_lam(x))

# plt.plot(x_values, y_values)
# plt.show()


