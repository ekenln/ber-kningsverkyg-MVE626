import math

# sin(x) = 0.2 => x1 = arcsin(0.2)
print("sin(x) = 0.2 => x1 =", math.asin(0.2), "rad , x2 = ", math.pi-math.asin(0.2), " rad")

# tan(x) = 6 => x = arctan(6)
print("tan(x) = 6 => x = ", math.atan(6))

# cos(x) = 2 => x = arccos(2)
print("cos(x) = 2 => x saknar lösning då cos(x) ∈ [-1, 1]")

# ln(x) + ln(2x) = 3 => ln(2x^2) = 3 => 2x^2 = e^3 => x = ± sqrt((e^3)/2)
print("ln(x) + ln(2x) = 3 => x1 = ", math.sqrt(math.e**3/2), ", x2 = ", -1*math.sqrt(math.e**3/2))

# e^2x - 5e^x = -6 => e^x*(e^2-5) = -6 => e^x = -6/(e^2-5) => x = ln(-6/(e^2-5)) => saknar lösning då ln(x) ∈ [0, ∞) för x ∈ ℝ.
print("e^2x - 5e^x = -6 => e^x*(e^2-5) = -6 => e^x = -6/(e^2-5) => x = ln(-6/(e^2-5)). e^2-5 > 0 => -6/(e^2-5) < 0 => ln(-6/(e^2-5)) saknar lösning då ln(x) ∈ [0, ∞) för x ∈ ℝ.")