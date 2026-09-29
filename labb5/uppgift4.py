import matplotlib.pyplot as plt
import math
import numpy as np
from pathlib import Path
base_dir = Path(__file__).parent
file_path = base_dir / 'primes.txt'

primes = []
with open(file_path) as f:
    for row in f:
        row_numbers = list(map(int, row.split()))
        primes.extend(row_numbers)

x_list = []
y_list = []

for i in primes:
    y = math.floor(i/100)
    y_list.append(y)
    x = i - y*100
    x_list.append(x)

colors = np.random.rand(1000)

plt.scatter(x_list, y_list, s=5, c=colors)
plt.title('Första 1000 primtalen')
plt.xlabel('Entals- och tiotalsdel')
plt.ylabel('Tusen- och hundratalsdel')
plt.show()