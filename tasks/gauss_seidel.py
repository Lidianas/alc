# Álgebra Linear Computacional - 2023.1
# Trabalho 01
# Task selecionadas: 1 e 2
# Aluna: Lidiana Souza dos Anjos

import utils
import numpy as np

def solve_by_gauss_seidel(A, B, X, tol):

    B = B[0].to_numpy()
    Y = [0]*len(X)
    iter = 0
    while True:
        iter+=1
        for i in range(len(B)):
            Y[i] = round((B[i] - sum(np.array(A.iloc[i, i+1:])*X[i+1:]) - sum(np.array(A.iloc[i, :i])*Y[:i]))/A.iloc[i, i], 4)

        r = utils.residue(Y, X)
        if r <= tol:
            return Y, iter
        X = Y.copy()    
        if iter >= 200:
            return 1


    
