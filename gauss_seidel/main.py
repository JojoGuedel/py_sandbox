from math import *

def solve(equ_matrix, iterations):
    if (len(equ_matrix) < 2):
        return None
    
    dim = int(sqrt(len(equ_matrix)))
    if (dim * (dim + 1) != len(equ_matrix)):
        return None

    x = [0] * dim

    for i in range(iterations):
        for j in range(dim):
            count = equ_matrix[j * (dim + 1) + dim]
            denom = equ_matrix[j * (dim + 1) + j]

            for k in range(dim):
                if j != k:
                    count -= equ_matrix[j * (dim + 1) + k] * x[k]
            
            x[j] = count / denom

        res = 0
        for j in range(dim):
            res += x[j] * equ_matrix[j]
        
        if res == equ_matrix[dim]:
            print(i)
            return x
    
    return x

equation_matrix_1 = [9,  2,  3, 7,
                     1, 12,  9, 2,
                     4,  6, 14, 1]

print(solve(equation_matrix_1, 1000))