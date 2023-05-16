# Álgebra Linear Computacional - 2023.1
# Trabalho 01
# Task selecionadas: 1 e 2
# Aluna: Lidiana Souza dos Anjos

import pandas as pd
import lu_decomposition
import utils
import cholesky_decomposition
import gauss_seidel
import jacobi
import power_method as pm
import jacobi_eigenvectors as jcb_eigen

print("The matrix A must be in the following format \n \
       A B C\n \
       D E F\n \
       G H I\n\n ")

A = pd.read_csv("/home/lidiana/Desktop/ufrj/alc/t1/data/Matriz_C.dat", header=None, sep=' ', skipinitialspace=True)

print("The vector B must be in the following format \n \
       P Q R ")
    
B = pd.read_csv("/home/lidiana/Desktop/ufrj/alc/t1/data/Vetor_D_01.dat", header=None, sep=' ', skipinitialspace=True)

#N = int(input("Digite a ordem do sistema de equações \n"))
# possible warnings:
# - matrix A is not a square matrix
# - the numbers of vector B lines is not the same as the number of lines from matrix A
# - cholesky only works for symetric matrix, so this must be evaluated
# - cholesky requires that the matrix must be define positive
# - for iteractive methods:
#   - there is no convergence garantee
#   - the matrix is diagonal positive, so the convergence is assured
# - the operation number chose did not exist, please choose from the list below
# relevant infos:
# - 
# - the matrix is define positive, so the convergence is assured

valid_cod = False
while valid_cod == False:
    print("Choose the operation \n 1 - LU Decomposition \n 2 - Cholesky Decomposition \n 3 - Jacobi Iteractive Method \n 4 - Gauss-Seidel Iteractive Method\n 5 - Power Method \n 6 - Jacobi method for eigenvalues and eigenvector")
    cod = int(input("Type the operation number \n"))
    tol = float(input("Type the tolerance in the case of iteractive methods \n"))

    if cod == 1:
        res = lu_decomposition.solve_by_lu(A, B)
        print(res)
        valid_cod=True

    elif cod == 2:
            
        if utils.sym(A):
            res = cholesky_decomposition.solve_by_cholesky(A, B)
            print(res)
        else:
            print("The matrix is not symmetric")

        valid_cod = True
            
    elif cod == 3:
        X, iter = jacobi.solve_by_jacobi(A, B, [1]*len(B), tol)
        print("Solution: ", str(X))
        print("Iterations: ", str(iter))

        valid_cod = True

    elif cod == 4:
        X, iter = gauss_seidel.solve_by_gauss_seidel(A, B, [1]*len(B), tol)
        print("Solution: ", str(X))
        print("Iterations: ", str(iter))

        valid_cod = True

    elif cod == 5:
        eigenvalue, eigenvector, iter = pm.solve_by_pm(A, [1]*len(A), tol)
        print("Higher eigenvalue: \n", str(eigenvalue))
        print("Higher eigenvector: \n", str(eigenvector))
        print("Iterations: \n", str(iter))

        valid_cod = True
    
    elif cod == 6:

        if utils.sym(A):
            eigenvalues, eigenvectors, iter = jcb_eigen.solve_by_jacobi_sym(A, tol)
            print("Eigenvalues: \n", str(eigenvalues))
            print("Eigenvectors: \n", str(eigenvectors))
            print("Iterations: \n", str(iter))

        else:
            print("The matrix is not symmetric")

        valid_cod = True
    else:
        print("--------------------Warning!---------------------------")
        print("This is an invalid option, choose one from the list below.")
        print("-------------------------------------------------------")
