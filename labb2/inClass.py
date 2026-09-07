#en kodcell 

#FRÅGA 1
# import math

# grans = int(input("mata in ett positivt heltal:"))
# s = 0
# i = 1

# while s < grans:
# 	i += 1
# 	s += math.log(i)
# 	print("s: ", s)

#FRÅGA 2

import random

antal = int(input("mata in positivt heltal: "))

random_list = []
s = 0


for i in range(antal):
	rand_num = random.randint(1,100)
	random_list.append(rand_num)
	print(f"Tal nr {i+1} är {rand_num}")
	s += rand_num

m = s/antal
print("summan är {s}")
print("medelvärdet är", round(m,2))


# FRÅGA 3
# import random 

# A = set({})
# B = set({})

# while len(A) < 20:
# 	A.add(random.randint(1,100))

# while len(B) < 20:
# 	B.add(random.randint(1,100))

# print("A: ", A)
# print("\nB: ",B)

# print("Unionen av A och B är", A.union(B))
# print("Snittet av A och B är", A.intersection(B))



# %%