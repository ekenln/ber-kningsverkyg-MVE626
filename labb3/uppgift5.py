import numpy as np

def add(pol1, pol2):
    if len(pol1) < len(pol2):
        pol1 = pol1 + [0]*int(len(pol2) - len(pol1))
    elif len(pol2) < len(pol1):
        pol2 = pol2 + [0]*int(len(pol1) - len(pol2))

    return np.add(pol1, pol2)    

def multiply(pol1, pol2):
    res = [0]*int((int(len(pol1)))+int(len(pol2)-1))
    for i in range(len(pol1)):
        for j in range(len(pol2)):
            pos = i + j
            val = pol1[i]*pol2[j]
            res[pos] += val
    return res

def derivative(pol):
    pol = pol[1:]
    for i in range(len(pol)):
        pol[i] = (i+1)*pol[i]
    return pol

def isequal(pol1, pol2):
    if len(pol1) != len(pol2):
        return False
    for i in range(len(pol1)):
        if pol1[i] != pol2[i]:
            return False
    return True

pol1, pol2 = [1, 0, -1, 0, 0, 1], [3,1,2]
print(add(pol1, pol2))
print(multiply(pol1, pol2))
print(derivative(pol1))
print(derivative(pol2))
print(isequal(derivative(multiply(pol1, pol2)), add(multiply(pol1, derivative(pol2)), multiply(derivative(pol1), pol2))))