"""
CVE154 (A.Y. 2026-2027, S1)
Template script for Programming Activity No. 03

Prepared by Christian Cahig

This file belongs to the repository
https://github.com/christian-cahig/CVE154_AY-2026-2027-S1.
"""

import math as mt
import scipy.optimize as spo

__AUTHOR__ = "Group 1"


# Part 1. Core

def fun(x, ed=0.01, Re=5000):
    # Computes the Colebrook-White function
    return x + 2 * mt.log10(ed/3.7 + 2.51*x/Re)


def dfun(x, ed=0.01, Re=5000):
    # Computes the derivative of the Colebrook-White function
    return 1 + (2/mt.log(10)) * (2.51/Re) / (ed/3.7 + 2.51*x/Re)


if __name__ == "__main__":

    # Part 2-1
    
    print("Part 2-1. Bisection")

    ed_bs = 0.0123456789
    Re_bs = 9876.543210

    x0_bs = (1, 10)
    K_bs = 100
    tol_bs = 1e-7

    z_bs = lambda x: fun(x, ed=ed_bs, Re=Re_bs)

    x_bs, x_bs_info = spo.bisect(
        z_bs,
        x0_bs[0],
        x0_bs[1],
        xtol=tol_bs,
        maxiter=K_bs,
        full_output=True,
        disp=False
    )

    print(f"{' '*3}rel. rough.: {ed_bs}")
    print(f"{' '*3}Reynolds n.: {Re_bs}")
    print(f"{' '*3}init. guess: {x0_bs}")
    print(f"{' '*3}max. iters.: {K_bs}")
    print(f"{' '*3}z({x_bs}) = {z_bs(x_bs)} in {x_bs_info.iterations} iters.")
    print(f"{' '*3}fric. fact.: {1/(x_bs**2):.8f}")

    # Part 2-2
    
    print("\nPart 2-2. Newton-Raphson")

    ed_nr = 0.0456789123
    Re_nr = 6789.543210

    x0_nr = x_bs
    K_nr = 100
    tol_nr = 1e-7

    z_nr = lambda x: fun(x, ed=ed_nr, Re=Re_nr)
    dz_nr = lambda x: dfun(x, ed=ed_nr, Re=Re_nr)

    x_nr, x_nr_info = spo.newton(
        z_nr,
        x0_nr,
        fprime=dz_nr,
        tol=tol_nr,
        maxiter=K_nr,
        full_output=True,
        disp=False
    )

    print(f"{' '*3}rel. rough.: {ed_nr}")
    print(f"{' '*3}Reynolds n.: {Re_nr}")
    print(f"{' '*3}init. guess: {x0_nr}")
    print(f"{' '*3}max. iters.: {K_nr}")
    print(f"{' '*3}z({x_nr}) = {z_nr(x_nr)} in {x_nr_info.iterations} iters.")
    print(f"{' '*3}fric. fact.: {1/(x_nr**2):.8f}")

    # Part 2-3
        
    print("\nPart 2-3. Secant")

    ed_sc = 0.0213789456
    Re_sc = 4567.890123

    x0_sc = (x_bs, x_nr)
    K_sc = 100
    tol_sc = 1e-7

    z_sc = lambda x: fun(x, ed=ed_sc, Re=Re_sc)

    x_sc_info = spo.root_scalar(
        z_sc,
        method="secant",
        x0=x0_sc[0],
        x1=x0_sc[1],
        xtol=tol_sc,
        maxiter=K_sc
    )

    x_sc = x_sc_info.root

    print(f"{' '*3}rel. rough.: {ed_sc}")
    print(f"{' '*3}Reynolds n.: {Re_sc}")
    print(f"{' '*3}init. guess: {x0_sc}")
    print(f"{' '*3}max. iters.: {K_sc}")
    print(f"{' '*3}z({x_sc}) = {z_sc(x_sc)} in {x_sc_info.iterations} iters.")
    print(f"{' '*3}fric. fact.: {1/(x_sc**2):.8f}")

    # Part 2-4
        
    print("\nPart 2-4. TOMS Algorithm 748")

    ed_to = 0.0321789456
    Re_to = 12345.6789

    x0_to = (1, 10)
    K_to = 100
    tol_to = 1e-7

    z_to = lambda x: fun(x, ed=ed_to, Re=Re_to)

    x_to_info = spo.root_scalar(
        z_to,
        method="toms748",
        bracket=x0_to,
        xtol=tol_to,
        maxiter=K_to
    )

    x_to = x_to_info.root

    print(f"{' '*3}rel. rough.: {ed_to}")
    print(f"{' '*3}Reynolds n.: {Re_to}")
    print(f"{' '*3}init. guess: {x0_to}")
    print(f"{' '*3}max. iters.: {K_to}")
    print(f"{' '*3}z({x_to}) = {z_to(x_to)} in {x_to_info.iterations} iters.")
    print(f"{' '*3}fric. fact.: {1/(x_to**2):.8f}")