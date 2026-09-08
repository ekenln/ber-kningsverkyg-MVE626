# I programmet får användaren mata in två sidlängder i en triangel samt vinkeln mellan dessa.
# Programmet avgör om triangeln är liksidig, likbent eller oliksidig

import math

a = float(input("Mata in första sidlängd a i en triangel: "))
b = float(input("Mata in andra sidlängd b i en triangel: "))
v =  float(input("Mata in vinkeln v i grader mellan sidor a och b: "))

# Använder cosinussatsen för att räkna ut längden på den tredje sidan c
c = math.sqrt(a**2+b**2-2*a*b*math.cos(math.radians(v)))

# Använder math.isclose för att avgöra om sidlängderna är lika
if math.isclose(a, b, rel_tol=1e-10) and math.isclose(b, c, rel_tol=1e-10): # Avgör om alla sidlängder är lika => liksidig
    print("Triangeln är liksidig")
elif  math.isclose(a, b, rel_tol=1e-10) or math.isclose(b, c, rel_tol=1e-10) or math.isclose(c,a, rel_tol=1e-10): # Avgör om två sidlängder är lika => likbent
    print("Triangeln är likbent")
else: # Om triangeln inte uppfyller något av tidigare kriterier är den oliksidig
    print("Triangeln är oliksidig")

