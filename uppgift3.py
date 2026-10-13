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
    print(f'N = 10^{i}: {trapetsmetoden(f, 0, 0, 10**i)} - 1.8519370519824662 = {trapetsmetoden(f, 0, np.pi, 10**i)-1.8519370519824662}')

# Liknande går inte att göra för f = 1/x eftersom det första värdet i trapetsen är oändligt stort.

# Ingen enorm skillnad på mittpunkts- och trapetsmetoden, men mittpunktsmetoden är mer flexibel för olika funktioner och ger en extra korrekt värdesiffra

# a > b ger rätt resultat eftersom h blir negativt. 
# a = b ger rätt resultat eftersom bredden blir 0