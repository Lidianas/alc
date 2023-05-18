def forward_substitution(A, B, is_lu=True):

    i = 0
    X = [0]*len(B)
    while i < len(B):
        if is_lu == True:
            X[i] = B[i] - sum(A[i, j]*X[j] for j in range(i)) 
        else:
            X[i] = (B[i] - sum(A[i, j]*X[j] for j in range(i)))/A[i,i]
        i+=1
    return X
        
def backward_substitution(A, B):

    i = len(B) - 1
    X = [0]*len(B)
    while i >= 0:
        X[i] = (B[i] - sum(A[i, j]*X[j] for j in range(-1,-(len(B)-i),-1)))/A[i,i] 
        i-=1
    return X
