# Álgebra Linear Computacional - 2023.1
# Trabalho 01
# Task selecionadas: 1 e 2
# Aluna: Lidiana Souza dos Anjos

import utils as ut
import pandas as pd

def solve_by_pm(A, X, tol):

    iter = 0
    oldLambda = 1
    while True:
        iter += 1
        Y = ut.matrixVector_product(A, X)
        newLambda = max(Y)
        r = ut.residuo(newLambda, oldLambda, 1)
        oldLambda = newLambda
        X = Y/newLambda
        if r <= tol: 
            return newLambda, X, iter

        

    


    