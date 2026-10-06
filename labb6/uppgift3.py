import sympy as sp

x = sp.symbols('x')

def stationar(expr, x):
	derivata = sp.diff(expr, x) #tar ut första derivatan för att kunna hitta stationära punkter
	punkter = sp.solveset(derivata, x, domain=sp.S.Reals) #returnerar en mängd av punkter där derivata == 0
	print("\nstationära punkter för")
	sp.pprint(expr)
	return punkter

def inflexion(expr, x):
	derivata = sp.diff(expr, x)
	andra_derivata = sp.diff(derivata, x) #deriverar 2 ggr för att hitta inflexionspunkter, antar att funktionen är derviverbar 2 ggr
	inflexion_punkt = sp.solveset(andra_derivata, x, domain=sp.S.Reals) 
	print("\ninflexionspunkter för")
	sp.pprint(expr)
	return inflexion_punkt

print("STATIONÄRA PUNKTER")
sp.pprint(stationar(x + sp.cos(x), x))
sp.pprint(stationar(100*x + 200*sp.sin(x), x))
sp.pprint(stationar(sp.sqrt(3*x) + 2*sp.sin(x), x)) #solveset kan ge falsk mängd. ger lösningar till ett kvadrerat uttryck. 
sp.pprint(stationar(sp.E**-x*sp.sin(2*x), x))

print("\nINFLEXIONSPUNKTER")
sp.pprint(inflexion(x**3 - x**2, x))
sp.pprint(inflexion(x**4 - x**2, x))
sp.pprint(inflexion(sp.sin(2*x), x))
sp.pprint(inflexion(sp.sin(sp.ln(x)), x)) #löser dåligt eftersom ln i sin uttrycket och solveset inte kan substitutera och sedan lösa med ln(x)
