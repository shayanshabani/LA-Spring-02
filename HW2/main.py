import numpy as np

input_string = input().split()
width = int(input_string[0])
height = int(input_string[1])
basis = np.array([0]) # construct a 1D numpy array
for i in range(height):
    binary_number = int(input(), 2) # input is in binary, but convert it to decimal
    if binary_number == 0: # no need to check zero number
        print('YES')
    else:
        for i in range(len(basis)):
            # xor operation is bitwise, so there is no need to convert decimal value to binary
            xored_value = binary_number ^ basis[i]
            # if the result of xor is less than previous one, it means that one of the left_most 1's of number has been removed
            binary_number = min(binary_number, xored_value)
        if binary_number == 0: # all of the 1's can be constructed using basis
            print('YES')
        else:
            basis = np.hstack((basis, binary_number))
            print('NO')