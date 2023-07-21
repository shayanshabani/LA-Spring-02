import numpy as np
import math

def inner_product(first_vector, second_vector):
    result = 0
    # element wise product
    for i in range(len(first_vector)):
        result += first_vector[i] * second_vector[i]
    return result


def norm(vector):
    # <v, v> = |v|^2
    return math.sqrt(inner_product(vector, vector))


def QR_decomposition(matrix):
    # run gram-schmidt procedure to find QR decomposition of the matrix
    Q = np.empty(shape=(len(matrix), len(matrix)))
    R = np.empty(shape=(len(matrix), len(matrix)))
    # iterate over the columns of the matrix
    for i in range(len(matrix)):
        vector = matrix[:, i]
        # linear combination of i - 1 orthonormal vectors
        inner_product_coefficients = np.array([])
        q_bar = np.array(vector)
        for j in range(i):
            q = Q[:, j]
            R[j, i] = inner_product(vector, q)
            q_bar -= inner_product(vector, q) * q
        norm_q_bar = norm(q_bar)
        R[i, i] = norm_q_bar
        R[i+1:, i] = 0
        q = q_bar / norm_q_bar
        Q[:, i] = q
    return Q, R


dimension = int(input())
matrix = np.array([])
for i in range(dimension):
    each = list(map(float, input().split()))
    if len(matrix) == 0:
        matrix = np.array(each)
    else:
        matrix = np.vstack((matrix, np.array(each)))


for i in range(1000):
    Q, R = QR_decomposition(matrix)
    matrix = R @ Q
eigenvalues = []
determinant = 1
for i in range(len(matrix)):
    eigenvalues.append(matrix[i, i])
    determinant *= matrix[i, i]
eigenvalues.sort()
for i in range(len(eigenvalues)):
    print("{:.3f}".format(round(eigenvalues[i], 3)), end='    ')
    #print(round(eigenvalues[i], 3), end='    ')
print()
print("{:.3f}".format(round(determinant, 3)))
