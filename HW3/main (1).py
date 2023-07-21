import numpy as np
import sys

def custom_round(x):
    x[np.abs(x) < 0.000001] = 0
    return np.round(x, 2)

def find_inverse(matrix):
    # stack identity matrix to the right of this matrix
    matrix = np.hstack((matrix, np.identity(len(matrix))))
    for i in range(len(matrix)):
        matrix[i,:] *= 1 / matrix[i, i]
        for j in range(len(matrix)):
            if j == i:
                continue
            matrix[j] = np.subtract(matrix[j], matrix[i] * matrix[j,i])
    return matrix

#dimensions_string = input().split()
number_of_samples = int(input())
number_of_linear_transformations = int(input())
number_of_requests = int(input())
temp_X = np.array([])
temp_Y = np.array([])
X = np.array([])
Y = np.array([])
for i in range(number_of_samples):
    # building X matrix
    row = list(map(int, input().split()))
    temp_X = np.array(row)
    # building Y matrix
    for j in range(number_of_linear_transformations):
        another_row = list(map(int, input().split()))
        if j == number_of_linear_transformations - 1:
            temp_Y = np.array(another_row)
            #print(temp_Y)
            if i == 0:
                X = np.array(temp_X)
                Y = np.array(temp_Y)
            else:
                Y = np.vstack((Y, temp_Y))
                X = np.vstack((X, temp_X))

final = np.array([])
for i in range(number_of_requests):
    row = list(map(int, input().split()))
    final_temp = np.array(row)
    final_temp = final_temp.T
    if i == 0:
        final = np.array(final_temp)
    else:
        final = np.vstack((final, final_temp))

X = np.transpose(X)
Y = np.transpose(Y)
final = np.transpose(final)
X_T = np.transpose(X)
aimed_for_inverse = np.matmul(X, X_T)
if np.linalg.det(aimed_for_inverse) <= 0.01:
    print("The results are unknown")
else:
    inversed_matrix = find_inverse(aimed_for_inverse)
    if inversed_matrix is None:
        print("The results are unknown")
    else:
        #inversed_matrix = inversed_matrix[int(len(inversed_matrix) / 2):, :]
        inversed_matrix = np.hsplit(inversed_matrix, 2)[1]
        #print(inversed_matrix)
        A = np.matmul(Y, np.matmul(X_T, inversed_matrix))
        if np.sum(np.abs(np.subtract(np.matmul(A, X), Y))) > 0.01:
            print("The results are noisy")
        final_Y = np.matmul(A, final)
        for i in range(len(final_Y)):
            final_Y[i] = custom_round(final_Y[i])
        final_Y = final_Y.transpose().tolist()
        for x in final_Y:
            for y in x:
                print(y, end=' ')
            print()