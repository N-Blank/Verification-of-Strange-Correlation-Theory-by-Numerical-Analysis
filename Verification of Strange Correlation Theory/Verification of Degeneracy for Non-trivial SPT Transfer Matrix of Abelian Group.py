# import numpy as np

# G = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
# tab = np.zeros((9, 9), dtype=object)  # 创建一个9x9的全零矩阵
# T = np.zeros((9, 9), dtype=object)

# for i in range(9):
#     for j in range(9):
#         for k in range(9):
#             if(G[k] == [(G[i][0] + G[j][0]) % 3, (G[i][1] + G[j][1]) % 3]):
#                 tab[i][j] = k + 1

# # 输出tab矩阵内容
# for row in tab:
#     print(row)

# print("\n")


# x = -0.5 + (3 ** 0.5)/2j
# for i in range(9):
#     for j in range(9):
#         for k in range(9):
#             T[i][tab[i][j] - 1] = x ** (G[i][0] * G[j][1])

# for row in T:
#     print(row)

# import numpy as np

# G = [[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [1, 2], [1, 3], [2, 0], [2, 1], [2, 2], [2, 3], [3, 0], [3, 1], [3, 2], [3, 3]]
# tab = np.zeros((16, 16), dtype=int)
# T = np.zeros((16, 16), dtype=complex)

# for i in range(16):
#     for j in range(16):
#         for k in range(16):
#             if G[k] == [(G[i][0] + G[j][0]) % 4, (G[i][1] + G[j][1]) % 4]:
#                 tab[i][j] = k + 1

# # Output the tab matrix content
# for row in tab:
#     print(row)

# print("\n")

# x = 1j
# for i in range(16):
#     for j in range(16):
#         for k in range(16):
#             T[i][tab[i][j] - 1] = x ** (G[i][0] * G[j][1])

# for row in T:
#     print(row)

# eva, evt = np.linalg.eig(T)
# print("Matrix T:\n{}".format(T))
# print("---------------------------------------")
# print("Eigenvalues of matrix T:\n{}".format(eva))
# print("Eigenvectors of matrix T:\n{}".format(evt))

import numpy as np

G = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5]]
tab = np.zeros((18, 18), dtype=int)
T = np.zeros((18, 18), dtype=complex)

for i in range(18):
    for j in range(18):
        for k in range(18):
            if G[k] == [(G[i][0] + G[j][0]) % 3, (G[i][1] + G[j][1]) % 6]:
                tab[i][j] = k + 1

# Output the tab matrix content
for row in tab:
    print(row)

print("\n")

x = -0.5 - (3 ** 0.5)/2j
for i in range(18):
    for j in range(18):
        for k in range(18):
            T[i][tab[i][j] - 1] = x ** (G[i][0] * G[j][1])

for row in T:
    print(row)

eva, evt = np.linalg.eig(T)
print("Matrix T:\n{}".format(T))
print("---------------------------------------")
print("Eigenvalues of matrix T:\n{}".format(eva))
#print("Eigenvectors of matrix T:\n{}".format(evt))


   
from sympy import Matrix, symbols

# Create a SymPy matrix
M = Matrix(T)
#print("Matrix: {}".format(M))

# Use the diagonalize() method
P, D = M.diagonalize()

#print("Diagonal of a matrix: {}".format(D))
if (M.is_diagonalizable()):
    print("T is diagonalizable!")
# import numpy as np

# G = [[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [1, 2], [1, 3], [2, 0], [2, 1], [2, 2], [2, 3], [3, 0], [3, 1], [3, 2], [3, 3]]
# tab = np.zeros((16, 16), dtype=int)
# T = np.zeros((16, 16), dtype=complex)

# for i in range(16):
#     for j in range(16):
#         for k in range(16):
#             if G[k] == [(G[i][0] + G[j][0]) % 4, (G[i][1] + G[j][1]) % 4]:
#                 tab[i][j] = k + 1

# # Output the tab matrix content
# for row in tab:
#     print(row)

# print("\n")

# x = -1 
# for i in range(16):
#     for j in range(16):
#         for k in range(16):
#             T[i][j] = x ** (G[i][0] * (G[j][1] - G[i][1]))


# eva, evt = np.linalg.eig(T)
# eva = abs(eva)
# print("Matrix T:\n{}".format(T))
# print("---------------------------------------")
# print("Eigenvalues of matrix T:\n{}".format(eva))
# print("Eigenvectors of matrix T:\n{}".format(evt))

# import numpy as np

# G = [[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [1, 2], [1, 3], [2, 0], [2, 1], [2, 2], [2, 3], [3, 0], [3, 1], [3, 2], [3, 3]]
# tab = np.zeros((16, 16), dtype=int)
# T = np.zeros((16, 16), dtype=complex)

# for i in range(16):
#     for j in range(16):
#         for k in range(16):
#             if G[k] == [(G[i][0] + G[j][0]) % 4, (G[i][1] + G[j][1]) % 4]:
#                 tab[i][j] = k + 1

# # Output the tab matrix content
# for row in tab:
#     print(row)

# print("\n")

# x = 1j ** 0.5
# for i in [4, 5, 6, 7, 12, 13, 14 ,15]:
#     for j in [4, 5, 6, 7, 12, 13, 14 ,15]:
#         for k in range(16):
#             T[i][j] = x ** (G[i][0] * (G[j][1] - G[i][1]))

# for row in T:
#     print(row)

# eva, evt = np.linalg.eig(T)
# print("Matrix T:\n{}".format(T))
# print("---------------------------------------")
# print("Eigenvalues of matrix T:\n{}".format(eva))
# print("Eigenvectors of matrix T:\n{}".format(evt))

# import numpy as np

# G = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [3, 0], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5]]
# tab = np.zeros((24, 24), dtype=int)
# T = np.zeros((24, 24), dtype=complex)

# for i in range(24):
#     for j in range(24):
#         for k in range(24):
#             if G[k] == [(G[i][0] + G[j][0]) % 4, (G[i][1] + G[j][1]) % 6]:
#                 tab[i][j] = k + 1

# # Output the tab matrix content
# for row in tab:
#     print(row)

# print("\n")x = 1j
y = 0.5 + 3 ** 0.5/2j
e = 1
a = -1
b = 1
c = -1
d = 1
f = x
g = x ** 2
h = -x
T = [[e, a, b, c, d, f, g, h], [c, e, a, b, h, d, f, g], [b, c, e, a, g, h, d, f], [c, e, a, b, h, d, f, g]
, [d, h, g, f, e, c, b, a], [f, d, h, g, a, e, c, b], [g, f, d, h, b, a, e, c], [h, g, f, d, c, b, a, e]]

eva, evt = np.linalg.eig(T)
eva = abs(eva)
print("Matrix T:\n{}".format(T))
print("---------------------------------------")
print("Eigenvalues of matrix T:\n{}".format(eva))

# x = -1
# for i in range(24):
#     for j in range(24):
#         for k in range(24):
#             T[i][tab[i][j] - 1] = x ** (G[i][0] * G[j][1])

# for row in T:
#     print(row)

# eva, evt = np.linalg.eig(T)
# print("Matrix T:\n{}".format(T))
# print("---------------------------------------")
# print("Eigenvalues of matrix T:\n{}".format(eva))
# print("Eigenvectors of matrix T:\n{}".format(evt))

# import numpy as np

# G = [[0, 0], [0, 1], [1, 0], [1, 1]]
# tab = np.zeros((4, 4), dtype=int)
# T = np.zeros((4, 4), dtype=complex)

# for i in range(4):
#     for j in range(4):
#         for k in range(4):
#             if G[k] == [(G[i][0] + G[j][0]) % 2, (G[i][1] + G[j][1]) % 2]:
#                 tab[i][j] = k + 1

# # Output the tab matrix content
# for row in tab:
#     print(row)

# print("\n")

# x = -1
# y = 1j ** 0.3
# for i in range(4):
#     for j in range(4):
#         for k in range(4):
#             T[i][tab[i][j] - 1] = x ** (G[i][0] * G[j][1]) * y ** (tab[i][j] - 1)

# for row in T:
#     print(row)

# eva, evt = np.linalg.eig(T)
# eva = abs(eva)
# print("Matrix T:\n{}".format(T))
# print("---------------------------------------")
# print("Eigenvalues of matrix T:\n{}".format(eva))
# print("Eigenvectors of matrix T:\n{}".format(evt))

# import numpy as np

# G = [[0, 0], [0, 1]]
# tab = np.zeros((2, 2), dtype=int)
# T = np.zeros((2, 2), dtype=complex)

# for i in range(2):
#     for j in range(2):
#         for k in range(2):
#             if G[k] == [(G[i][0] + G[j][0]) % 2, (G[i][1] + G[j][1]) % 2]:
#                 tab[i][j] = k + 1

# # Output the tab matrix content
# for row in tab:
#     print(row)

# print("\n")

# T = [[1, 1], [-1, 1]]
# y = 1j ** 0.
# for i in range(2):
#     for j in range(2):
#         for k in range(2):
#             T[i][j] = T[i][j] * y ** (tab[i][j] - 1)

# for row in T:
#     print(row)

# eva, evt = np.linalg.eig(T)
# eva = abs(eva)
# print("Matrix T:\n{}".format(T))
# print("---------------------------------------")
# print("Eigenvalues of matrix T:\n{}".format(eva))
# print("Eigenvectors of matrix T:\n{}".format(evt))
# import numpy as np
# T = np.zeros((18, 18), dtype=complex)

# for i in range(18):
#     for j in range(18):
#         T[i][j] = 1

# for row in T:
#     print(row)

# eva, evt = np.linalg.eig(T)
# print("Matrix T:\n{}".format(T))
# print("---------------------------------------")
# print("Eigenvalues of matrix T:\n{}".format(eva))
# print("Eigenvectors of matrix T:\n{}".format(evt))

# T = [[1, 1], [-1, 1]]

# eva, evt = np.linalg.eig(T)
# #eva = abs(eva)
# print("Matrix T:\n{}".format(T))
# print("---------------------------------------")
# print("Eigenvalues of matrix T:\n{}".format(eva))
# print("Eigenvectors of matrix T:\n{}".format(evt))

# T = np.array([[0.70710678, 0.70710678], [0.70710678j, -0.70710678j]])
# S = np.array([[1, 0], [0, 1j]])
# A = np.linalg.inv(T)
# X = np.dot(A, S)
# X = np.dot(X, T)

# print("Matrix T:\n{}".format(T))
# print("Matrix X:\n{}".format(X))
# def is_diagonalizable(matrix):
#     eigenvalues, eigenvectors = np.linalg.eig(matrix)
#     distinct_eigenvalues = np.unique(eigenvalues)

#     if len(distinct_eigenvalues) == matrix.shape[0]:
#         return True
#     else:
#         return False
# if is_diagonalizable(T):
#     print("矩阵可对角化")
# else:
#     print("矩阵不可对角化")
# det = np.linalg.det(T)
# print(det)
# x = 1j
# e = 1
# a = x
# b = x ** 2
# c = x ** 3
# d = x ** 0.5
# f = x ** 1.5
# T = [[e, a, b, c, d, f], [a, e, d, f, b, c], [b, f, e, d, c, a], [c, d, f, e, a, b], [f, b, c, a, e, d], [d, c, a, b, f, e]]

# eva, evt = np.linalg.eig(T)
# eva = abs(eva)
# print("Matrix T:\n{}".format(T))
# print("---------------------------------------")
# print("Eigenvalues of matrix T:\n{}".format(eva))
# print("Eigenvectors of matrix T:\n{}".format(evt))


#print("Eigenvectors of matrix T:\n{}".format(evt))

x = 1j ** 0.5
y = 0.5 + 3 ** 0.5/2j
z = 1j
u = -1j

e = 1
cx = 1
cy = y 
cz = y ** 2
di = 1
dj = z 
dk = z ** 2
dl = z ** 3
bi = 1
bj = u ** 2
bk = u ** 3
bl = u ** 4

T = [[e, cx, cy, cz, di, dj, dk, dl, bi, bj, bk, bl], [cx, e, cz, cy, bk, dk, dj, bi, dl, bl, di, bj], [cy, cz, e, cx, bl, bi, dl, dk, dj, bk, bj, di], [cz, cy, cx, e, bj, dl, bi, dj ,dk, di, bl, bk],[bi, dk, dl, dj, e, bk, bl, bj, di, cy, cz, cx], [bj, bk, di, bl, dk, e, cy, cx, cz, dj, dl, bi],
    [bk, bj, bl, di, dl, cy, e, cz, cx, bi, dk, dj], [bl, di, bk, bj, dj, cx, cz, e, cy, dk, bi, dl], [di, bl, bj, bk, bi, cz, cx, cy, e, dl, dj, dk], [dj, dl, dk, bi, cy, bj, di, bk, bl, e, cx, cz],[dk, bi, dj, dl, cz, bl, bk, di, bj, cx, e, cy], [dl, dj, bi, dk, cx, di, bj, bl, bk, cz, cy, e]]

eva, evt = np.linalg.eig(T)
eva = abs(eva)
print("---------------------------------------")
print("Eigenvalues of matrix T:\n{}".format(eva))