import numpy as np
import matplotlib.pyplot as plt

#UPPGIFT 2
#använder len(polynom) - 1 för attfå ut graden av polynomet
#skapar en lista x med alla x värden där polynomet ska räknas ut och plottas. 

def plotta_polynom(polynom, start, slut):
	x = np.linspace(start , slut, 2 + (len(polynom)-1) * 5 * (slut-start))
	plt.plot(x, np.polynomial.polynomial.polyval(x, polynom), 'g:.')
	plt.show()


plotta_polynom([0, 0, 1, 1], -1, 1)