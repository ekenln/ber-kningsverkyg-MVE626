import numpy as np

def korsar_x_axeln(k, m):
	try: 
		x = -m/k
		return x
	except:
		return "inget svar"

korsar_x_axeln = np.frompyfunc(korsar_x_axeln, 2, 1)

print(korsar_x_axeln([1, 2, 0], [1, 0, 1]))
