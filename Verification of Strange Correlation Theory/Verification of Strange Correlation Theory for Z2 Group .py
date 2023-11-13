import numpy as np
import sys
from itertools import product

# G is our Z2 group
# N is the size of the system N != (4n + 2) or deternimnator = 0
# d is the distance between two operators
# confs is all configurations
G = [0, 1]
N = 5
confs = list(product(G, repeat = N * N))

def v2(g1, g2, g3):
    if (g1, g2, g3) in [(0, 0, 0), (1, 1, 1), (0, 1, 1), (1, 0, 0), (0, 0, 1), (1, 1, 0)]:
        return 1
    elif (g1, g2, g3) in [(1, 0, 1), (0, 1, 0)]:
        return -1
    else:
        return None  # Return None if input combination doesn't match any defined values

for d in range(N):
    numer = 0
    deter = 0
    for conf in confs:
        coefficient = 1
        print(conf[1])
        for j in range(N):
            for i in range(N):  
                coefficient *= v2(conf[N * j + i], conf[N * (j + 1)%N + i], conf[N * (j + 1)%N + (i + 1)%N]) * v2(conf[N * j + i], conf[N * j + (i + 1)%N], conf[N * (j + 1)%N + (i + 1)%N])
                print(coefficient)
        deter += coefficient
        if conf[0] != conf[d - 1]:
            coefficient *= -1
        else:
            coefficient *= 1
        numer += coefficient
    print(f"numer ({d}) = {numer}")  
    print(f"deter ({d}) = {deter}")  
    print(f"strange ({d}) = {numer/deter}")  