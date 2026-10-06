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



