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


# Part 0/1. Core: z(x) and z'(x)
#
#   Colebrook-White:  1/sqrt(f) = -2*log10( ed/3.7 + 2.51/(Re*sqrt(f)) )
#
#   Letting x stand in for f, and moving everything to one side:
#       z(x) = 1/sqrt(x) + 2*log10( ed/3.7 + 2.51/(Re*sqrt(x)) )
#   z(x) = 0 exactly when x equals the friction factor f.


def _u(x, ed, Re):
    """Helper: the argument of the log10 term."""
    return ed / 3.7 + 2.51 / (Re * mt.sqrt(x))


def fun(x, ed=0.01, Re=5000):
    """z(x): residual of the Colebrook-White equation."""
    return 1 / mt.sqrt(x) + 2 * mt.log10(_u(x, ed, Re))


def dfun(x, ed=0.01, Re=5000):
    """z'(x): derivative of fun with respect to x."""
    u = _u(x, ed, Re)
    return x ** (-1.5) * (-0.5 - 2.51 / (Re * mt.log(10) * u))


# Part 2. Synthesis
# Tolerance for every method: 1e-7

# 2-1. Bisection
# ed = 0.0123456789, Re = 9876.543210

e_bs = 1e-7
x0_bs = (0.008, 0.1)          # (a0, b0); z changes sign across this interval
K_bs = mt.ceil(mt.log2((x0_bs[1] - x0_bs[0]) / e_bs))  # NMPy3 Sec. 4.3

z_bs = lambda x: fun(x, ed=0.0123456789, Re=9876.543210)

x_bs, x_bs_info = spo.bisect(
    z_bs, x0_bs[0], x0_bs[1],
    rtol=e_bs, xtol=e_bs,
    maxiter=K_bs,
    full_output=True,
)

assert mt.isclose(z_bs(x_bs), 0, abs_tol=1e-4), "x_bs is not a root of z"


# 2-2. Newton-Raphson
# ed = 0.0456789123, Re = 6789.543210

e_nr = 1e-7
x0_nr = x_bs                  # initial estimate: root from Section 2-1
K_nr = K_bs + 3

z_nr = lambda x: fun(x, ed=0.0456789123, Re=6789.543210)
dz_nr = lambda x: dfun(x, ed=0.0456789123, Re=6789.543210)

x_nr, x_nr_info = spo.newton(
    z_nr, x0=x0_nr, fprime=dz_nr,
    tol=e_nr, maxiter=K_nr,
    full_output=True,
)

assert mt.isclose(z_nr(x_nr), 0, abs_tol=1e-4), "x_nr is not a root of z"


# 2-3. Secant
# ed = 0.0213789456, Re = 4567.890123

e_sc = 1e-7
x0_sc = (x_bs, x_nr)           # (x_{-1}, x_0) = roots from 2-1, 2-2
K_sc = K_nr + 2

z_sc = lambda x: fun(x, ed=0.0213789456, Re=4567.890123)

x_sc, x_sc_info = spo.newton(
    z_sc, x0=x0_sc[1], x1=x0_sc[0],
    tol=e_sc, maxiter=K_sc,
    full_output=True,
)

assert mt.isclose(z_sc(x_sc), 0, abs_tol=1e-4), "x_sc is not a root of z"


# 2-4. TOMS Algorithm 748
# ed = 0.0321789456, Re = 12345.6789

e_to = 1e-7
x0_to = (0.008, 0.1)
K_to = mt.ceil(mt.log2((x0_to[1] - x0_to[0]) / e_to))  # NMPy3 Sec. 4.3

z_to = lambda x: fun(x, ed=0.0321789456, Re=12345.6789)

x_to, x_to_info = spo.toms748(
    z_to, x0_to[0], x0_to[1],
    rtol=e_to, xtol=e_to, k=2,
    maxiter=K_to,
    full_output=True,
)

assert mt.isclose(z_to(x_to), 0, abs_tol=1e-4), "x_to is not a root of z"


if __name__ == "__main__":
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