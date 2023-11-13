import numpy as np
import sys
from itertools import product

# G is our Z2T group
# N is the size of the system N != (4n + 2) or deternimnator = 0
# d is the distance between two operators
# confs is all configurations
G = [0, 1]
N = 12
confs = list(product(G, repeat=N))


for d in range(N):
    strange = 0
    numer = 0
    deter = 0
    for conf in confs:
        coefficient = 1
        for i in range(N):  
            if conf[i] != conf[(i + 1)%N]:
                coefficient *= 1j
        deter += coefficient
        if conf[0] != conf[d]:
            coefficient *= -1
        else:
            coefficient *= 1
        numer += coefficient
    print(f"strange ({d}) = {numer/deter}")  
