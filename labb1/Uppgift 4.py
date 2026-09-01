import math

x = float(input("x = "))
y = float(input("y = "))

r = math.sqrt(x**2 + y**2)

if x>0:
    p = math.atan(y/x)
elif x==0:
    if y>=0:
        p = math.pi/2
    if y<0:
        p = -1*math.pi/2
else:
    p = math.pi + math.atan(y/x)

if p<0:
    p+=2*math.pi

p = math.degrees(p)

print("radie = ", r, ", vinkel = ", p, "°")