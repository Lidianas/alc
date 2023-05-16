import back_forward_substitution
import utils

def lu(A):
    
    len_A = len(A)
    
    j = 0
    while j < len_A:
        i = 1
        while i < len_A:
            if j == 0:
                A.loc[i, j] = A.loc[i, j]/A.loc[0, 0]
            elif i<=j:
                A.loc[i, j] = A.loc[i, j] - utils.back_mult(A, i-1, i, j)
            elif i>j:
                A.loc[i, j] = (A.loc[i, j] - utils.back_mult(A, i-2, i, j))/A.loc[j, j]
            i+=1 
        j+=1
    return A

def solve_by_lu(A, B):
    LU = lu(A)
    print(LU)
    Y = back_forward_substitution.forward_substitution(LU, B, True)
    print(Y)
    X = back_forward_substitution.backward_substitution(LU, Y)
    return X


