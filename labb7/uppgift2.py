"""
2. För att beräkna rötter till en ekvation f(x)=0 med Newtons metod behöver man också derivatan av f.
Ni ska nu skriva en funktion som realiserar Newtons metod och som utnyttjar SymPy för att beräkna derivatan (diff)
så att man bara behöver skicka in f och inte dess derivata. 

Funktionen ska vara på formen newton(f, x, x0, tol = 1e-10). 
- Här är f ett uttryck med den symboliska variabeln x
- x0 startvärdet för iterationen och 
- tol anger gränsen för att avbryta algoritmen då absolutbeloppet av differensen mellan två efterföljande värden är mindre än tol. 
|y|

Om den inte har konvergerat så att differensen är mindre än tol efter 100 iterationer så ska den avbryta,
skriva ut 'Misslyckades att konvergera' och 
returnera np.nan.

I annat fall ska den returnera den approximativa lösningen.

Viktigt: För att beräkna värdet av f i en punkt a (där a är ett tal)
kan man som vi såg förra veckan använda f.subs(x, a).
Det är viktigt man ser till att a är ett flyttal istället för ett exakt tal i detta fallet
för annars riskerar man att iterationerna ger väldigt komplexa exakta uttryck.
Alternativt kan man använda funktionen sp.lambdify(x, f) som konverterar f till en numpy-funktion,se exempel nedan. 
Detta andra alternativet är rekommenderat här och generellt om man kombinerar sympy med numeriska beräkningar (numpy).
"""

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


# f_lam = sp.lambdify(x, f)
# x_values = np.linspace(0, 16)
# y_values = []
# for x in x_values:
# 	y_values.append(f_lam(x))

# plt.plot(x_values, y_values)
# plt.show()
