"""
CVE154 (A.Y. 2026-2027, S1)
Template script for Programming Activity No. 03

Prepared by Christian Cahig

This file belongs to the repository
https://github.com/christian-cahig/CVE154_AY-2026-2027-S1.
"""

import math as mt
import scipy.optimize as spo


# Part 1. Core

__AUTHOR__ = "Group 5"


def fun(x, ed=0.01, Re=5000):
    # Computes z(x) from the Colebrook-White equation.
    # z(x) = 1/sqrt(x) + 2 * log10(ed/3.7 + 2.51/(Re * sqrt(x)))
    return 1.0 / mt.sqrt(x) + 2.0 * mt.log10((ed / 3.7) + (2.51 / (Re * mt.sqrt(x))))


def dfun(x, ed=0.01, Re=5000):
    # Computes derivative z'(x) with respect to x.
    term1 = -0.5 * (x ** -1.5)
    u = (ed / 3.7) + (2.51 / (Re * mt.sqrt(x)))
    du_dx = -1.255 / (Re * (x ** 1.5))
    term2 = (2.0 / (u * mt.log(10))) * du_dx
    return term1 + term2

if __name__ == "__main__":
    
    # Part 2-1 BISECTION
    
    ed_bs = 0.0123456789
    Re_bs = 9876.543210
    e_bs = 10**-7
    x0_bs = (0.008, 0.1)
    K_bs = mt.ceil(mt.log2((x0_bs[1] - x0_bs[0]) / e_bs))

    z_bs = lambda x: fun(x, ed=ed_bs, Re=Re_bs)

    x_bs, x_bs_info = spo.bisect(
        z_bs,
        a=x0_bs[0],
        b=x0_bs[1],
        xtol=e_bs,
        rtol=e_bs,
        maxiter=K_bs,
        full_output=True,
    )

    print("Part 2-1. Bisection")
    print(f"{' '*3}rel. rough.: {ed_bs}")
    print(f"{' '*3}Reynolds n.: {Re_bs}")
    print(f"{' '*3}init. guess: {x0_bs}")
    print(f"{' '*3}max. iters.: {K_bs}")
    print(f"{' '*3}z({x_bs}) = {z_bs(x_bs)} in {x_bs_info.iterations} iters.")
    print(f"{' '*3}fric. fact.: {x_bs}\n")

    # Part 2-2 NETWON RAPHSON
    
    ed_nr = 0.0456789123
    Re_nr = 6789.543210
    e_nr = 10**-7
    x0_nr = x_bs
    K_nr = K_bs + 3

    z_nr = lambda x: fun(x, ed=ed_nr, Re=Re_nr)
    dz_nr = lambda x: dfun(x, ed=ed_nr, Re=Re_nr)

    x_nr, x_nr_info = spo.newton(
        z_nr,
        x0=x0_nr,
        fprime=dz_nr,
        tol=e_nr,
        maxiter=K_nr,
        full_output=True,
    )

    print("Part 2-2. Newton-Raphson")
    print(f"{' '*3}rel. rough.: {ed_nr}")
    print(f"{' '*3}Reynolds n.: {Re_nr}")
    print(f"{' '*3}init. guess: {x0_nr}")
    print(f"{' '*3}max. iters.: {K_nr}")
    print(f"{' '*3}z({x_nr}) = {z_nr(x_nr)} in {x_nr_info.iterations} iters.")
    print(f"{' '*3}fric. fact.: {x_nr}\n")

    # Part 2-3 SECANT
    
    ed_sc = 0.0213789456
    Re_sc = 4567.890123
    e_sc = 10**-7
    x0_sc = (x_bs, x_nr)
    K_sc = K_nr + 2

    z_sc = lambda x: fun(x, ed=ed_sc, Re=Re_sc)

    x_sc, x_sc_info = spo.newton(
        z_sc,
        x0=x0_sc[1],
        x1=x0_sc[0],
        tol=e_sc,
        maxiter=K_sc,
        full_output=True,
    )

    print("Part 2-3. Secant")
    print(f"{' '*3}rel. rough.: {ed_sc}")
    print(f"{' '*3}Reynolds n.: {Re_sc}")
    print(f"{' '*3}init. guess: {x0_sc}")
    print(f"{' '*3}max. iters.: {K_sc}")
    print(f"{' '*3}z({x_sc}) = {z_sc(x_sc)} in {x_sc_info.iterations} iters.")
    print(f"{' '*3}fric. fact.: {x_sc}\n")

    # Part 2-4 TOMS
    
    ed_to = 0.0321789456
    Re_to = 12345.6789
    e_to = 10**-7
    x0_to = (0.008, 0.1)
    K_to = mt.ceil(mt.log2((x0_to[1] - x0_to[0]) / e_to))

    z_to = lambda x: fun(x, ed=ed_to, Re=Re_to)

    x_to, x_to_info = spo.toms748(
        z_to,
        a=x0_to[0],
        b=x0_to[1],
        xtol=e_to,
        rtol=e_to,
        k=2,  
    maxiter=K_to,
    full_output=True,
    )

    print("Part 2-4. TOMS Algorithm 748")
    print(f"{' '*3}rel. rough.: {ed_to}")
    print(f"{' '*3}Reynolds n.: {Re_to}")
    print(f"{' '*3}init. guess: {x0_to}")
    print(f"{' '*3}max. iters.: {K_to}")
    print(f"{' '*3}z({x_to}) = {z_to(x_to)} in {x_to_info.iterations} iters.")
    print(f"{' '*3}fric. fact.: {x_to}")
