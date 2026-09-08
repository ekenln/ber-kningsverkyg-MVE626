
"""
Skriv ett program som frågar efter ett positivt heltal n 
och som sedan beräknar den harmoniska summan upp till n 
"""

import math

n = int(input("mata in ett positivt heltal:"))

if n < 0:
	print("endast positiva heltal är tillåtet")
	exit()

summa = 0
i = 1

#beräknar harmonisk summa
while i <= n:
	summa += 1/i
	i += 1

print(f"den harmoniska summan när i går mot {n} är {summa}")

# här beräknar vi differansen mellan den harmoniska summan i 10 potenser upp til 1e7 med ln(n)
i = 10
while i <= 1e7:
	j = 1
	summa = 0
	while j <= i:
		summa += 1/j
		j += 1
	print(f"differansen är: {summa - math.log(i)}")
	i *= 10


#här ser vi att differensen rör sig mot ett gränsvärde -> eulers konstant, 0.57721...
#att det finns ett gränsävrde tyder på att de är asymptoter
