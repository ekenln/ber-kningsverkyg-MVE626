# %%
#UPPGIFT 1
import numpy as np
import matplotlib.pyplot as plt

def bisektion(f, start, stop, tol = 1e-10):
    if f(start)*f(stop) > 0:
        print('Funktionens värde i ändpunkterna har inte olika tecken.')
        return np.nan
    else:
        while stop-start > tol:
            mid = (stop+start)/2
            if f(mid)*f(stop) < 0:
                start = mid
            elif f(mid)*f(start) < 0:
                stop = mid
            elif f(mid) == 0:
                return mid
            elif f(start) == 0:
                return start
            elif f(stop) == 0:
                return stop
        return mid

f = lambda x: np.sqrt(x) - 4*np.sin(x)
x = np.linspace(0, 25, 1000)

plt.plot(x, f(x))
#plt.show()

print('Funktionen har följande nollställen:')
print(bisektion(f, 0, 1))
print(bisektion(f, 0.0001, 1))
print(bisektion(f, 1, 3))
print(bisektion(f, 3, 7.5))
print(bisektion(f, 7.5, 10))
print(bisektion(f, 10, 14))
print(bisektion(f, 14, 20))

# %%
#UPPGIFT 2

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.symbols('x')

def my_newton(f, x, x0, tol = 1e-10):
	der = sp.diff(f, x)
	der_lam = sp.lambdify(x, der)
	f_lam = sp.lambdify(x, f)

	for i in range(100):
		der_sol = der_lam(x0)
		if (np.abs(der_sol) < tol):
			print("Misslyckades att konvergera")
			return np.nan
		x_next = x0 - f_lam(x0)/der_sol
		if(np.abs(x_next-x0) < tol):
			return x_next
		x0 = x_next
	print("Misslyckades att konvergera")
	return np.nan

f = sp.sqrt(x) - 4*sp.sin(x)
print(my_newton(f, x, 0.1))
print(my_newton(f, x, 2.7))
print(my_newton(f, x, 6.9))
print(my_newton(f, x, 8.5))
print(my_newton(f, x, 13.5))
print(my_newton(f, x, 14.3))
print(my_newton(f, x, 1.47))

#%%
#UPPGIFT 3
import numpy as np

def mittpunktsmetoden(f, a, b, N):
    half_step = (b-a)/(2*N)
    x = np.linspace(a+half_step, b-half_step, N)
    sum = 0
    for i in x:
        sum += f(i)*(b-a)/N
    return(sum)

f = lambda x: np.sin(x)/x

for i in range(7):
    print(f'N = 10^{i}: {mittpunktsmetoden(f, 0, np.pi, 10**i)} - 1.8519370519824662 = {mittpunktsmetoden(f, 0, np.pi, 10**i)-1.8519370519824662}')

# För varje 10-dubbling av antalet intervall får resultatet 2 fler korrekta värdesiffror 

f = lambda x: 1/x

for i in range(7):
    print(f'N = 10^{i}: {mittpunktsmetoden(f, 0, 1, 10**i)}')

# Värdet ökar för varje ökning av antalet intervall, eftersom integralen -> oo

def trapetsmetoden(f, a, b, N):
    x = np.linspace(a, b, N+1)
    sum = 0
    h = (b-a)/N
    for i in x:
        sum += (f(i)+f(i+h))/2*h
    return(sum)

def f(x):
    if x == 0:
        return 1
    else:
        return np.sin(x)/x

for i in range(7):
    print(f'N = 10^{i}: {trapetsmetoden(f, 0, np.pi, 10**i)} - 1.8519370519824662 = {trapetsmetoden(f, 0, np.pi, 10**i)-1.8519370519824662}')

# Liknande går inte att göra för f = 1/x eftersom det första värdet i trapetsen är oändligt stort.

# Ingen enorm skillnad på mittpunkts- och trapetsmetoden, men mittpunktsmetoden är mer flexibel för olika funktioner och ger en extra korrekt värdesiffra

# a > b ger rätt resultat eftersom h blir negativt. 
# a = b ger rätt resultat eftersom bredden blir 0

#%%
#UPPGIFT 4
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

#%%
#UPPGIFT 5
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

def myfunctionplot(f, a, b, dx=1e-4, N=100):
    x = np.linspace(a, b, N)

    y_f = f(x)

    y_fprim = (f(x + dx) - f(x - dx)) / (2 * dx)

    y_F = cumulative_trapezoid(y_f, x, initial=0)

    fig, axs = plt.subplots(1, 3, figsize=(15, 4))

    # Plottning
    axs[0].plot(x, y_F)
    axs[0].set_title('F (integral)')
    axs[0].grid(True)

    axs[1].plot(x, y_f)
    axs[1].set_title('f (funktion)')
    axs[1].grid(True)

    axs[2].plot(x, y_fprim)
    axs[2].set_title("f' (derivata)")
    axs[2].grid(True)

    plt.show()

f = lambda x: np.sin(x)/x

myfunctionplot(f, -10, 10)