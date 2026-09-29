
import numpy as np
import ast

def solve_second_degree(polynom):
	if (len(polynom) != 3 or polynom[-1] == 0):
		print("inte ett andragradspolynom")
		return []
	roots = np.roots(list(reversed(polynom)))
	if (np.isreal(roots).any()):
		roots = roots.tolist()
		if (roots[0] == roots[1]):
			roots.pop(1)
		return roots
	else: 
		return []


f = open("Andragradspolynom.txt")
line = f.readline()
poly_list = ast.literal_eval(line)
f.close()

solutions = []
for p in poly_list:
	solutions.append(solve_second_degree(p))
solution_string = str(solutions)
f = open("solutions.txt", 'w')
f.write(solution_string)
f.close()