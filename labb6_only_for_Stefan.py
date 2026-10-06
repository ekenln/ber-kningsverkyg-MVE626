#%% Uppgift 1
import sympy as sp
import matplotlib.pyplot as plt
from collections import Counter

def draw_pi(n):
	# print(sp.pi.evalf(n))
	pi_n = sp.pi.evalf(n+3) #extra decimaler för att få rätt avrundning vid n

	#gör om till sträng för att kunna iterera lättare o se varje decimal
	pi_str = str(pi_n)
	decimals = [] 
	for c in pi_str:
		if c.isdigit():
			decimals.append(int(c))
	#lagt i lista för att ordna nummer och ger till inbyggd function som skapar som en dictionary med key: numret och value: förekomsten
	count = Counter(decimals[1:-2])

	#plotta utifrån dictionary count
	plt.bar(count.keys(), count.values(), color='blue') 
	plt.title('Förekomst av siffror i Pi')
	plt.show()

for i in [10, 100, 1000, 10000, 100000]:
	draw_pi(i)

#%% Uppgift 2
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

#%% Uppgift 3
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

#%% Uppgift 4
import sympy as sp

def maxmin(expr, x, start, end):

    # Börjar med xmin0 och xmax0 -> Kommer uppdateras till xmin och xmax
    xmin0, xmax0 = set({}), set({})

    # Börjar med ymin som -inf och ymax som inf för att kunna jämföra
    ymin, ymax = sp.oo, -1*sp.oo

    # Gör en checklista med tal som ska kollas om de ger minst/störst värde i funktionen
    check_list = [start, end]

    # Lägger till stationära punkter i checklistan. Sätter domänen till intervallet mellan start och end för att funktionen inte ska krascha med funktioner som har oändligt många stationära punkter
    check_list.extend(list(sp.solveset(expr.diff(), x, domain=sp.Interval(start, end))))
    
    # Går igenom checklistan och redigerar ymin och ymax därefter. Lägger till värden i xmin0 och xmax0 för att gå igenom senare
    for i in check_list: 
        test = expr.subs(x, i)
        if test <= ymin:
            ymin = test
            xmin0.add(i)
        if test >= ymax:
            ymax = test
            xmax0.add(i)

    # Gör nya xmin och xmax för att bara få med korrekta värden
    xmin, xmax = set({}), set({})

    # Går igenom xmin0 och lägger bara till min-värdena i xmin
    for i in xmin0:
        if expr.subs(x, i) == ymin:
            xmin.add(i)

    # Går igenom xmax0 och lägger bara till max-värdena i xmax
    for i in xmax0:
        if expr.subs(x, i) == ymax:
            xmax.add(i)

    return [xmin, ymin, xmax, ymax]

# Nedan går vi igenom testerna för uppgiften. 

x = sp.symbols('x')
f = x*(1-x)
print(maxmin(f, x, 0, 1))

f = x**2*(1-x)**2
print(maxmin(f, x, 0, 1))

f = 3*sp.pi*x + 6*sp.sin(sp.pi*x)
print(maxmin(f, x, 0, 1))

f = (x+2)/(x+1)
print(maxmin(f, x, 0, 1))

f = x**3 - x**2
print(maxmin(f, x, sp.Rational(-1,3), 1))

#%% Uppgift 5

import sympy as sp

x = sp.symbols('x')

def largest_power_with_limit_at_zero(f, x):
	a = 0
	limes = sp.limit(f/x**a, x, 0) #kollar första för a == 0, alltså f
	if (sp.Abs(limes) == sp.oo): #om absoluta gränsvärdet där a == 0 är oändligheten ser vi att den är divergent, inget a fungerar
		return sp.nan
	while (limes == 0): #fortsätt så länge gränsvärdet ger 0, f är fortfarande mindre än x^a, kan testa högre a
		a = a + 1
		if a >= 100: #efter 100 gånger så 
			return sp.oo
		limes = sp.limit(f/x**a, x, 0)
		if sp.Abs(limes) == sp.oo: #om vi får att det hoppar så det går direkt till oändligheten ser vi att a är för stort. Förra a var största godkända 
			return a-1
	return a #limes nollskilt men inte heller går mot oändligheten (ändligt) -> bryter ur while loopen och returnerar a

print(largest_power_with_limit_at_zero(sp.sqrt(x), x))
print(largest_power_with_limit_at_zero(1/x, x))
print(largest_power_with_limit_at_zero(sp.sin(x), x))
print(largest_power_with_limit_at_zero(1 - sp.cos(x) + sp.log(1-x**2)/2, x))
print(largest_power_with_limit_at_zero(sp.exp(-1/x**2), x))