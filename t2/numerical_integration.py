# Álgebra Linear Computacional - 2023.1
# Trabalho 02
# Aluna: Filipe Santos Pacheco Prates e Lidiana Souza dos Anjos

from sympy import symbols
import numpy as np
import math
import decimal

def f(eq, p, elements):
    d = {}
    d[str(elements)] = round(p, 4)
    return eval(str(eq), d)

def simpson(eq, a, b, el):
    l = b - a
    m = (a+b)/2
    simp = (l/6)*(f(eq, a, el)+4*f(eq, m, el)+f(eq, b, el))
    return simp

def numerical_integration(eq, interval, tol, elements):
    tolk = 1
    n_inter = 3
    a, b = interval[0], interval[1]
    i = simpson(eq, a, b, elements)
    l = b-a
    iter = 0
    pair = []
    while tolk >= tol:
        i_new = 0
        n_inter = 2*n_inter-1
        a, b = interval[0], interval[1]
        d = l/(n_inter-1)
        for c in range(n_inter-1):
            b = a+d
            i_new = i_new + simpson(eq, a, b, elements)
            a = a+d
        pair.append([n_inter, i_new])
        iter+=1
        tolk = abs(i_new-i)/abs(i_new)
        i = i_new
        if iter == 20:
            break
    return iter, pair

def print_res(eq, it, pair, el):

    print("---------------------------------------------")
    print("For the equation ", eval(str(eq),{"w":el}), ":")
    print("- number of iterations: ", it)
    for c in range(len(pair)):
        print("nº of points: ", pair[c][0], " integral: ", pair[c][1])
    print("---------------------------------------------")

def main():
    #questão 6
    print("---------------------------------------------")
    print("Questão 6")
    w = symbols('w')
    w_n = 1.0
    eps = 0.05
    s_n = 2.0
    rao = 1/(((1-(w/w_n)**2)**2+(2*eps*(w/w_n))**2))**(1/2)
    eq = (rao**2)*s_n
    f_m0 = [eq, [0, 10]]
    f_m2 = [eq*(w**2), [0, 10]]
    it0, pr0 = numerical_integration(f_m0[0], f_m0[1], 0.0001, w)
    it2, pr2 = numerical_integration(f_m2[0], f_m2[1], 0.000001, w)
    print_res(f_m0[0], it0, pr0, w)
    print_res(f_m2[0], it2, pr2, w)

    """#questão 7
    print("---------------------------------------------")
    print("Questão 7")
    hs = 3.0
    tz = 5.0
    s_n = ((4*(np.pi**3)*(hs**2))/((w**5)*(tz**4)))*(math.e**(-(16*(np.pi**3))/(w**4)*(tz**4)))
    rao = 1/(((1-(w/w_n)**2)**2+(2*eps*(w/w_n))**2))**(1/2)
    eq = (rao**2)*s_n
    f_m0 = [eq, [0, 10]]
    f_m2 = [eq*(w**2), [0, 10]]
    it0, pr0 = numerical_integration(f_m0[0], f_m0[1], 0.0001, w)
    it2, pr2 = numerical_integration(f_m2[0], f_m2[1], 0.0001, w)
    print_res(f_m0[0], it0, pr0, w)
    print_res(f_m2[0], it2, pr2, w)"""

main()