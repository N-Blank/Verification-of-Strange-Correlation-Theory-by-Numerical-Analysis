import numpy as np

# Eigen value of transfer matrix for Z3*Z6 group
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
