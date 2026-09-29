"""
CVE154 (A.Y. 2026-2027, S1)
Template script for Programming Activity No. 03

Prepared by Christian Cahig

This file belongs to the repository
https://github.com/christian-cahig/CVE154_AY-2026-2027-S1.
"""
import math as mt
import scipy.optimize as spo

__AUTHOR__ = "Group 2"


# Part 1. Core: Define fun and dfun
def fun(x, ed=0.01, Re=5000):
    """Univariate function z(x) for the Colebrook-White equation."""
    sqrt_x = mt.sqrt(x)
    term = ed / 3.7 + 2.51 / (Re * sqrt_x)
    return 1.0 / sqrt_x + 2.0 * mt.log10(term)

def dfun(x, ed=0.01, Re=5000):
    """Derivative function z'(x) with respect to x."""
    sqrt_x = mt.sqrt(x)
    x_3_2 = x * sqrt_x
    term = ed / 3.7 + 2.51 / (Re * sqrt_x)
    # Derivative analytical formulation
    return -0.5 / x_3_2 * (1.0 + 2.51 / (Re * term * mt.log(10)))


# Part 2. Synthesis

if __name__== "__main__":
# 2-1. Bisection Method
    e_bs = 1e-7
    a_0, b_0 = 0.008, 0.1
    x0_bs = (a_0, b_0)
    K_bs = mt.ceil(mt.log2((b_0 - a_0) / e_bs))

    z_bs = lambda x: fun(x, ed=0.0123456789, Re=9876.543210)

    x_bs_res = spo.root_scalar(z_bs, method='bisect', bracket=x0_bs, xtol=e_bs, rtol=e_bs, maxiter=K_bs)
    x_bs = x_bs_res.root
    x_bs_info = x_bs_res

    print("--- 2-1. Bisection ---")
    print(f"Verification z(x_bs) ≈ 0: {z_bs(x_bs)}")
    print(f"Iterations taken: {x_bs_info.iterations}")
    print(f"Friction factor: {x_bs}\n")


    # 2-2. Newton-Raphson Method
    e_nr = 1e-7
    x0_nr = x_bs
    K_nr = K_bs + 3

    z_nr = lambda x: fun(x, ed=0.0456789123, Re=6789.543210)
    dz_nr = lambda x: dfun(x, ed=0.0456789123, Re=6789.543210)

    x_nr_res = spo.root_scalar(z_nr, x0=x0_nr, fprime=dz_nr, method='newton', tol=e_nr, maxiter=K_nr)
    x_nr = x_nr_res.root
    x_nr_info = x_nr_res

    print("--- 2-2. Newton-Raphson ---")
    print(f"Verification z(x_nr) ≈ 0: {z_nr(x_nr)}")
    print(f"Iterations taken: {x_nr_info.iterations}")
    print(f"Friction factor: {x_nr}\n")


    # 2-3. Secant Method
    e_sc = 1e-7
    x0_sc = (x_bs, x_nr)
    K_sc = K_nr + 2

    z_sc = lambda x: fun(x, ed=0.0213789456, Re=4567.890123)

    x_sc_res = spo.root_scalar(z_sc, x0_sc[1], x1=x0_sc[0], method='secant', tol=e_sc, maxiter=K_sc)
    x_sc = x_sc_res.root
    x_sc_info = x_sc_res

    print("--- 2-3. Secant ---")
    print(f"Verification z(x_sc) ≈ 0: {z_sc(x_sc)}")
    print(f"Iterations taken: {x_sc_info.iterations}")
    print(f"Friction factor: {x_sc}\n")


    # 2-4. TOMS Algorithm 748
    e_to = 1e-7
    a_to, b_to = 0.008, 0.1
    x0_to = (a_to, b_to)
    K_to = mt.ceil(mt.log2((b_to - a_to) / e_to))

    z_to = lambda x: fun(x, ed=0.0321789456, Re=12345.6789)

    x_to_res = spo.root_scalar(z_to, method='toms748', bracket=x0_to, xtol=e_to, rtol=e_to, maxiter=K_to, k=2)
    x_to = x_to_res.root
    x_to_info = x_to_res

    print("--- 2-4. TOMS Algorithm 748 ---")
    print(f"Verification z(x_to) ≈ 0: {z_to(x_to)}")
    print(f"Iterations taken: {x_to_info.iterations}")
    print(f"Friction factor: {x_to}")

    #AVILA_BALALA_PUGOY_TACTACON