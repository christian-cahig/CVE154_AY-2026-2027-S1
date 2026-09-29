"""
CVE154 (A.Y. 2026-2027, S1)
Template script for Programming Activity No. 03

Prepared by Christian Cahig

This file belongs to the repository
https://github.com/christian-cahig/CVE154_AY-2026-2027-S1.
"""

# =====================================================================
# Part 0. Formulations
# ---------------------------------------------------------------------
# Colebrook-White:
#     1/sqrt(f) = -2 log10( ed/3.7 + 2.51 / (Re sqrt(f)) )
#
# Let x = f (the friction factor). Moving everything to one side gives
#     z(x)  = 1/sqrt(x) + 2 log10( ed/3.7 + 2.51 / (Re sqrt(x)) )
# z(x) = 0 exactly when the left- and right-hand sides are equal.
# Its derivative with respect to x is
#     z'(x) = -0.5 x^(-3/2)
#             - 2.51 x^(-3/2) / ( Re ln(10) ( ed/3.7 + 2.51 / (Re sqrt(x)) ) )
# =====================================================================

# =====================================================================
# Part 1. Core
# =====================================================================

import math as mt
import scipy.optimize as spo

__AUTHOR__ = "Group 5"


def _arg(x, ed, Re):
    # Auxiliary helper: the argument of the logarithm,
    # ed/3.7 + 2.51 / (Re sqrt(x))
    return (ed / 3.7) + (2.51 / (Re * mt.sqrt(x)))


def fun(x, ed=0.01, Re=5000):
    return (1 / mt.sqrt(x)) + (2 * mt.log10(_arg(x, ed, Re)))


def dfun(x, ed=0.01, Re=5000):
    x32 = x ** -1.5
    return (-0.5 * x32) - ((2.51 * x32) / (Re * mt.log(10) * _arg(x, ed, Re)))


# =====================================================================
# Part 2. Synthesis
# =====================================================================

if __name__ == "__main__":
    # Part 2-1

    e_bs = 1e-7
    x0_bs = (0.005, 0.1)
    K_bs = mt.ceil(mt.log2((x0_bs[1] - x0_bs[0]) / e_bs))
    z_bs = lambda x: fun(x, ed=0.0123456789, Re=9876.543210)
    x_bs, x_bs_info = spo.bisect(
        z_bs, x0_bs[0], x0_bs[1],
        xtol=e_bs, rtol=e_bs, maxiter=K_bs, full_output=True
    )

    print("Part 2-1. Bisection")
    print(f"{' '*3}rel. rough.: {0.0123456789}")
    print(f"{' '*3}Reynolds n.: {9876.543210}")
    print(f"{' '*3}init. guess: {x0_bs}")
    print(f"{' '*3}max. iters.: {K_bs}")
    print(f"{' '*3}z({x_bs}) = {z_bs(x_bs)} in {x_bs_info.iterations} iters.")
    print(f"{' '*3}fric. fact.: {x_bs}")

    # Part 2-2

    e_nr = 1e-7
    x0_nr = x_bs
    K_nr = K_bs + 3
    z_nr = lambda x: fun(x, ed=0.0456789123, Re=6789.543210)
    dz_nr = lambda x: dfun(x, ed=0.0456789123, Re=6789.543210)
    x_nr, x_nr_info = spo.newton(
        z_nr, x0_nr, fprime=dz_nr,
        tol=e_nr, maxiter=K_nr, full_output=True
    )

    print("Part 2-2. Newton-Raphson")
    print(f"{' '*3}rel. rough.: {0.0456789123}")
    print(f"{' '*3}Reynolds n.: {6789.543210}")
    print(f"{' '*3}init. guess: {x0_nr}")
    print(f"{' '*3}max. iters.: {K_nr}")
    print(f"{' '*3}z({x_nr}) = {z_nr(x_nr)} in {x_nr_info.iterations} iters.")
    print(f"{' '*3}fric. fact.: {x_nr}")

    # Part 2-3

    e_sc = 1e-7
    x0_sc = (x_bs, x_nr)
    K_sc = K_nr + 2
    z_sc = lambda x: fun(x, ed=0.0213789456, Re=4567.890123)
    x_sc, x_sc_info = spo.newton(
        z_sc, x0_sc[1], x1=x0_sc[0],
        tol=e_sc, maxiter=K_sc, full_output=True
    )

    print("Part 2-3. Secant")
    print(f"{' '*3}rel. rough.: {0.0213789456}")
    print(f"{' '*3}Reynolds n.: {4567.890123}")
    print(f"{' '*3}init. guess: {x0_sc}")
    print(f"{' '*3}max. iters.: {K_sc}")
    print(f"{' '*3}z({x_sc}) = {z_sc(x_sc)} in {x_sc_info.iterations} iters.")
    print(f"{' '*3}fric. fact.: {x_sc}")

    # Part 2-4

    e_to = 1e-7
    x0_to = (0.005, 0.1)
    K_to = mt.ceil(mt.log2((x0_to[1] - x0_to[0]) / e_to))
    z_to = lambda x: fun(x, ed=0.0321789456, Re=12345.6789)
    x_to, x_to_info = spo.toms748(
        z_to, x0_to[0], x0_to[1],
        k=2, rtol=e_to, xtol=e_to, maxiter=K_to, full_output=True
    )

    print("Part 2-4. TOMS Algorithm 748")
    print(f"{' '*3}rel. rough.: {0.0321789456}")
    print(f"{' '*3}Reynolds n.: {12345.6789}")
    print(f"{' '*3}init. guess: {x0_to}")
    print(f"{' '*3}max. iters.: {K_to}")
    print(f"{' '*3}z({x_to}) = {z_to(x_to)} in {x_to_info.iterations} iters.")
    print(f"{' '*3}fric. fact.: {x_to}")
