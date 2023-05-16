import back_forward_substitution
import utils

def cholesky(A):
    
    len_A = len(A)
    
    i = 0
    while i < len_A:
        j = 0
        while j <= i:
            """if j == 0:
                A.loc[i, j] = A.loc[i, j]/A.loc[0, 0]
                A.loc[j, i] = A.loc[i, j]"""
            if i==j:
                tmp = A.loc[i, j] - sum(A.loc[i, j]**2 for j in range(i))
                if tmp > 0:
                    A.loc[i,j] = (tmp)**(1/2)
                else: 
                    return "The matrix is not positive defined"
            elif j == 0:
                A.loc[i, j] = (A.loc[i, j])/A.loc[j, j]
                A.loc[j, i] = A.loc[i, j]
            elif i>j:
                A.loc[i, j] = (A.loc[i, j] - utils.back_mult(A, i-2, i, j))/A.loc[j, j]
                A.loc[j, i] = A.loc[i, j]
            j+=1 
        i+=1
    return A

def solve_by_cholesky(A, B):
    cho = cholesky(A)
    print(cho)
    print(B)
    Y = back_forward_substitution.forward_substitution(cho, B, False)
    print(Y)
    X = back_forward_substitution.backward_substitution(cho, Y)
    return X