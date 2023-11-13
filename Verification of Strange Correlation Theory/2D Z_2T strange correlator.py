import numpy as np
import sys
from itertools import product

# G is our Z2 group
# N is the size of the system N != (4n + 2) or deternimnator = 0
# d is the distance between two operators
# confs is all configurations
G = [0, 1]
N1 = 8
N2 = 3
confs = list(product(G, repeat = N1 * N2))
print(f"{N1}*{N2} system")

def v2(g1, g2, g3):
    if (g1, g2, g3) in [(0, 0, 0), (1, 1, 1)]:
        return 1
    elif (g1, g2, g3) in [(0, 1, 1), (1, 0, 0), (0, 0, 1), (1, 1, 0)]:
        return -1
    elif (g1, g2, g3) in [(0, 1, 0)]:
        return 1j
    elif (g1, g2, g3) in [(1, 0, 1)]:
        return -1j
    else:
        return None  # Return None if input combination doesn't match any defined values

for d in range(N1 + 1):
    numer = 0
    deter = 0
    for conf in confs:
        coefficient = 1
        for j in range(N2):
            for i in range(N1):  
                coefficient *= v2(conf[N1 * j + i], conf[N1 * (j + 1)%N2 + i], conf[N1 * (j + 1)%N2 + (i + 1)%N1]) * v2(conf[N1 * j + i], conf[N1 * j + (i + 1)%N1], conf[N1 * (j + 1)%N2 + (i + 1)%N1]).conjugate()
        deter += coefficient
        if conf[0] != conf[d - 1]:
            coefficient *= -1
        else:
            coefficient *= 1
        numer += coefficient
    print(f"strange ({d}) = {numer/deter}")