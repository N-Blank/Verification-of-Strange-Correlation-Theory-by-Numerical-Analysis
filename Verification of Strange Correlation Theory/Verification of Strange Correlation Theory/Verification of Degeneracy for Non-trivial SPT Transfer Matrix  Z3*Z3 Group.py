import numpy as np

# Eigen value of transfer matrix for Z3*Z3 group
G = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
tab = np.zeros((9, 9), dtype=object)  # 创建一个9x9的全零矩阵
T = np.zeros((9, 9), dtype=object)

for i in range(9):
    for j in range(9):
        for k in range(9):
            if(G[k] == [(G[i][0] + G[j][0]) % 3, (G[i][1] + G[j][1]) % 3]):
                tab[i][j] = k + 1

# 输出tab矩阵内容
for row in tab:
    print(row)

print("\n")


x = -0.5 + (3 ** 0.5)/2j
for i in range(9):
    for j in range(9):
        for k in range(9):
            T[i][tab[i][j] - 1] = x ** (G[i][0] * G[j][1])

for row in T:
    print(row)

eva, evt = np.linalg.eig(T)
print("Matrix T:\n{}".format(T))
print("---------------------------------------")
print("Eigenvalues of matrix T:\n{}".format(eva))
print("Eigenvectors of matrix T:\n{}".format(evt))
