"""
Skriv kod som ber användaren att mata in ett tal r. 
Därefter ska koden skriva ut vad omkrets och area blir av en cirkel med radien r 
(med förklarande text) samt vad area och volym blir av ett klot med radien r.
"""

import math

"""
omkrets: 2pir
volym klot: 4pir^3/3
area klot: : 4pir^2
"""

r = float(input("skriv in en radie: "))

if r > 0:
	omkrets = round(2 * math.pi * r, 4)
	volym = round((4 * math.pi * math.pow(r,3)) / 3, 4)
	area = round(4 * math.pi * r**2, 4)

	print("omkrets av en cirkel med radie:", r, "är:", omkrets)
	print("volym av ett klot med radie:", r, "är:", volym)
	print("Area av ett klot med radie:", r, "är:", area)

else:
	print("fel: behöver positiv input")


