import sympy as sp

def maxmin(expr, x, start, end):

    xmin0, xmax0 = set({}), set({})
    ymin, ymax = sp.oo, -1*sp.oo
    check_list = [start, end]

    check_list.extend(list(sp.solveset(expr.diff(), x, domain=sp.S.Reals)))
    for i in check_list: 
        test = expr.subs(x, i)
        if test <= ymin:
            ymin = test
            xmin0.add(i)
        if test >= ymax:
            ymax = test
            xmax0.add(i)

    xmin, xmax = set({}), set({})
    for i in xmin0:
        if expr.subs(x, i) == ymin:
            xmin.add(i)

    for i in xmax0:
        if expr.subs(x, i) == ymax:
            xmax.add(i)

    return [xmin, ymin, xmax, ymax]

x = sp.symbols('x')
f = x*(1-x)
print(maxmin(f, x, 0, 1))

f = x**2*(1-x)**2
print(maxmin(f, x, 0, 1))

# f = 3*sp.pi*x + 6*sp.sin(sp.pi*x)
# print(maxmin(f, x, 0, 1))

f = (x+2)/(x+1)
print(maxmin(f, x, 0, 1))

f = x**3 - x**2
print(maxmin(f, x, sp.Rational(-1,3), 1))