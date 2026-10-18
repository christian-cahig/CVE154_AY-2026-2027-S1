"""
CVE154 (A.Y. 2026-2027, S1)
Template script for Programming Activity No. 04

Prepared by Christian Cahig

This file belongs to the repository
https://github.com/christian-cahig/CVE154_AY-2026-2027-S1.
"""

import math as mt
import scipy.optimize as spo
import numpy as np

__AUTHOR__ = "Group 3"


def Ay(w_L, w_R, L):
    """Compute reaction force at support A."""
    return - (2.0 * w_L - w_R) * L / 6.0


def By(w_L, w_R, L):
    """Compute reaction force at support B."""
    return L * (2.0 * w_R - w_L) / 6.0


def polyvalder(coeffs, s):
    """
    Evaluates a polynomial and its first derivative at s using only
    multiplication, addition, and for loops.
    coeffs: list of coefficients [a0, a1, a2, ..., an]
    Returns: np.array([value, derivative])
    """
    val = 0.0
    der = 0.0

    # Evaluate polynomial: sum(a_k * s^k)
    s_pow = 1.0
    for a in coeffs:
        val = val + a * s_pow
        s_pow = s_pow * s

    # Evaluate derivative: sum(k * a_k * s^(k-1))
    s_pow = 1.0
    for k in range(1, len(coeffs)):
        der = der + k * coeffs[k] * s_pow
        s_pow = s_pow * s

    return np.array([val, der])


def nu(x, w_L, w_R, L):
    """Computes shear force v(x) and its derivative v'(x)."""
    ay = Ay(w_L, w_R, L)
    a0 = ay
    a1 = w_L
    a2 = -(w_L + w_R) / (2.0 * L)
    coeffs = [a0, a1, a2]
    return polyvalder(coeffs, x)


def mu(x, w_L, w_R, L):
    """Computes bending moment mu(x) and its derivative mu'(x)."""
    ay = Ay(w_L, w_R, L)
    a0 = 0.0
    a1 = ay
    a2 = w_L / 2.0
    a3 = -(w_L + w_R) / (6.0 * L)
    coeffs = [a0, a1, a2, a3]
    return polyvalder(coeffs, x)


def m(x, w_L, w_R, L):
    """Computes slope m(x) and its derivative m'(x)."""
    ay = Ay(w_L, w_R, L)
    C1 = (8.0 * w_L - 7.0 * w_R) * (L * L * L) / 360.0
    a0 = C1
    a1 = 0.0
    a2 = ay / 2.0
    a3 = w_L / 6.0
    a4 = -(w_L + w_R) / (24.0 * L)
    coeffs = [a0, a1, a2, a3, a4]
    return polyvalder(coeffs, x)


def y(x, w_L, w_R, L):
    """Computes deflection y(x) and its derivative y'(x)."""
    ay = Ay(w_L, w_R, L)
    C1 = (8.0 * w_L - 7.0 * w_R) * (L * L * L) / 360.0
    a0 = 0.0
    a1 = C1
    a2 = 0.0
    a3 = ay / 6.0
    a4 = w_L / 24.0
    a5 = -(w_L + w_R) / (120.0 * L)
    coeffs = [a0, a1, a2, a3, a4, a5]
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
