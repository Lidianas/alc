# Álgebra Linear Computacional - 2023.1
# Trabalho 02
# Aluna: Filipe Santos Pacheco Prates e Lidiana Souza dos Anjos

import numpy as np
from sympy import symbols, diff

def jacobiana(f, n_eq, elements):
    
    jac = []
    for e in range(n_eq):
        tmp_f = f[e]
        f_diff = []
        for u in range(n_eq):  
            tmp_diff = diff(tmp_f, elements[u])
            f_diff.append(tmp_diff)
        jac.append(f_diff)
    return jac

def calc_jacobiana(j, v, j_elements):
    
    d = {}
    z = []
    for c in range(len(v)):
        d[str(j_elements[c])] = v[c]
    for df in range(len(j)):
        s = []
        for el in range(len(j)):
            r = eval(str(j[df][el]), d)
            s.append(r)
        z.append(s)
    return z

def calc_eq(eq, v, elements):
    s = []
    d = {}
    for c in range(len(v)):
        d[str(elements[c])] = v[c]
    for f in range(len(eq)):
        r = eval(str(eq[f]), d)
        s.append(r)
    return np.array(s)

def newton(equations, elements, initial_solution, tol):

    v = initial_solution
    new_v = [0, 0, 0]
    j = jacobiana(equations, 3, elements)
    iter = 0
    tolk = 1
    while tol <= tolk:
        f = calc_eq(equations, v, elements)
        j_c = calc_jacobiana(j, v, elements)
        inv_j = np.linalg.inv(j_c)
        delta_x = -(np.matmul(inv_j, f))
        new_v = v + delta_x
        tolk = np.linalg.norm(delta_x)/np.linalg.norm(new_v)
        v = new_v
        iter += 1
        if iter == 100:
            break
    print("The solution is \n", new_v)
    print("Number of iterations \n", iter)

def broyden(equations, elements, initial_solution, tol):

    v = initial_solution
    new_v = [0, 0, 0]
    j = jacobiana(equations, 3, elements)
    j_c = calc_jacobiana(j, v, elements)
    iter = 0
    tolk = 1    
    while tol <= tolk:
        f = calc_eq(equations, v, elements)
        inv_j = np.linalg.inv(j_c)
        delta_x = -(np.matmul(inv_j, f))
        new_v = v + delta_x
        y = calc_eq(equations, new_v, elements)-calc_eq(equations, v, elements)
        j_c = j_c + ((y - np.matmul(j_c, delta_x))*np.transpose(delta_x))/(np.transpose(delta_x)*delta_x)
        tolk = np.linalg.norm(delta_x)/np.linalg.norm(new_v)
        v = new_v
        iter += 1
        if iter == 100:
            break
    print("The solution is \n", new_v)
    print("Number of iterations \n", iter)

def main():
    x = symbols('x')
    y = symbols('y')
    z = symbols('z')
    eq = [16*x**4+16*y**4+z**4 - 16,x**2+y**2+z**2 - 3,x**3 - y + z - 1]
    print("----------------------------")
    print("|          Newton          |")
    print("----------------------------")
    newton(eq, [x, y, z], [1, 1, 1], 0.0001)
    print("----------------------------")
    print("----------------------------")
    print("|          Broyden         |")
    print("----------------------------")
    broyden(eq, [x, y, z], [1, 1, 1], 0.0001)
    print("----------------------------")
main()

