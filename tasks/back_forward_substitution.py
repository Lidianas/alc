def forward_substitution(A, B, is_lu=True):
    """ AX=B """

    i = 0
    X = B[0].to_numpy()
    while i < len(B):
        if is_lu == True:
            X[i] = X[i] - sum(A[i, j]*X[j] for j in range(i)) 
        else:
            X[i] = (X[i] - sum(A[i, j]*X[j] for j in range(i)))/A[i,i]
        i+=1
    return X
        
def backward_substitution(A, B):
    """ AX=B """

    i = len(B) - 1
    X = B
    while i >= 0:
        X[i] = (B[i] - sum(A[i, j]*B[j] for j in range(-1,-(len(B)-i),-1)))/A[i,i] 
        i-=1
    return X
