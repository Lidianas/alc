# Álgebra Linear Computacional - 2023.1
# Trabalho 01
# Task selecionadas: 1 e 2
# Aluna: Lidiana Souza dos Anjos

import utils as ut
import pandas as pd
import numpy as np

def solve_by_pm(A, X, tol):

    iter = 0
    oldLambda = 1
    ind = 0
    while True:
        
        Y = ut.matrixVector_product(A, X)
        if iter == 0:
            newLambda = max(Y.min(), Y.max(), key=abs)
            ind = np.where(Y==newLambda)[0][0]
        else:
            newLambda = Y[ind]
            
        r = ut.residue(newLambda, oldLambda, 1)
        if r <= tol: 
            return newLambda, X, iter
        else:
            oldLambda = newLambda
            X = Y/newLambda
        iter += 1

    


    