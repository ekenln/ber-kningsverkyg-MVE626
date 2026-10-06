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