import numpy as np

def linear_algebra_demo():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])

    dot_product = np.dot(a, b)

    A = np.array([[1, 2],
                  [3, 4]])

    B = np.array([[5, 6],
                  [7, 8]])

    matrix_product = np.matmul(A, B)
    transpose_A = A.T
    determinant_A = np.linalg.det(A)

    return dot_product, matrix_product, transpose_A, determinant_A
    import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Dot Product:", np.dot(a, b))
