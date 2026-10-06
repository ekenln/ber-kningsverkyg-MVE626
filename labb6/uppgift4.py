import sympy as sp

def maxmin(expr, x, start, end):

    # Börjar med xmin0 och xmax0 -> Kommer uppdateras till xmin och xmax
    xmin0, xmax0 = set({}), set({})

    # Börjar med ymin som -inf och ymax som inf för att kunna jämföra
    ymin, ymax = sp.oo, -1*sp.oo

    # Gör en checklista med tal som ska kollas om de ger minst/störst värde i funktionen
    check_list = [start, end]

    # Lägger till stationära punkter i checklistan
    check_list.extend(list(sp.solveset(expr.diff(), x, domain=sp.S.Reals)))
    
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

# Funktionen misslyckas med nedanstående funktion
# f = 3*sp.pi*x + 6*sp.sin(sp.pi*x)
# print(maxmin(f, x, 0, 1))

f = (x+2)/(x+1)
print(maxmin(f, x, 0, 1))

f = x**3 - x**2
print(maxmin(f, x, sp.Rational(-1,3), 1))