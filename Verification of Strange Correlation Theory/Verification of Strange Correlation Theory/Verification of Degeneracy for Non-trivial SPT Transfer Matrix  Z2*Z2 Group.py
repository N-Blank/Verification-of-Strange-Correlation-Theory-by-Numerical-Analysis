import numpy as np

#Verification of Degeneracy for Non-trivial SPT Transfer Matrix  Z2*Z2 Group with coboundary
G = [[0, 0], [0, 1], [1, 0], [1, 1]]
tab = np.zeros((4, 4), dtype=int)
T = np.zeros((4, 4), dtype=complex)

for i in range(4):
    for j in range(4):
        for k in range(4):
            if G[k] == [(G[i][0] + G[j][0]) % 2, (G[i][1] + G[j][1]) % 2]:
                tab[i][j] = k + 1

# Output the tab matrix content
for row in tab:
    print(row)

print("\n")

x = -1
y = 1j ** 0.3
for i in range(4):
    for j in range(4):
        for k in range(4):
            T[i][tab[i][j] - 1] = x ** (G[i][0] * G[j][1]) * y ** (tab[i][j] - 1)

for row in T:
    print(row)

eva, evt = np.linalg.eig(T)
eva = abs(eva)
print("Matrix T:\n{}".format(T))
print("---------------------------------------")
print("Eigenvalues of matrix T:\n{}".format(eva))
print("Eigenvectors of matrix T:\n{}".format(evt))Verification of Degeneracy for Non-trivial SPT Transfer Matrix  Z2*Z2 Group

G = [[0, 0], [0, 1]]
tab = np.zeros((2, 2), dtype=int)
T = np.zeros((2, 2), dtype=complex)

for i in range(2):
    for j in range(2):
        for k in range(2):
            if G[k] == [(G[i][0] + G[j][0]) % 2, (G[i][1] + G[j][1]) % 2]:
                tab[i][j] = k + 1

# Output the tab matrix content
for row in tab:
    print(row)

print("\n")

T = [[1, 1], [-1, 1]]
y = 1j ** 0.
for i in range(2):
    for j in range(2):
        for k in range(2):
            T[i][j] = T[i][j] * y ** (tab[i][j] - 1)

for row in T:
    print(row)

eva, evt = np.linalg.eig(T)
eva = abs(eva)
print("Matrix T:\n{}".format(T))
print("---------------------------------------")
print("Eigenvalues of matrix T:\n{}".format(eva))
print("Eigenvectors of matrix T:\n{}".format(evt))
