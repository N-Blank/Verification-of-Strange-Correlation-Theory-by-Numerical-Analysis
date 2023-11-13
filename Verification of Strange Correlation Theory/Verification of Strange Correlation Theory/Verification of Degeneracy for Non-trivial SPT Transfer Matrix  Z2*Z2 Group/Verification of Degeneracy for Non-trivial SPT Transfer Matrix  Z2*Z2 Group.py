import numpy as np

# Eigen value of transfer matrix for Z2*Z2 group
T = np.array([[1, 1, 1, 1], [1, 1, 1, 1], [1, -1, 1, -1], [-1, 1, -1, 1]])

eva, evt = np.linalg.eig(T)

print("Matrix T:\n{}".format(T))
print("---------------------------------------")
print("Eigenvalues of matrix T for Z2*Z2 group:\n{}".format(eva))
print("Eigenvectors of matrix T for Z2*Z2 group:\n{}".format(evt))
O = np.array([[2, 0, 0, 0], [0, 1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -2]])
S1 = np.array([[0.5, 0.5, 0.26697694, -0.59000461],
                   [0.5, -0.5, 0.26697694, 0.38973653],
                   [0.5, -0.5, -0.65476966, 0.59000461],
                   [-0.5, 0.5, 0.65476966, -0.38973653]])
S = S1.T
S_inv = np.linalg.inv(S)
O = np.matmul(np.matmul(S_inv, O), S)
print("Matrix S:\n{}".format(S))
print("Matrix S_inv:\n{}".format(S_inv))
print("Matrix O':\n{}".format(O))

# Eigen value of transfer matrix for Z2*Z2 group with coboundary
T = np.array([[1, x, x ** 2, x ** 3], [x, 1, x ** 3, x ** 2], [x ** 2, x ** 3, 1, x], [x ** 3, x ** 2, x, 1]])

eva, evt = np.linalg.eig(T)

print("Matrix T:\n{}".format(T))
print("---------------------------------------")
print("Eigenvalues of matrix T:\n{}".format(eva))
print("Eigenvectors of matrix T:\n{}".format(evt))
O = np.array([[2, 0, 0, 0], [0, 1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -2]])
S1 = np.array([[0.5 + 0.00000000e+00j, 0.5 - 3.17739123e-16j,
               0.5 + 0.00000000e+00j, 0.5 - 2.55422187e-16j],
              [0.5 + 8.62850119e-17j, 0.5 + 0.00000000e+00j,
               -0.5 + 5.10050833e-16j, -0.5 + 1.18991827e-16j],
              [0.5 + 1.31365772e-16j, -0.5 + 4.19334208e-17j,
               -0.5 + 5.23084635e-17j, 0.5 + 0.00000000e+00j],
              [0.5 + 4.12042521e-17j, -0.5 + 2.42301648e-16j,
               0.5 - 2.44247090e-16j, -0.5 + 5.16150454e-17j]])
S = S1.T
S_inv = np.linalg.inv(S)
O = np.matmul(np.matmul(S_inv, O), S)
print("Matrix S:\n{}".format(S))
print("Matrix S_inv:\n{}".format(S_inv))
print("Matrix O':\n{}".format(O))
T = np.array([
    [complex(1, 0), complex(1, 0), complex(1, 0), complex(1, 0), complex(1, 0), complex(1, 0), complex(1, 0), complex(1, 0), complex(1, 0)],
    [complex(1, 0), complex(1, 0), complex(1, 0), complex(1, 0), complex(1, 0), complex(1, 0), complex(1, 0), complex(1, 0), complex(1, 0)],
    [complex(1, 0), complex(1, 0), complex(1, 0), complex(1, 0), complex(1, 0), complex(1, 0), complex(1, 0), complex(1, 0), complex(1, 0)],
    [complex(1, 0), complex(-0.5, -0.8660254037844386), complex(-0.4999999999999999, 0.8660254037844386), complex(1, 0), complex(-0.5, -0.8660254037844386), complex(-0.4999999999999999, 0.8660254037844386), complex(1, 0), complex(-0.5, -0.8660254037844386), complex(-0.4999999999999999, 0.8660254037844386)],
    [complex(-0.4999999999999999, 0.8660254037844386), complex(1, 0), complex(-0.5, -0.8660254037844386), complex(-0.4999999999999999, 0.8660254037844386), complex(1, 0), complex(-0.5, -0.8660254037844386), complex(-0.4999999999999999, 0.8660254037844386), complex(1, 0), complex(-0.5, -0.8660254037844386)],
    [complex(-0.5, -0.8660254037844386), complex(-0.4999999999999999, 0.8660254037844386), complex(1, 0), complex(-0.5, -0.8660254037844386), complex(-0.4999999999999999, 0.8660254037844386), complex(1, 0), complex(-0.5, -0.8660254037844386), complex(-0.4999999999999999, 0.8660254037844386), complex(1, 0)],
    [complex(1, 0), complex(-0.4999999999999999, 0.8660254037844386), complex(-0.5, -0.8660254037844384), complex(1, 0), complex(-0.4999999999999999, 0.8660254037844386), complex(-0.5, -0.8660254037844384), complex(1, 0), complex(-0.4999999999999999, 0.8660254037844386), complex(-0.5, -0.8660254037844384)],
    [complex(-0.5, -0.8660254037844384), complex(1, 0), complex(-0.4999999999999999, 0.8660254037844386), complex(-0.5, -0.8660254037844384), complex(1, 0), complex(-0.4999999999999999, 0.8660254037844386), complex(-0.5, -0.8660254037844384), complex(1, 0), complex(-0.4999999999999999, 0.8660254037844386)],
    [complex(-0.4999999999999999, 0.8660254037844386), complex(-0.5, -0.8660254037844384), complex(1, 0), complex(-0.4999999999999999, 0.8660254037844386), complex(-0.5, -0.8660254037844384), complex(1, 0), complex(-0.4999999999999999, 0.8660254037844386), complex(-0.5, -0.8660254037844384), complex(1, 0)],
])

eva, evt = np.linalg.eig(T)

print("Matrix T:\n{}".format(T))
print("---------------------------------------")
print("Eigenvalues of matrix T:\n{}".format(eva))
print("Eigenvectors of matrix T:\n{}".format(evt))
