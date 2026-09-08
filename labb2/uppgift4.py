
import math

"""
Fn = Fn-1 + Fn-2
for n > 1"""

fib = [0, 1]

for i in range(2,100):
	fib.append(fib[-1] + fib[-2])


#Här kan ve se att listan innehåller 100 tal och att det sista är det korrekta 
print(f"antal tal i listan: {len(fib)} inledning är {fib[0], fib[1]} och det 100e talet: {fib[99]}")

fib_rest2 = []
fib_rest3 = []
fib_rest5 = []
fib_rest7 = []

for num in fib:
	fib_rest2.append(num % 2)
	fib_rest3.append(num % 3)
	fib_rest5.append(num % 5)
	fib_rest7.append(num % 7)


print(f"\nrest med div 2: {fib_rest2}")
print(f"\nrest med div 3: {fib_rest3}")
print(f"\nrest med div 5: {fib_rest5}")
print(f"\nrest med div 7: {fib_rest7}")

"""
det vi kan se är att iom att fibonaccis serie är divergent och består av "par" alltså att de två föregående blir nästa tal
blir även resterna som en fibonacciserie fast med modulo av det talet som resten beräknas och eftersom det finns ett begränsat antal par kommer serien att upprepa sig
"""