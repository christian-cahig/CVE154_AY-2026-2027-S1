"""
CVE154 (A.Y. 2026-2027, S1)
Template script for Programming Activity No. 03

Prepared by Christian Cahig

This file belongs to the repository
https://github.com/christian-cahig/CVE154_AY-2026-2027-S1.
"""

import math as mt
import scipy.optimize as spo

__AUTHOR__ = "Group 5"

def fun(x, ed=0.01, Re=5000):
    """Colebrook-White residual function z(x)."""
    return 1.0 / mt.sqrt(x) + 2.0 * mt.log10(ed / 3.7 + 2.51 / (Re * mt.sqrt(x)))

def dfun(x, ed=0.01, Re=5000):
    """Derivative of z(x) with respect to x."""
    term = ed / 3.7 + 2.51 / (Re * mt.sqrt(x))
    dterm = -2.51 / (2.0 * Re * x * mt.sqrt(x))
    return -0.5 / (x * mt.sqrt(x)) + 2.0 / (mt.log(10) * term) * dterm


if __name__ == "__main__":
    # Part 2-1. Bisection
    e_bs = 1e-7
    x0_bs = (0.01, 0.1)
    K_bs = int(mt.ceil(mt.log2((x0_bs[1] - x0_bs[0]) / e_bs)))
    z_bs = lambda x: fun(x, ed=0.0123456789, Re=9876.543210)
    
    res_bs = spo.root_scalar(z_bs, bracket=x0_bs, method='bisect', rtol=e_bs, xtol=e_bs, maxiter=K_bs)
    x_bs = res_bs.root
    x_bs_info = res_bs

    print("Part 2-1. Bisection")
    print(f"{' '*3}rel. rough.: {0.0123456789}")
    print(f"{' '*3}Reynolds n.: {9876.543210}")
    print(f"{' '*3}init. guess: {x0_bs}")
    print(f"{' '*3}max. iters.: {K_bs}")
    print(f"{' '*3}z({x_bs}) = {z_bs(x_bs)} in {x_bs_info.iterations} iters.")
    print(f"{' '*3}fric. fact.: {x_bs}")

    # Part 2-2. Newton-Raphson
    e_nr = 1e-7
    x0_nr = x_bs
    K_nr = K_bs + 3
    z_nr = lambda x: fun(x, ed=0.0456789123, Re=6789.543210)
    dz_nr = lambda x: dfun(x, ed=0.0456789123, Re=6789.543210)

    res_nr = spo.root_scalar(z_nr, x0=x0_nr, fprime=dz_nr, method='newton', xtol=e_nr, maxiter=K_nr)
    x_nr = res_nr.root
    x_nr_info = res_nr

    print("Part 2-2. Newton-Raphson")
    print(f"{' '*3}rel. rough.: {0.0456789123}")
    print(f"{' '*3}Reynolds n.: {6789.543210}")
    print(f"{' '*3}init. guess: {x0_nr}")
    print(f"{' '*3}max. iters.: {K_nr}")
    print(f"{' '*3}z({x_nr}) = {z_nr(x_nr)} in {x_nr_info.iterations} iters.")
    print(f"{' '*3}fric. fact.: {x_nr}")

    # Part 2-3. Secant
    e_sc = 1e-7
    x0_sc = (x_bs, x_nr)
    K_sc = K_nr + 2
    z_sc = lambda x: fun(x, ed=0.0213789456, Re=4567.890123)

    res_sc = spo.root_scalar(z_sc, x0=x0_sc[1], x1=x0_sc[0], method='secant', xtol=e_sc, maxiter=K_sc)
    x_sc = res_sc.root
    x_sc_info = res_sc
        
    print("Part 2-3. Secant")
    print(f"{' '*3}rel. rough.: {0.0213789456}")
    print(f"{' '*3}Reynolds n.: {4567.890123}")
    print(f"{' '*3}init. guess: {x0_sc}")
    print(f"{' '*3}max. iters.: {K_sc}")
    print(f"{' '*3}z({x_sc}) = {z_sc(x_sc)} in {x_sc_info.iterations} iters.")
    print(f"{' '*3}fric. fact.: {x_sc}")

    # Part 2-4. TOMS Algorithm 748
    e_to = 1e-7
    x0_to = (0.01, 0.1)
    K_to = int(mt.ceil(mt.log2((x0_to[1] - x0_to[0]) / e_to)))
    z_to = lambda x: fun(x, ed=0.0321789456, Re=12345.6789)

    res_to = spo.root_scalar(z_to, bracket=x0_to, method='toms748', rtol=e_to, xtol=e_to, options={'k': 2}, maxiter=K_to)
    x_to = res_to.root
    x_to_info = res_to
        
    print("Part 2-4. TOMS Algorithm 748")
    print(f"{' '*3}rel. rough.: {0.0321789456}")
    print(f"{' '*3}Reynolds n.: {12345.6789}")
    print(f"{' '*3}init. guess: {x0_to}")
    print(f"{' '*3}max. iters.: {K_to}")
    print(f"{' '*3}z({x_to}) = {z_to(x_to)} in {x_to_info.iterations} iters.")
    print(f"{' '*3}fric. fact.: {x_to}")