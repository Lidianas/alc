# Álgebra Linear Computacional - 2023.1
# Trabalho 01
# Task selecionadas: 1 e 2
# Aluna: Lidiana Souza dos Anjos

import utils
import numpy as np
import math

def maxValue(A):

    higherValue = 0
    pos_HV = [0,0]
    for i in range(len(A)):
        for j in range(len(A)):
            if i < j:
                tmp_higherValue = abs(A[i, j])
                if tmp_higherValue >= higherValue:
                    higherValue = tmp_higherValue
                    pos_HV[0] = i
                    pos_HV[1] = j
    
    return pos_HV

def calcTeta(maxV, Aii, Ajj):

    if Aii == Ajj:
        return np.pi/4
    else:
        
        teta = (1/2)*math.atan((2*maxV)/(Aii - Ajj))
        print("teta:",str(teta))
        return (1/2)*math.atan((2*maxV)/(Aii - Ajj))
        

def regP(posMaxV, dim, teta):

    p = np.identity(dim)
    p[posMaxV[0], posMaxV[0]] = np.cos(teta)
    p[posMaxV[1], posMaxV[1]] = np.cos(teta)
    p[posMaxV[0], posMaxV[1]] = -np.sin(teta)
    p[posMaxV[1], posMaxV[0]] = np.sin(teta)
    return p

def isDiagElemHigher(A, dim, tol):
    for i in range(dim):
        for j in range(dim):
            if i < j:
                if A[i, j] > tol:
                    return True
    return False

def solve_by_jacobi_sym(A, tol):

    dim = len(A)
    A = np.asmatrix(A)
    print(A)
    X = np.identity(dim)
    isDEH = True
    iter = 0
    while isDEH==True:
        posMaxV = maxValue(A)
        teta = calcTeta(A[posMaxV[0], posMaxV[1]], A[posMaxV[0], posMaxV[0]], A[posMaxV[1], posMaxV[1]])
        P = regP(posMaxV, dim, teta)
        PT = np.transpose(P)
        productAP = utils.matrixMatrix_product(A, P)
        A = utils.matrixMatrix_product(PT, productAP)
        X = utils.matrixMatrix_product(X, P)
        isDEH = isDiagElemHigher(A, dim, tol)
        iter += 1

    return A, X, iter


    




    

