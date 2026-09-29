"""
CVE154 (A.Y. 2026-2027, S1)
Template script for Programming Activity No. 03

Prepared by Christian Cahig

This file belongs to the repository
https://github.com/christian-cahig/CVE154_AY-2026-2027-S1.
"""

import math as mt
import scipy.optimize as spo

__AUTHOR__ = "Group 3"

def fun(x, ed = 0.01, Re = 5000):
    return 1 / mt.sqrt(x) + 2 * mt.log10(ed / 3.7 + 2.51 / (Re * mt.sqrt(x)))

def dfun(x, ed = 0.01, Re = 5000):
    return -1 / (2 * x**(3/2)) + 2 * (1 / (mt.log(10) * (ed / 3.7 + 2.51 / (Re * mt.sqrt(x)))) * (-2.51 / (2 * Re * x**(3/2))))



if __name__ == "__main__":
# Part 2-1
   
    e_bs = 1e-7                          # Tolerance
    x0_bs = (0.01, 0.1)                  # Initial interval [a0, b0]
    a0, b0 = x0_bs
    K_bs = mt.ceil(mt.log2((b0 - a0) / e_bs))
    z_bs = lambda x: fun(x, ed=0.0123456789, Re=9876.543210)
    x_bs, x_bs_info = spo.bisect(z_bs, a0, b0, rtol=e_bs, xtol=e_bs, maxiter=K_bs, full_output=True)



    print("Part 2-1. Bisection")
    print(f"{' '*3}rel. rough.: {0.0123456789}")
    print(f"{' '*3}Reynolds n.: {9876.543210}")
    print(f"{' '*3}init. guess: {x0_bs}")
    print(f"{' '*3}max. iters.: {K_bs}")
    print(f"{' '*3}z({x_bs}) = {z_bs(x_bs)} in {x_bs_info.iterations} iters.")
    print(f"{' '*3}fric. fact.: {x_bs}")


    # Part 2-2
    
    e_nr = e_bs                 # Tolerance
    x0_nr = x_bs                # Initial estimate is the root found in Section 2-1
    K_nr = K_bs + 3             # Iteration budget is three more than in Section 2-1
    z_nr = lambda x: fun(x, ed=0.0456789123, Re=6789.543210)
    dz_nr = lambda x: dfun(x, ed=0.0456789123, Re=6789.543210)
    x_nr, x_nr_info = spo.newton(z_nr,x0_nr,fprime=dz_nr,tol=e_nr,maxiter=K_nr,full_output=True)


    print("Part 2-2. Newton-Raphson")
    print(f"{' '*3}rel. rough.: {0.0456789123}")
    print(f"{' '*3}Reynolds n.: {6789.543210}")
    print(f"{' '*3}init. guess: {x0_nr}")
    print(f"{' '*3}max. iters.: {K_nr}")
    print(f"{' '*3}z({x_nr}) = {z_nr(x_nr)} in {x_nr_info.iterations} iters.")
    print(f"{' '*3}fric. fact.: {x_nr}")

    # Part 2-3
        
    e_sc = e_nr                  # Tolerance (same as previous)
    x0_sc = (x_bs, x_nr)         # Tuple: (x_{-1}, x_0) -> (root from 2-1, root from 2-2)
    K_sc = K_nr + 2 
    z_sc = lambda x: fun(x, ed=0.0213789456, Re=4567.890123)
    x_sc, x_sc_info = spo.newton(z_sc, x1=x0_sc[1],x1=x0_sc[0],tol=e_sc,maxiter=K_sc,full_output=True)

    print("Part 2-3. Secant")
    print(f"{' '*3}rel. rough.: {0.0213789456}")
    print(f"{' '*3}Reynolds n.: {4567.890123}")
    print(f"{' '*3}init. guess: {x0_sc}")
    print(f"{' '*3}max. iters.: {K_sc}")
    print(f"{' '*3}z({x_sc}) = {z_sc(x_sc)} in {x_sc_info.iterations} iters.")
    print(f"{' '*3}fric. fact.: {x_sc}")

    # Part 2-4
        
    e_to = e_sc                  # Tolerance 
    x0_to = (0.01, 0.1)          # Initial interval [a0, b0]
    a0_to, b0_to = x0_to
    K_to = mt.ceil(mt.log2((b0_to - a0_to) / e_to))
    z_to = lambda x: fun(x, ed=0.0321789456, Re=12345.6789)
    x_to, x_to_info = spo.toms748(z_to,a0_to,b0_to,rtol=e_to,xtol=e_to,k=2,maxiter=K_to,full_output=True)

    print("Part 2-4. TOMS Algorithm 748")
    print(f"{' '*3}rel. rough.: {0.0321789456}")
    print(f"{' '*3}Reynolds n.: {12345.6789}")
    print(f"{' '*3}init. guess: {x0_to}")
    print(f"{' '*3}max. iters.: {K_to}")
    print(f"{' '*3}z({x_to}) = {z_to(x_to)} in {x_to_info.iterations} iters.")
    print(f"{' '*3}fric. fact.: {x_to}")
