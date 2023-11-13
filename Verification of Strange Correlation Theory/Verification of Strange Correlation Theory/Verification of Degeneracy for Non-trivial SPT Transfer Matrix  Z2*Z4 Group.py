import numpy as np
# Eigen value of transfer matrix for Z2*Z4 group
T = np.array([[1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, -1, 1, -1, 1, -1, 1, -1], [-1, 1, -1, 1, -1, 1, -1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, -1, 1, -1, 1, -1, 1, -1], [-1, 1, -1, 1, -1, 1, -1, 1]])

eva, evt = np.linalg.eig(T)

print("Matrix T:\n{}".format(T))
print("---------------------------------------")
print("Eigenvalues of matrix T:\n{}".format(eva))
print("Eigenvectors of matrix T:\n{}".format(evt))

O = np.array([[3, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 2, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, -2, 0, 0], [0, 0, 0, 0, 0, 0, -1, 0], [0, 0, 0, 0, 0, 0, 0, -3]])
S1 = np.array([[-0.64516144, 0.37600001, -0.35355339, -0.24576771, 0.17228814, 0.39708932, 0.42887511, -0.60469694],
 [-0.31242009, -0.71169437, -0.35355339, -0.24576771, 0.19391569, 0.59179288, 0.15101858, -0.33837828],
 [0.08318534, -0.2719236, -0.35355339, 0.43542879, -0.50817103, -0.53261537, -0.49834879, 0.3833906],
 [-0.08318534, 0.2719236, 0.35355339, -0.43542879, 0.42403004, -0.38234123, 0.29629045, -0.2065127],
 [0.47879077, 0.16784718, -0.35355339, -0.24576771, -0.14103142, -0.0369628, -0.29360487, 0.2509678],
 [0.47879077, 0.16784718, -0.35355339, -0.24576771, -0.14103142, -0.0369628, -0.48732803, 0.51522952],
 [0.08318534, -0.2719236, -0.35355339, 0.43542879, 0.47691431, 0.17248885, 0.36307855, -0.02966146],
 [-0.08318534, 0.2719236, 0.35355339, -0.43542879, -0.47691431, -0.17248885, 0.040019, 0.02966146]])
S = S1.T
S_inv = np.linalg.inv(S)
O = np.multiply(O, S)
O = np.multiply(S_inv, O)
print("Matrix S:\n{}".format(S))
print("Matrix S_inv:\n{}".format(S_inv))
print("Matrix O`:\n{}".format(O))
x = 1j ** 0.25
y = x.conjugate()
