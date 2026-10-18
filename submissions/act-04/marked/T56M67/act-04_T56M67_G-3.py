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


def Ay(wL, wR, L):
    """Vertical reaction at the left hinge A."""
    return L * (wR - 2.0 * wL) / 6.0


def By(wL, wR, L):
    """Vertical reaction at the right hinge B."""
    return L * (2.0 * wR - wL) / 6.0


def polyvalder(a, s):
    """Value and derivative of a0 + a1*s + ... + an*s^n via Horner's scheme."""
    p = 0.0
    dp = 0.0
    for ak in reversed(a):
        dp = dp * s + p
        p = p * s + ak
    return np.array([p, dp])


def nu(x, wL, wR, L):
    """Internal shear and its derivative at x."""
    a = [Ay(wL, wR, L), wL, -(wL + wR) / (2.0 * L)]
    return polyvalder(a, x)


def mu(x, wL, wR, L):
    """Bending moment and its derivative at x."""
    a = [0.0, Ay(wL, wR, L), wL / 2.0, -(wL + wR) / (6.0 * L)]
    return polyvalder(a, x)


def m(x, wL, wR, L):
    """Slope and its derivative at x."""
    c1 = L * L * L * (8.0 * wL - 7.0 * wR) / 360.0
    a = [c1, 0.0, Ay(wL, wR, L) / 2.0, wL / 6.0, -(wL + wR) / (24.0 * L)]
    return polyvalder(a, x)


def y(x, wL, wR, L):
    """Deflection and its derivative at x."""
    c1 = L * L * L * (8.0 * wL - 7.0 * wR) / 360.0
    a = [0.0, c1, 0.0, Ay(wL, wR, L) / 6.0, wL / 24.0, -(wL + wR) / (120.0 * L)]
    return polyvalder(a, x)


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
