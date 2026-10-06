import sympy as sp

x = sp.symbols('x')

def stationar(expr, x):
	derivata = sp.diff(expr, x)
	stationar = sp.solveset(derivata, x, domain=sp.Reals)
	print("\nmängden stationära punkter för expr")
	sp.pprint(expr)
	return stationar

def inflexion(expr, x):
	derivata = sp.diff(expr, x)
	andra_derivata = sp.diff(derivata, x)
	inflexion_punkt = sp.solveset(andra_derivata, x, domain=sp.Reals)
	print("inflexionspunkter for expr")
	return inflexion_punkt

print("STATIONÄRA PUNKTER")
sp.pprint(stationar(x + sp.cos(x), x))
sp.pprint(stationar(100*x + 200*sp.sin(x), x))
sp.pprint(stationar(sp.sqrt(3*x) + 2*sp.sin(x), x))
sp.pprint(stationar(sp.E**-x*sp.sin(2*x), x))


print("INFLEXIONSPUNKTER")
sp.pprint(inflexion(x**3 - x**2, x))
sp.pprint(inflexion(x**4 - x**2, x))
sp.pprint(inflexion(sp.sin(2*x), x))
sp.pprint(inflexion(sp.sin(sp.log(x)), x))

#expr är deriverbar minst två gånger överallt

#andra derivatan = 0