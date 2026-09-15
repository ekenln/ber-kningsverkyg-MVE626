import math

def sqrt(n):
    if n < 0:
        return "Kan inte beräkna rot ur negativt tal"
    x = 1
    x_prev = 0
    iterations = 0
    while abs(x-x_prev) > 1e-10:
        x_prev = x
        x = (x_prev + n/x_prev)/2
        iterations += 1
    # print(iterations)
    return x

inp = float(input("Mata in ett positivt tal för att ta reda på dess rot: "))

sqrt = sqrt(inp)

print(f"Skillnad mellan egen funktion och math-funktion: \n {sqrt} - {math.sqrt(inp)} = {sqrt - math.sqrt(inp)}")