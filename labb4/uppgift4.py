import numpy as np
import matplotlib.pyplot as plt
import math


#UPPGIFT 4

# har en while loop så att vi fortsätter fråga om input tills användaren har matat in ett positivt heltal
# antingen så kommer input() att kasta ett error och så fångas det upp av except eller om det är en int men den är 
#negativ fångar vi upp det genom att kolla om inmatningen är positiv och bryter ur while loopen
while True:
	try:
		heltal = int(input("mata in ett heltal: "))
		if heltal >= 0:
			break
		else:
			print("endast heltal tillåtet")
	except ValueError:
		print("endast heltal tillåtet")

#en universell funktion för att kunna räkna ut cos(x) av flera värden och få tillbaka en lista med punkter av y = cos(x)
cos = np.frompyfunc(np.cos, 1, 1)

#lista med x värden att beräkna i intervallet -pi, pi
x = np.linspace(-math.pi, math.pi)

#lista med k-värden för att räkna ut summan i maclaurinpolynomet
n = np.arange(0, np.floor(heltal/2)+1, 1)

#samlar alla summor i maclaurin_points för de olika x värdena och lägger till i en lista 
def maclaurin(x):
	maclaurin_points = []
	for j in x:
		y = 0
		for i in n:
			y += (-1)**i * (j**(2*i)/(math.factorial(int(2*i))))
		maclaurin_points.append(y)
	return maclaurin_points
		
maclaurin_points = maclaurin(x)
cos_res = cos(x)

#plottar graferna för x värdena och y värdena som beräknats och har nycklar för plt.legend()
plt.plot(x , maclaurin_points, 'g:.', label=f"maclaurinpolynom av grad {heltal}")
plt.plot(x , cos_res, 'r:.', label="cos(x)")
plt.legend()

plt.show()