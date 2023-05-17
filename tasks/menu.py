# Álgebra Linear Computacional - 2023.1
# Trabalho 01
# Task selecionadas: 1 e 2
# Aluna: Lidiana Souza dos Anjos

import pandas as pd
import numpy as np
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

A = pd.read_csv("/home/lidiana/Desktop/ufrj/alc/t1/data/Matriz_A.dat", header=None, sep=' ', skipinitialspace=True)
print("The vector B must be in the following format \n \
       P Q R ")

B1 = pd.read_csv("/home/lidiana/Desktop/ufrj/alc/t1/data/Vetor_B_01.dat", header=None, sep=' ', skipinitialspace=True)
B2 = pd.read_csv("/home/lidiana/Desktop/ufrj/alc/t1/data/Vetor_B_02.dat", header=None, sep=' ', skipinitialspace=True)
B3 = pd.read_csv("/home/lidiana/Desktop/ufrj/alc/t1/data/Vetor_B_03.dat", header=None, sep=' ', skipinitialspace=True)
B = [B1, B2, B3]
valid_cod = False
while valid_cod == False:
    print("Choose the operation \n 1 - LU Decomposition \n 2 - Cholesky Decomposition \n 3 - Jacobi Iteractive Method \n 4 - Gauss-Seidel Iteractive Method\n 5 - Power Method \n 6 - Jacobi method for eigenvalues and eigenvector")
    cod = int(input("Type the operation number \n"))
    tol = float(input("Type the tolerance in the case of iteractive methods \n"))
    det = int(input("Type 0 if the determinant must be calculated \n"))

    if cod == 1:
        lu = lu_decomposition.lu(np.array(A))
        print(lu)
        for b in B:
            resB = lu_decomposition.solve_by_lu(lu, b)
            print("The solution using LU decomposition \n for vector B = ", str(np.array(b.transpose())), " \n is X = ", str(resB))
        
        if det == 0:
            d = 1
            dE = utils.getDiagElem(lu)
            for i in dE:
                d = d * i
            print("The determinant is ", str(d))
        valid_cod=True

    elif cod == 2:
            
        if utils.sym(A):
            cho = cholesky_decomposition.cholesky(np.array(A))
            if cho == 0:
                print("The matrix is not positive definite")
            else:
                for b in B:
                    resB = cholesky_decomposition.solve_by_cholesky(cho, b)
                    print("The solution using Cholesky decomposition\n for vector B = ", str(np.array(b.transpose())), "\n is X = ", str(resB))
                
                if det == 0:
                    d = 1
                    dE = utils.getDiagElem(cho)
                    for i in dE:
                        d = d * i
                    print("The determinant is ", str(d))

        else:
            print("The matrix is not symmetric, therefore cholesky can't be used")

        valid_cod = True
            
    elif cod == 3:
        if utils.diagDom(A) == 0:
            for b in B:
                X, iter = jacobi.solve_by_jacobi(A, b, [1]*len(b), tol)
                if X == 1:
                    print("After 200 iterations, the method does not converge")
                else:
                    print("The solution using Jabobi iteractive method\n for vector B = ", str(np.array(b.transpose())), "\n is X = ", str(X))
                    print("Iterations: ", str(iter))
        else:
            print("The matrix is not diagonally dominant, therefore the method will not converge")

        if det == 0:
            print("The determinant can't be calculated by this method")
        valid_cod = True

    elif cod == 4:
        if utils.diagDom(A) == 0:
            for b in B:
                X, iter = gauss_seidel.solve_by_gauss_seidel(A, b, [1]*len(b), tol)
                if X == 1:
                    print("After 200 iterations, the method does not converge")
                else:
                    print("The solution using Gauss-Seidel iteractive method\n for vector B = ", str(np.array(b.transpose())), "\n is X = ", str(X))
                    print("Iterations: ", str(iter))
        else:
            print("The matrix is not diagonally dominant, therefore the method will not converge")

        if det == 0:
            print("The determinant can't be calculated by this method")
        valid_cod = True

    elif cod == 5:
        eigenvalue, eigenvector, iter = pm.solve_by_pm(A, [1]*len(A), tol)
        print("Higher eigenvalue: \n", str(eigenvalue))
        print("Higher eigenvector: \n", str(eigenvector))
        print("Iterations: \n", str(iter))

        if det == 0:
            print("The determinant can't be calculated by this method")
        valid_cod = True
    
    elif cod == 6:

        if utils.sym(A):
            eigenvalues, eigenvectors, iter = jcb_eigen.solve_by_jacobi_sym(A, tol)
            print("Eigenvalues: \n", str(np.transpose(eigenvalues)))
            print("Eigenvectors: \n", str(eigenvectors))
            print("Iterations: \n", str(iter))

        else:
            print("The matrix is not symmetric")

        if det == 0:
            d = 1
            for i in eigenvalues:
                d = d * i
            print("The determinant is ", str(d))
        valid_cod = True
    else:
        print("--------------------Warning!---------------------------")
        print("This is an invalid option, choose one from the list below.")
        print("-------------------------------------------------------")
