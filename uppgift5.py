"""
Undersök om följande gränsvärden kan existera och vad de skulle kunna vara genom att beräkna följande 
funktioner för värden nära de angivna in-värdena där de inte är definierade.
"""

import math

limit_pos = 1e-6
limit_n = -1e-6


limit1 = math.sin(limit_pos) / limit_pos
limit2 = math.sin(limit_n) / limit_n

print("beräkningar med ett positivt- och negativt värde nära de värdena där de inte är definierade, " \
"om de verkar gå mot samma värde kan vi tänka att det kanske är ett gränsvärde")

print("\nberäkning för sin(x)/x när x->0")
print("från stort", limit1)
print("från litet", limit2)

limit1 = math.log(1 + limit_pos) / limit_pos
limit2 = math.log(1 + limit_n) / limit_n

print("\nberäkning för ln(1+x) / x när x->0:")
print("från stort", limit1)
print("från litet", limit2)

limit1 = math.sin(1 / limit_pos)
limit2 = math.sin(1 / limit_n)

print("\nberäkning för sin(1/x) när x->0")
print("från stort", limit1)
print("från litet", limit2)

limit1 = (1 - math.cos(limit_pos)) / (limit_pos**2)
limit2 = (1 - math.cos(limit_n)) / (limit_n**2)

print("\nberäkning (1-cos(x)) / x^2 när x->0")
print("från stort", limit1)
print("från litet", limit2)
