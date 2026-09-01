"""
1. Skriv kod som tilldelar tre variabler heltalsvärden. 
Därefter ska koden skriva ut det största värdet, det minsta värdet och medelvärdet med förklarande text.
"""

import statistics

a = 10
b = 33
c = 2

print("values:", a, b, c)

print("biggest value: ", max(a, b, c))
print("smallest value: ", min(a, b, c))
print("medelvärde: ", statistics.mean([a, b, c]))

