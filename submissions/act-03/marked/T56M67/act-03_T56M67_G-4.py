"""
CVE154 (A.Y. 2026-2027, S1)
Activity No. 03: Numerical Solution of the Colebrook-White Equation

Section: T56M67
Group: 4
"""

import math as mt
import scipy.optimize as spo

__AUTHOR__ = "Group 4"


# =============================================================================
# PART 0 & 1: CORE FORMULATIONS & FUNCTIONS
# =============================================================================

# Part 0a. Derivation of g(x):
# Colebrook-White equation:
# 1 / sqrt(f) = -2 * log10( (ed / 3.7) + (2.51 / (Re * sqrt(f))) )
#
# Substituting x = 1 / sqrt(f), we get f = 1 / x^2.
# Rearranging into root-finding form g(x) = 0:
# g(x) = x + 2 * log10( (ed / 3.7) + (2.51 * x / Re) )


def fun(x, ed=0.01, Re=5000):
    """
    Computes g(x) derived from the Colebrook-White equation.
    g(x) = x + 2 * log10(ed/3.7 + 2.51*x/Re)
    """
    arg = (ed / 3.7) + (2.51 * x / Re)
    return x + 2.0 * mt.log10(arg)


# Part 0b. Derivation of g'(x):
# Using natural log identity: log10(u) = ln(u) / ln(10)
# d/dx [ 2 * log10(u) ] = 2 / (ln(10) * u) * du/dx
# where u(x) = ed/3.7 + (2.51 / Re) * x  ==>  du/dx = 2.51 / Re
#
# g'(x) = 1 + (2 * 2.51) / (ln(10) * Re * u(x))
# g'(x) = 1 + 5.02 / (ln(10) * Re * (ed/3.7 + 2.51*x/Re))


def dfun(x, ed=0.01, Re=5000):
    """
    Computes dg/dx, the first derivative of g(x) with respect to x.
    """
    arg = (ed / 3.7) + (2.51 * x / Re)
    return 1.0 + 5.02 / (mt.log(10.0) * Re * arg)


# =============================================================================
# PART 2: SYNTHESIS
# =============================================================================

if __name__ == "__main__":

    # -------------------------------------------------------------------------
    # Part 2-1. Bisection
    # -------------------------------------------------------------------------
    ed_bs = 0.0123456789
    Re_bs = 9876.543210

    e_bs = 1e-6
    x0_bs = (1.0, 20.0)

    a_bs, b_bs = x0_bs
    K_bs = mt.ceil(mt.log2((b_bs - a_bs) / e_bs))

    z_bs = lambda x: fun(x, ed=ed_bs, Re=Re_bs)

    x_bs, x_bs_info = spo.bisect(
        z_bs,
        a_bs,
        b_bs,
        rtol=e_bs,
        xtol=e_bs,
        maxiter=K_bs,
        full_output=True,
        disp=False,
    )

    f_bs = 1.0 / (x_bs**2)

    print("Part 2-1. Bisection")
    print(f"{' '*3}rel. rough.: {0.0123456789}")
    print(f"{' '*3}Reynolds n.: {9876.543210}")
    print(f"{' '*3}init. guess: {x0_bs}")
    print(f"{' '*3}max. iters.: {K_bs}")
    print(f"{' '*3}z({x_bs}) = {z_bs(x_bs)} in {x_bs_info.iterations} iters.")
    print(f"{' '*3}fric. fact.: {f_bs}\n")

    # -------------------------------------------------------------------------
    # Part 2-2. Newton-Raphson
    # -------------------------------------------------------------------------
    ed_nr = 0.0456789123
    Re_nr = 6789.543210

    e_nr = 1e-6
    x0_nr = x_bs
    K_nr = K_bs + 3

    z_nr = lambda x: fun(x, ed=ed_nr, Re=Re_nr)
    dz_nr = lambda x: dfun(x, ed=ed_nr, Re=Re_nr)

    x_nr, x_nr_info = spo.newton(
        z_nr,
        x0_nr,
        fprime=dz_nr,
        tol=e_nr,
        maxiter=K_nr,
        full_output=True,
        disp=False,
    )

    f_nr = 1.0 / (x_nr**2)

    print("Part 2-2. Newton-Raphson")
    print(f"{' '*3}rel. rough.: {0.0456789123}")
    print(f"{' '*3}Reynolds n.: {6789.543210}")
    print(f"{' '*3}init. guess: {x0_nr}")
    print(f"{' '*3}max. iters.: {K_nr}")
    print(f"{' '*3}z({x_nr}) = {z_nr(x_nr)} in {x_nr_info.iterations} iters.")
    print(f"{' '*3}fric. fact.: {f_nr}\n")

    # -------------------------------------------------------------------------
    # Part 2-3. Secant
    # -------------------------------------------------------------------------
    ed_sc = 0.0213789456
    Re_sc = 4567.890123

    e_sc = 1e-6
    x0_sc = (x_bs, x_nr)
    K_sc = K_nr + 2

    z_sc = lambda x: fun(x, ed=ed_sc, Re=Re_sc)

    x_sc, x_sc_info = spo.newton(
        z_sc,
        x0_sc[0],
        x1=x0_sc[1],
        tol=e_sc,
        maxiter=K_sc,
        full_output=True,
        disp=False,
    )

    f_sc = 1.0 / (x_sc**2)

    print("Part 2-3. Secant")
    print(f"{' '*3}rel. rough.: {0.0213789456}")
    print(f"{' '*3}Reynolds n.: {4567.890123}")
    print(f"{' '*3}init. guess: {x0_sc}")
    print(f"{' '*3}max. iters.: {K_sc}")
    print(f"{' '*3}z({x_sc}) = {z_sc(x_sc)} in {x_sc_info.iterations} iters.")
    print(f"{' '*3}fric. fact.: {f_sc}\n")

    # -------------------------------------------------------------------------
    # Part 2-4. TOMS Algorithm 748
    # -------------------------------------------------------------------------
    ed_to = 0.0321789456
    Re_to = 12345.6789

    e_to = 1e-6
    x0_to = (1.0, 20.0)

    a_to, b_to = x0_to
    K_to = mt.ceil(mt.log2((b_to - a_to) / e_to))

    z_to = lambda x: fun(x, ed=ed_to, Re=Re_to)

    x_to, x_to_info = spo.toms748(
        z_to,
        a_to,
        b_to,
        rtol=e_to,
        xtol=e_to,
        k=2,
        maxiter=K_to,
        full_output=True,
        disp=False,
    )

    f_to = 1.0 / (x_to**2)

    print("Part 2-4. TOMS Algorithm 748")
    print(f"{' '*3}rel. rough.: {0.0321789456}")
    print(f"{' '*3}Reynolds n.: {12345.6789}")
    print(f"{' '*3}init. guess: {x0_to}")
    print(f"{' '*3}max. iters.: {K_to}")
    print(f"{' '*3}z({x_to}) = {z_to(x_to)} in {x_to_info.iterations} iters.")
    print(f"{' '*3}fric. fact.: {f_to}\n")