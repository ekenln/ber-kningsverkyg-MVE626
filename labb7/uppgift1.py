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