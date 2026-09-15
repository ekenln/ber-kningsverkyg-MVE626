import numpy as np
import math

def add(pol1, pol2):

    if len(pol1) < len(pol2):
        pol1 = pol1 + [0]*int(len(pol2) - len(pol1))
    elif len(pol2) < len(pol1):
        pol2 = pol2 + [0]*int(len(pol1) - len(pol2))
    print(pol1, pol2)

    return np.add(pol1, pol2)
#print(add([1, 0, -1, 0, 0, 1], [3, 1, 2]))
    

def multiply(pol1, pol2):
    res = [0]*int((int(len(pol1)))+int(len(pol2)-1))
    for i in range(len(pol1)):
        for j in range(len(pol2)):
            pos = i + j
            val = pol1[i]*pol2[j]
            res[pos] += val
    return res
print(multiply([1, 0, -1, 0, 0, 1], [3, 1, 2]))


def derivative(pol):
    pol = pol[1:]
    n=1
    for i in range(len(pol)):
        pol[i] = n*pol[i]
        n+=1
    return pol
#print(derivative([1, 0, -1, 0, 0, 1]))

def isequal(pol1, pol2):
    if len(pol1) != len(pol2):
        return False
    for i in range(len(pol1)):
        if pol1[i] != pol2[i]:
            return False
    return True