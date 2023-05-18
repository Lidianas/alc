import back_forward_substitution
import numpy as np
def lu(M):
    
    len_A = len(M)
    Z = np.zeros((len_A, len_A))
    for j in range(0, len_A):
        for i in range(0, len_A):
            if j>=i:
                Z[i][j] = round(M[i,j] - sum(Z[i, k]*Z[k,j] for k in range(i)), 4)
            else:
                Z[i][j] = round((M[i,j] - sum(Z[i, k]*Z[k,j] for k in range(i)))/Z[j,j], 4)
    return Z

def solve_by_lu(M, B):
    Y = back_forward_substitution.forward_substitution(M, B, True)
    X = back_forward_substitution.backward_substitution(M, Y)
    return X


