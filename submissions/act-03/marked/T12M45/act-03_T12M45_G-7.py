"""
CVE154 (A.Y. 2026-2027, S1)
Template script for Programming Activity No. 03

Prepared by Christian Cahig

This file belongs to the repository
https://github.com/christian-cahig/CVE154_AY-2026-2027-S1.
"""

import math as mt
import scipy.optimize as spo

__AUTHOR__ = "Group 7"

def fun(x, ed=0.01, Re=5000):
    """Colebrook-White residual function z(x).

    x corresponds to 1 / sqrt(f).
    """
    u = (ed / 3.7) + (2.51 * x / Re)
    return x + 2.0 * mt.log10(u)

def dfun(x, ed=0.01, Re=5000):
    """First derivative dz/dx of the Colebrook-White residual function."""
    u = (ed / 3.7) + (2.51 * x / Re)
    du = 2.51 / Re
    return 1.0 + (2.0 / mt.log(10.0)) * (du / u)

if __name__ == "__main__":

    # Part 2-1. Bisection
    ed_bs = 0.0123456789
    Re_bs = 9876.543210

    e_bs = 1e-7
    x0_bs = (1.0, 20.0)
    K_bs = mt.ceil(mt.log2((x0_bs[1] - x0_bs[0]) / e_bs))

    z_bs = lambda x: fun(x, ed=ed_bs, Re=Re_bs)

    x_bs, x_bs_info = spo.bisect(
        z_bs, x0_bs[0], x0_bs[1],
        rtol=e_bs, xtol=e_bs, maxiter=K_bs,
        full_output=True, disp=False,
    )

    if not x_bs_info.converged:
        print(f"{' ' * 3}Bisection did not converge!")

    f_bs = 1.0 / x_bs ** 2

    print("Part 2-1. Bisection")
    print(f"{' ' * 3}rel. rough.: {ed_bs}")
    print(f"{' ' * 3}Reynolds n.: {Re_bs}")
    print(f"{' ' * 3}init. guess: {x0_bs}")
    print(f"{' ' * 3}max. iters.: {K_bs}")
    print(f"{' ' * 3}z({x_bs}) = {z_bs(x_bs)} in {x_bs_info.iterations} iters.")
    print(f"{' ' * 3}fric. fact.: {f_bs}")

    # Part 2-2. Newton-Raphson
    ed_nr = 0.0456789123
    Re_nr = 6789.543210

    e_nr = 1e-7
    x0_nr = x_bs
    K_nr = K_bs + 3

    z_nr = lambda x: fun(x, ed=ed_nr, Re=Re_nr)
    dz_nr = lambda x: dfun(x, ed=ed_nr, Re=Re_nr)

    x_nr, x_nr_info = spo.newton(
        z_nr, x0_nr, fprime=dz_nr,
        tol=e_nr, maxiter=K_nr,
        full_output=True, disp=False,
    )

    if not x_nr_info.converged:
        print(f"{' ' * 3}Newton-Raphson did not converge!")

    f_nr = 1.0 / x_nr ** 2

    print("Part 2-2. Newton-Raphson")
    print(f"{' ' * 3}rel. rough.: {ed_nr}")
    print(f"{' ' * 3}Reynolds n.: {Re_nr}")
    print(f"{' ' * 3}init. guess: {x0_nr}")
    print(f"{' ' * 3}max. iters.: {K_nr}")
    print(f"{' ' * 3}z({x_nr}) = {z_nr(x_nr)} in {x_nr_info.iterations} iters.")
    print(f"{' ' * 3}fric. fact.: {f_nr}")

    # Part 2-3. Secant
    ed_sc = 0.0213789456
    Re_sc = 4567.890123

    e_sc = 1e-7
    x0_sc = (x_bs, x_nr)
    K_sc = K_nr + 2

    z_sc = lambda x: fun(x, ed=ed_sc, Re=Re_sc)

    x_sc, x_sc_info = spo.newton(
        z_sc, x0_sc[1], x1=x0_sc[0],
        tol=e_sc, maxiter=K_sc,
        full_output=True, disp=False,
    )

    if not x_sc_info.converged:
        print(f"{' ' * 3}Secant method did not converge!")

    f_sc = 1.0 / x_sc ** 2

    print("Part 2-3. Secant")
    print(f"{' ' * 3}rel. rough.: {ed_sc}")
    print(f"{' ' * 3}Reynolds n.: {Re_sc}")
    print(f"{' ' * 3}init. guess: {x0_sc}")
    print(f"{' ' * 3}max. iters.: {K_sc}")
    print(f"{' ' * 3}z({x_sc}) = {z_sc(x_sc)} in {x_sc_info.iterations} iters.")
    print(f"{' ' * 3}fric. fact.: {f_sc}")

    # Part 2-4. TOMS Algorithm 748
    ed_to = 0.0321789456
    Re_to = 12345.6789

    e_to = 1e-7
    x0_to = (1.0, 20.0)
    K_to = mt.ceil(mt.log2((x0_to[1] - x0_to[0]) / e_to))

    z_to = lambda x: fun(x, ed=ed_to, Re=Re_to)

    x_to, x_to_info = spo.toms748(
        z_to, x0_to[0], x0_to[1],
        k=2,
        xtol=e_to, rtol=e_to, maxiter=K_to,
        full_output=True, disp=False,
    )

    if not x_to_info.converged:
        print(f"{' ' * 3}TOMS 748 did not converge!")

    f_to = 1.0 / x_to ** 2

    print("Part 2-4. TOMS Algorithm 748")
    print(f"{' ' * 3}rel. rough.: {ed_to}")
    print(f"{' ' * 3}Reynolds n.: {Re_to}")
    print(f"{' ' * 3}init. guess: {x0_to}")
    print(f"{' ' * 3}max. iters.: {K_to}")
    print(f"{' ' * 3}z({x_to}) = {z_to(x_to)} in {x_to_info.iterations} iters.")
    print(f"{' ' * 3}fric. fact.: {f_to}")