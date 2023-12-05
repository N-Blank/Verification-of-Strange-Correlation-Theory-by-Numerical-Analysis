import numpy as np
import cmath

# Eigenvalue of transfer matrix for Z3*Z6 group
G = [[0, 0], [0, 1], [0, 2], [0, 3], [2, 0], [2, 1], [2, 2], [2, 3]]
tab = np.zeros((8, 8), dtype=int)
table = np.zeros((8, 8), dtype=int)
T = np.zeros((8, 8), dtype=complex)
V1 = np.zeros((8, 8), dtype=complex)
V2 = np.zeros((8, 8), dtype=complex)
theta = 2.5

def v1(k):
    if k == 1:
        return cmath.exp(1j * theta)
    else:
        return 1

for i in range(8):
    for j in range(8):
        for k in range(8):
            if G[k] == [(-G[i][0] + G[j][0]) % 4, (-G[i][1] + G[j][1]) % 4]:
                table[i][j] = k + 1

for i in range(8):
    for j in range(8):
        V1[i][j] = v1(table[i][j] - 1)

for row in V1:
    print(row)

print("\n")

for i in range(8):
    for j in range(8):
        V2[i][j] = V1[i][j] * V1[0][i] / V1[0][j]

# Output the V2 matrix content
for row in V2:
    print(row)

print("\n")

for i in range(8):
    for j in range(8):
        for k in range(8):
            if G[k] == [(G[i][0] + G[j][0]) % 4, (G[i][1] + G[j][1]) % 4]:
                tab[i][j] = k + 1

x = 1j
for i in range(8):
    for j in range(8):
        for k in range(8):
            T[i][tab[i][j] - 1] = (x ** (G[i][0] * G[j][1])) * V2[i][j]


eva, evt = np.linalg.eig(T)
S = np.diag([1 * V2[0][0], 1j * V2[1][1], -1 * V2[2][2], -1j * V2[3][3], 1 * V2[4][4], 1j * V2[5][5], -1 * V2[6][6], -1j * V2[7][7]])
S_inv = np.linalg.inv(S)
T11 = S.dot(T).dot(S_inv)
print("Matrix T11:\n{}".format(T11))
print("---------------------------------------")
print("Eigenvalues of matrix T:\n{}".format(eva))
P = evt
P_inv = np.linalg.inv(P)
D = P_inv.dot(T).dot(P)
print("Matrix D:\n{}\n".format(D))


# Eigen value of transfer matrix for Z3*Z6 group
G0 = [[0, 0], [0, 1], [0, 2], [0, 3], [2, 0], [2, 1], [2, 2], [2, 3]]
G1 = [[1, 0], [1, 1], [1, 2], [1, 3], [3, 0], [3, 1], [3, 2], [3, 3]]
tab = np.zeros((8, 8), dtype=int)
T01 = np.zeros((8, 8), dtype=complex)

for i in range(8):
    for j in range(8):
        for k in range(8):
            if G1[k] == [(G0[i][0] + G1[j][0]) % 4, (G0[i][1] + G1[j][1]) % 4]:
                tab[i][j] = k + 1

# Output the tab matrix content
for row in tab:
    print(row)

print("\n")

x = 1j
for i in range(8):
    for j in range(8):
        for k in range(8):
            T01[i][tab[i][j] - 1] = (x ** (G0[i][0] * G1[j][1])) * V2[i][j]

for row in T01:
    print(row)

S_inv = np.linalg.inv(S)
X = P_inv.dot(T01).dot(S_inv).dot(P)
print("Matrix X:\n{}".format(X))

#S = np.diag([1, -1j, -1, 1j, 1, -1j, -1, 1j])
# O = np.diag([1, 1j, -1, -1j, 1, 1j, -1, -1j])
# diagonal_elements = np.diag(T01)
# T01 = np.diag(diagonal_elements)

