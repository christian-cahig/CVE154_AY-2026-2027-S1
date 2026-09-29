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
    """Evaluates the Colebrook-White function z(x)."""
    term = (ed / 3.7) + (2.51 / (Re * mt.sqrt(x)))
    return (1.0 / mt.sqrt(x)) + 2.0 * mt.log10(term)

def dfun(x, ed=0.01, Re=5000):
    """Evaluates the derivative of the Colebrook-White function z'(x)."""
    term = (ed / 3.7) + (2.51 / (Re * mt.sqrt(x)))
    numerator = 5.02
    denominator = Re * mt.log(10) * term
    return -0.5 * (x ** -1.5) * (1.0 + (numerator / denominator))

if __name__ == "__main__":

    
    # Part 2-1. Bisection
    e_bs = 1e-7
    x0_bs = (0.001, 0.1) # Realistic bracket for friction factors (a0, b0)
    # Iteration budget for bisection: ceil(log2((b0 - a0) / tol))
    K_bs = mt.ceil(mt.log2((x0_bs[1] - x0_bs[0]) / e_bs))

    z_bs = lambda x: fun(x, ed=0.0123456789, Re=9876.543210)

    x_bs, x_bs_info = spo.bisect(
        z_bs, 
        a=x0_bs[0], 
        b=x0_bs[1], 
        xtol=e_bs, 
        rtol=e_bs, 
        maxiter=K_bs, 
        full_output=True
    )


    print("Part 2-1. Bisection")
    print(f"{' '*3}rel. rough.: {0.0123456789}")
    print(f"{' '*3}Reynolds n.: {9876.543210}")
    print(f"{' '*3}init. guess: {x0_bs}")
    print(f"{' '*3}max. iters.: {K_bs}")
    print(f"{' '*3}z({x_bs}) = {z_bs(x_bs)} in {x_bs_info.iterations} iters.")
    print(f"{' '*3}fric. fact.: {x_bs:.10f}")

    # Part 2-2. Newton-Raphson
    e_nr = 1e-7
    x0_nr = x_bs
    K_nr = K_bs + 3

    z_nr = lambda x: fun(x, ed=0.0456789123, Re=6789.543210)
    dz_nr = lambda x: dfun(x, ed=0.0456789123, Re=6789.543210)

    x_nr, x_nr_info = spo.newton(
        func=z_nr, 
        x0=x0_nr, 
        fprime=dz_nr, 
        tol=e_nr, 
        maxiter=K_nr, 
        full_output=True
    )

    print("Part 2-2. Newton-Raphson")
    print(f"{' '*3}rel. rough.: {0.0456789123}")
    print(f"{' '*3}Reynolds n.: {6789.543210}")
    print(f"{' '*3}init. guess: {x0_nr}")
    print(f"{' '*3}max. iters.: {K_nr}")
    print(f"{' '*3}z({x_nr}) = {z_nr(x_nr)} in {x_nr_info.iterations} iters.")
    print(f"{' '*3}fric. fact.: {x_nr:.10f}")


    # Part 2-3. Secant
    e_sc = 1e-7
    x0_sc = (float(x_bs), float(x_nr)) # (x_-1, x_0)
    K_sc = K_nr + 2

    z_sc = lambda x: fun(x, ed=0.0213789456, Re=4567.890123)

    x_sc, x_sc_info = spo.newton(
        func=z_sc, 
        x0=x0_sc[1], 
        fprime=None, 
        tol=e_sc, 
        maxiter=K_sc, 
        full_output=True, 
        x1=x0_sc[0]
    )

    print("Part 2-3. Secant")
    print(f"{' '*3}rel. rough.: {0.0213789456}")
    print(f"{' '*3}Reynolds n.: {4567.890123}")
    print(f"{' '*3}init. guess: {x0_sc}")
    print(f"{' '*3}max. iters.: {K_sc}")
    print(f"{' '*3}z({x_sc}) = {z_sc(x_sc)} in {x_sc_info.iterations} iters.")
    print(f"{' '*3}fric. fact.: {x_sc:.10f}")


    # Part 2-4. TOMS Algorithm 748
    e_to = 1e-7
    x0_to = (0.001, 0.1) # Same realistic bracket as bisection
    # Same iteration budget derivation as bisection to guarantee tolerance bracket
    K_to = mt.ceil(mt.log2((x0_to[1] - x0_to[0]) / e_to))

    z_to = lambda x: fun(x, ed=0.0321789456, Re=12345.6789)

    x_to, x_to_info = spo.toms748(
        f=z_to, 
        a=x0_to[0], 
        b=x0_to[1], 
        k=2, 
        xtol=e_to, 
        rtol=e_to, 
        maxiter=K_to, 
        full_output=True
    )

    print("Part 2-4. TOMS Algorithm 748")
    print(f"{' '*3}rel. rough.: {0.0321789456}")
    print(f"{' '*3}Reynolds n.: {12345.6789}")
    print(f"{' '*3}init. guess: {x0_to}")
    print(f"{' '*3}max. iters.: {K_to}")
    print(f"{' '*3}z({x_to}) = {z_to(x_to)} in {x_to_info.iterations} iters.")
    print(f"{' '*3}fric. fact.: {x_to:.10f}")

