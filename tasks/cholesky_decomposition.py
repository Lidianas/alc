import back_forward_substitution
import utils

def cholesky(A):
    
    len_A = len(A)
    
    i = 0
    while i < len_A:
        j = 0
        while j <= i:
            if i==j:
                tmp = A[i][j] - sum(A[i][j]**2 for j in range(i))
                if tmp > 0:
                    A[i,j] = (tmp)**(1/2)
                else: 
                    return 0
            elif j == 0:
                A[i, j] = (A[i, j])/A[j, j]
                A[j, i] = A[i, j]
            elif i>j:
                A[i, j] = (A[i, j] - utils.back_mult(A, i-2, i, j))/A[j, j]
                A[j, i] = A[i, j]
            j+=1 
        i+=1
    return A

def solve_by_cholesky(A, B):
    Y = back_forward_substitution.forward_substitution(A, B, False)
    X = back_forward_substitution.backward_substitution(A, Y)
    return X