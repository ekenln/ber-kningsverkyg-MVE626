"""
Undersök om följande gränsvärden kan existera och vad de skulle kunna vara genom att beräkna följande 
funktioner för värden nära de angivna in-värdena där de inte är definierade.
"""

import math

limit_pos = 2.22e-6
limit_n = -2.22e-6


limit1 = math.sin(limit_pos) / limit_pos
limit2 = math.sin(limit_n) / limit_n

print("gränsvärde för sin(x)/x när x->0")
print("från stort", limit1)
print("från litet", limit2)

limit1 = math.log(1 + limit_pos) / limit_pos
limit2 = math.log(1 + limit_n) / limit_n

print("\ngränsvärde för ln(1+x) / x när x->0:")
print("från stort", limit1)
print("från litet", limit2)

limit1 = math.sin(1 / limit_pos)
limit2 = math.sin(1 / limit_n)

print("\ngränsvärde för sin(1/x) när x->0")
print("från stort", limit1)
print("från litet", limit2)

limit1 = (1 - math.cos(limit_pos)) / (limit_pos**2)
limit2 = (1 - math.cos(limit_n)) / (limit_n**2)

print("\ngränsvärde (1-cos(x)) / x^2 när x->0")
print("från stort", limit1)
print("från litet", limit2)
