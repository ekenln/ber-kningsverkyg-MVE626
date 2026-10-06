import sympy as sp
x = sp.symbols('x') # Definierar variabeln x

# Beräknar gränsvärde för f1 - f4
f1 = ((3*x+4)/(4*x+3))**x
print(sp.limit(f1, x, sp.oo))

f2 = (1+3*x)**(1/(8*x))
print(sp.limit(f2, x, 0))

f3 = (x - sp.sin(x))/(x-sp.tan(x))
print(sp.limit(f3, x, 0))

f4 = (sp.sin(x**sp.pi)**2)/(1-sp.cos(2*x**sp.pi))
print(sp.limit(f4.subs(x**sp.pi, x), x, 0))

# Beräknar derivata och förenklar funktionerna f5 - f8

f5 = sp.exp(3*x)/x
print(sp.simplify(sp.diff(f5)))

f6 = sp.asin((2*x+1)/5)
print(sp.simplify(sp.diff(f6)))

f7 = sp.exp(2*x)*sp.ln(2*x)
print(sp.simplify(sp.diff(f7)))

f8 = sp.cos(2*x) - sp.sin(x)**2
print(sp.simplify(sp.diff(f8)))

# Beräknar taylorserie för f9 - f11

f9 = sp.exp(-3*x)
print(f9.series(x, 1, 6))

f10 = sp.sin(2*x)
print(f10.series(x, sp.pi, 6))

f11 = sp.sin(x)**2
print(f11.series(x, sp.pi*sp.Rational(-1,2), 6))

f12 = (x+1)/(x**2)
print(f12.series(x, -2, 6))