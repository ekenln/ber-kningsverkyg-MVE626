import sympy as sp
import matplotlib.pyplot as plt
from collections import Counter

def draw_pi(n):
	print(sp.pi.evalf(n))
	pi_n = sp.pi.evalf(n+3) #extra decimaler för att få rätt avrundning vid n
	
	#gör om till sträng för att kunna iterera lättare o se varje decimal
	pi_str = str(pi_n)
	decimals = []
	for c in pi_str:
		if c.isdigit():
			decimals.append(int(c))
	count = Counter(decimals[1:-2])

	#plotta utifrån dictionary count
	plt.bar(count.keys(), count.values(), color='blue')
	plt.title('förekommande av nummer')
	plt.show()

draw_pi(100)



