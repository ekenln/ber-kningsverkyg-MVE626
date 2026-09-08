# I programmet undersöker vi hur många termer, n, som behövs för att summan av 1/i^2 för i mellan 1 och n 
# ska vara nära pi^2/6 med en felmarginal mindre än eta, som användaren matar in

import math

# Ber användaren mata in ett litet värde eta
eta = float(input("Mata in ett litet värde, eta: "))

sum = 0
i = 0

# Använder while-loop för att stoppa när kriteriet är uppnått
while abs(sum - (math.pi**2)/6) > eta:
    i += 1 # Ett steg framåt per iteration
    sum += 1/(i**2) # Adderar 1/i^2 till summan

print(f"För att differensen mellan pi^2/6 och summan av 1/i^2 för i mellan 1 och n ska vara mindre än eta behövs n={i} termer")