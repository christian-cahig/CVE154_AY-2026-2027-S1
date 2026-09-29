"""
CVE154 (A.Y. 2026-2027, S1)
Template script for Programming Activity No. 03

Prepared by Christian Cahig

This file belongs to the repository
https://github.com/christian-cahig/CVE154_AY-2026-2027-S1.
"""

import math as mt
import scipy.optimize as spo


__AUTHOR__ = "Group 6"



# Part 0. Formulations


# Colebrook-White equation:
#
# 1 / sqrt(x) = -2 log10(eps/3.7 + 2.51/(Re*sqrt(x)))
#
# Therefore:
#
# z(x) = 1/sqrt(x) + 2 log10(eps/3.7 + 2.51/(Re*sqrt(x)))
#
# The derivative is:
#
# z'(x) = -1/(2*x^(3/2))
#         - (2.51/Re) /
#         (ln(10)*x^(3/2)*(eps/3.7 + 2.51/(Re*sqrt(x))))



# Part 1. Core


def fun(x, eps=0.01, Re=5000):
    

    return (
        1 / mt.sqrt(x)
        + 2 * mt.log10(
            eps / 3.7
            + 2.51 / (Re * mt.sqrt(x))
        )
    )


def dfun(x, eps=0.01, Re=5000):
    

    A = eps / 3.7
    B = 2.51 / Re

    return (
        -1 / (2 * x ** 1.5)
        - B / (
            mt.log(10)
            * x ** 1.5
            * (A + B / mt.sqrt(x))
        )
    )



# Part 2. Synthesis


if __name__ == "__main__":

    
    tol = 10 ** -7


    
    # Part 2-1. Bisection
   

    eps_bs = tol

    
    x0_bs = (0.0001, 1.0)

    
    K_bs = mt.ceil(
        mt.log2(
            (x0_bs[1] - x0_bs[0]) / eps_bs
        )
    )

    
    
    z_bs = lambda x: fun(
        x,
        eps=0.0123456789,
        Re=9876.543210
    )

    
    x_bs_info = spo.root_scalar(
        z_bs,
        bracket=x0_bs,
        method="bisect",
        xtol=eps_bs,
        rtol=eps_bs,
        maxiter=K_bs
    )

    
    x_bs = x_bs_info.root


    
    # Part 2-2. Newton-Raphson
    

    eps_nr = tol

    
    x0_nr = x_bs

    
    K_nr = K_bs + 3

   
    z_nr = lambda x: fun(
        x,
        eps=0.0456789123,
        Re=6789.543210
    )

    dz_nr = lambda x: dfun(
        x,
        eps=0.0456789123,
        Re=6789.543210
    )

    
    x_nr_info = spo.root_scalar(
        z_nr,
        fprime=dz_nr,
        x0=x0_nr,
        method="newton",
        xtol=eps_nr,
        rtol=eps_nr,
        maxiter=K_nr
    )

    
    x_nr = x_nr_info.root


    
    # Part 2-3. Secant
    

    eps_sc = tol

    
    x0_sc = (x_bs, x_nr)

    
    K_sc = K_nr + 2

    
    z_sc = lambda x: fun(
        x,
        eps=0.0213789456,
        Re=4567.890123
    )

    
    x_sc_info = spo.root_scalar(
        z_sc,
        x0=x0_sc[0],
        x1=x0_sc[1],
        method="secant",
        xtol=eps_sc,
        rtol=eps_sc,
        maxiter=K_sc
    )

    
    x_sc = x_sc_info.root


    
    # Part 2-4. TOMS Algorithm 748
    

    eps_to = tol

    
    x0_to = (0.0001, 1.0)

    
    K_to = mt.ceil(
        mt.log2(
            (x0_to[1] - x0_to[0]) / eps_to
        )
    )

    
    z_to = lambda x: fun(
        x,
        eps=0.0321789456,
        Re=12345.6789
    )

    
    x_to_info = spo.root_scalar(
        z_to,
        bracket=x0_to,
        method="toms748",
        xtol=eps_to,
        rtol=eps_to,
        maxiter=K_to
    )

    
    x_to = x_to_info.root


    
    

    # Part 2-1

    print("Part 2-1. Bisection")
    print(f"{' '*3}rel. rough.: {0.0123456789}")
    print(f"{' '*3}Reynolds n.: {9876.543210}")
    print(f"{' '*3}init. guess: {x0_bs}")
    print(f"{' '*3}max. iters.: {K_bs}")
    print(f"{' '*3}z({x_bs}) = {z_bs(x_bs)} in {x_bs_info.iterations} iters.")
    print(f"{' '*3}fric. fact.: {x_bs}")


    # Part 2-2

    print("Part 2-2. Newton-Raphson")
    print(f"{' '*3}rel. rough.: {0.0456789123}")
    print(f"{' '*3}Reynolds n.: {6789.543210}")
    print(f"{' '*3}init. guess: {x0_nr}")
    print(f"{' '*3}max. iters.: {K_nr}")
    print(f"{' '*3}z({x_nr}) = {z_nr(x_nr)} in {x_nr_info.iterations} iters.")
    print(f"{' '*3}fric. fact.: {x_nr}")


    # Part 2-3

    print("Part 2-3. Secant")
    print(f"{' '*3}rel. rough.: {0.0213789456}")
    print(f"{' '*3}Reynolds n.: {4567.890123}")
    print(f"{' '*3}init. guess: {x0_sc}")
    print(f"{' '*3}max. iters.: {K_sc}")
    print(f"{' '*3}z({x_sc}) = {z_sc(x_sc)} in {x_sc_info.iterations} iters.")
    print(f"{' '*3}fric. fact.: {x_sc}")


    # Part 2-4

    print("Part 2-4. TOMS Algorithm 748")
    print(f"{' '*3}rel. rough.: {0.0321789456}")
    print(f"{' '*3}Reynolds n.: {12345.6789}")
    print(f"{' '*3}init. guess: {x0_to}")
    print(f"{' '*3}max. iters.: {K_to}")
    print(f"{' '*3}z({x_to}) = {z_to(x_to)} in {x_to_info.iterations} iters.")
    print(f"{' '*3}fric. fact.: {x_to}")