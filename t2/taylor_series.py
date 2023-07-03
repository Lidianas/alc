# Álgebra Linear Computacional - 2023.1
# Trabalho 02
# Aluna: Filipe Santos Pacheco Prates e Lidiana Souza dos Anjos

import numpy as np
from sympy import symbols

def calc_function(eq, v, elements):

    d = {}
    if len(elements) == 1:
        d[str(elements[0])] = v
    else:
        for c in range(len(elements)):
            d[str(elements[c])] = v[c]
    d['Abs'] = abs
    r = eval(str(eq), d)

    return np.array(r)

def taylor(eq, initial_conditions, h, T, elements):
    v = initial_conditions
    t = 0
    ddz = 0
    while t <= T:
        v[0] = t
        v[1] = v[1] + v[2]*h+(ddz*(h**2))/2
        v[2] = v[2] + ddz*h
        ddz = calc_function(eq, v[2], elements)
        print("t = ", t, "and z(t) = ", round(v[1], 4))
        print("-------------------------")
        t = round(t + h, 1)
    print("Final solution: \n")
    print("z = ",round(v[1], 4), "| t = ", t-h)

def rkn(eq, initial_conditions, h, T, elements, pos_el):

    v = initial_conditions
    t = 0
    k1, k2, k3, k4 = 0,0,0,0
    while t <= T:
        v[1] = v[1] + h*(v[2]+(1/3)*(k1+k2+k3))
        v[2] = v[2] + (1/3)*(k1+2*k2+2*k3+k4)
        k1 = (1/2)*h*(calc_function(eq, v[pos_el], elements)) 
        q = (1/2)*h*(v[2]+(1/2)*k1)
        tmp_k2 = [v[0]+(h/2),v[1]+q,v[2]+k1]
        k2 = (1/2)*h*(calc_function(eq, tmp_k2[pos_el], elements))
        tmp_k3 = [v[0]+(h/2),v[1]+q,v[2]+k2]
        k3 = (1/2)*h*(calc_function(eq, tmp_k3[pos_el], elements))
        l = h*(v[2]+k3)
        tmp_k4 = [v[0]+h,v[1]+l,v[2]+2*k3]
        k4 = (1/2)*h*(calc_function(eq, tmp_k4[pos_el], elements))
        print("t = ", t, "and z(t) = ", round(v[1], 4))
        print("-------------------------")
        t = round(t + h, 1)
    print("Final solution: \n")
    print("z = ",round(v[1], 4), "| t = ", t-h)

def main():
    g = 9.807
    k_d = 1.0
    dz = symbols('dz')
    ddz = -g - k_d*dz*abs(dz)
    h = 0.1
    T = 1
    pos_el = 2
    print("Choose the operation \n 1 - Taylor Series \n 2 - Runge-Kutta-Nystron \n")
    cod = int(input("Type the operation number \n"))    
    if cod == 1:
        print("Taylor Serie")
        taylor(ddz, [0, 0, 0], h, T, [dz])
    if cod==2:
        print("Runde-Kutta-Nystron")
        rkn(ddz, [0, 0, 0], h, T, [dz], pos_el)

main()