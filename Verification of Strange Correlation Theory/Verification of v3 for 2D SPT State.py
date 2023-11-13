import numpy as np
import sys
from itertools import product

G = [0, 1, 2, 3]

def v2(g0, g1, g2):
    if (g0 == g1 or g1 == g2):
        return 1
    elif (g0 == g2):
        return 1j
    # elif (g0, g1, g2) in [(0, 2, 3), (0, 1, 3), (1, 3, 2), (1, 0, 2), (2, 0, 1), (2, 3, 1), (3, 1, 0), (3, 2, 0)]:
    #     return -1
    # elif (g0, g1, g2) in [(0, 2, 1), (0, 3, 1), (1, 3, 0), (1, 2, 0), (2, 0, 3), (2, 1, 3), (3, 1, 2), (3, 0, 2)]:
    #     return -1
    # elif (g0, g1, g2) in [(0, 1, 2), (0, 3, 2), (1, 0, 3), (1, 2, 3), (2, 3, 0), (2, 1, 0), (3, 2, 1), (3, 0, 1)]:
    #     return -1j
    # elif (g0, g1, g2) in [(0, 1, 2), (0, 2, 3), (0, 3, 1), (1, 0, 3), (1, 3, 2), (1, 2, 0), (2, 3, 0), (2, 0, 1), (2, 1, 3), (3, 2, 1), (3, 1, 0), (3, 0, 2)]:
    #     return 1j ** 0.5
    # else:
    #     return 1j ** 0.5
    else:
        return 1j ** 0.5

for g0 in G:
    for g1 in G:
        for g2 in G:
            for g3 in G:
                for g4 in G:
                    dv2 = v2(g1, g2, g3) * v2(g0, g1, g3) / (v2(g0, g2, g3) * v2(g0, g1, g2)) 
                    if (dv2 != 1):print(g0, g1, g2, g3,  dv2)
        