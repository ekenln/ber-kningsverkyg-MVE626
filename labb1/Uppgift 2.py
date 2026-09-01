import math

# sin(x) = 0.2 => x1 = arcsin(0.2), x2 = pi-arcsin(0.2)
print("sin(x) = 0.2 => SVAR: x1 =", math.asin(0.2), "rad , x2 = ", math.pi-math.asin(0.2), " rad")

# tan(x) = 6 => x = arctan(6)
print("tan(x) = 6 => SVAR:  x = ", math.atan(6))

# cos(x) = 2 => x = arccos(2)
print("cos(x) = 2 => SVAR: x saknar lösning eftersom cos(x) ∈ [-1, 1]")

# ln(x) + ln(2x) = 3 => ln(2x^2) = 3 => 2x^2 = e^3 => x = sqrt((e^3)/2)
print("ln(x) + ln(2x) = 3 => SVAR: x1 = ", math.sqrt(math.e**3/2))

# e^2x - 5e^x = -6 => "e^2x - 5e^x = -6 => (e^x)^2 - 5e^x + 6 = 0. Ersätt e^x=t => t^2-5t+6=0 => (t-3)(t-2)=0 => t1=3, t2=2 => x1= ln(3), x2= ln(2)."
print("e^2x - 5e^x = -6 => (e^x)^2 - 5e^x + 6 = 0. Ersätt e^x=t => t^2-5t+6=0 => (t-3)(t-2)=0 => t1=3, t2=2 => SVAR: x1= ln(3)= %f, x2= ln(2) = %f." % (math.log(3), math.log(2))) 