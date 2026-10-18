

import math as mt
import scipy.optimize as spo
import numpy as np

__AUTHOR__ = "Group 4"

def Ay(L, wL, wR):
    """Computes the support reaction Ay at x = 0."""
    return (2.0 * wL + wR) * L / 6.0

def By(L, wL, wR):
    """Computes the support reaction By at x = L."""
    return (wL + 2.0 * wR) * L / 6.0

def polyvalder(coeffs, x):
    """
    Evaluates the value and the derivative of any polynomial using 
    only *, +, and for loops (no ** or mt.pow).
    """
    val = 0.0
    der = 0.0
    n = len(coeffs) - 1
    for i, c in enumerate(coeffs):
        deg = n - i
        x_deg = 1.0
        for _ in range(deg):
            x_deg = x_deg * x
        val = val + c * x_deg
        
        if deg > 0:
            x_deg_minus_1 = 1.0
            for _ in range(deg - 1):
                x_deg_minus_1 = x_deg_minus_1 * x
            der = der + c * deg * x_deg_minus_1
            
    return np.array([val, der])

def nu(L, wL, wR, x):
    """Computes distributed load w(x) and its derivative at location x."""
    coeffs = [(wR - wL) / L, wL]
    return polyvalder(coeffs, x)

def mu(L, wL, wR, x):
    """Computes internal shear V(x) and its derivative at location x."""
    ay_val = Ay(L, wL, wR)
    coeffs = [- (wR - wL) / (2.0 * L), - wL, ay_val]
    return polyvalder(coeffs, x)

def m(L, wL, wR, x):
    """Computes bending moment M(x) and its derivative at location x."""
    ay_val = Ay(L, wL, wR)
    coeffs = [- (wR - wL) / (6.0 * L), - wL / 2.0, ay_val, 0.0]
    return polyvalder(coeffs, x)

def y(L, wL, wR, x):
    """Computes deflection EI*y(x) and slope EI*y'(x) at location x."""
    ay_val = Ay(L, wL, wR)
    L3 = L * L * L
    theta_0 = - (8.0 * wL + 7.0 * wR) * L3 / 360.0
    coeffs = [
        - (wR - wL) / (120.0 * L),
        - wL / 24.0,
        ay_val / 6.0,
        0.0,
        theta_0,
        0.0
    ]
    return polyvalder(coeffs, x)

if __name__ == "__main__":
    wl, wr, L = 1, 7, 1
    print(f"wL = {wl} N/m; wR = {wr} N/m; L = {L} m")
    print(
        f"{' '*3}Ay: {Ay(wl, wr, L):.7f}",
        f"By: {By(wl, wr, L):.7f}",
        sep="\t"
    )
    for x in np.linspace(0, L, num=5, endpoint=True):
        print(f"{' '*3}@ x = {x} m")
        for fun in [nu, mu, m, y]:
            v, dv = fun(x, wl, wr, L)
            print(
                f"{' '*6}{fun.__name__}: {v:.7f}",
                f"{fun.__name__+"'"}: {dv:.7f}",
                sep="\t"
            )
    