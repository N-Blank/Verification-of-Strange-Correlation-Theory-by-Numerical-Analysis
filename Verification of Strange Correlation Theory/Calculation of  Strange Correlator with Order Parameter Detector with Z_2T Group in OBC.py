import numpy as np
import matplotlib.pyplot as plt
from itertools import product

# G is our Z2T group
# N is the size of the system N != (4n + 2) or determinant = 0
# d is the distance between two operators
# confs is all configurations
G = [0, 1]
N = 12
confs = list(product(G, repeat=N))

d_values = range(N)
strange_values = []

for d in d_values:
    strange = 0
    numer = 0
    deter = 0
    for conf in confs:
        coefficient = 1
        for i in range(N):
            if conf[i] != conf[(i + 1) % N]:
                coefficient *= 1j
        deter += coefficient
        if conf[0] != conf[d]:
            coefficient *= -1
        numer += coefficient
    strange_values.append(numer / deter)

# Plotting the values
plt.plot(d_values, strange_values)
plt.xlabel('d')
plt.ylabel('strange')
plt.title('Plot of strange vs. d')
plt.grid(True)
plt.show()
