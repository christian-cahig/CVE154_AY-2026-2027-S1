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

__AUTHOR__ = "Group 6"


def Ay(wL, wR, L):
    return (L / 6.0) * (2.0 * wL + wR)


def By(wL, wR, L):
    return (L / 6.0) * (wL + 2.0 * wR)


def polyvalder(coeffs, s):
    p_val = 0.0
    dp_val = 0.0

    for a in reversed(coeffs):
        p_val = p_val * s + a

    n = len(coeffs)
    for i in range(n - 1, 0, -1):
        dp_val = dp_val * s + i * coeffs[i]

    return np.array([p_val, dp_val])


def nu(x, wL, wR, L):
    
    A_y = Ay(wL, wR, L)
    a0 = A_y
    a1 = -wL
    a2 = -(wR - wL) / (2.0 * L)

    coeffs = [a0, a1, a2]
    return polyvalder(coeffs, x)


def mu(x, wL, wR, L):

    A_y = Ay(wL, wR, L)
    a0 = 0.0
    a1 = A_y
    a2 = -wL / 2.0
    a3 = -(wR - wL) / (6.0 * L)

    coeffs = [a0, a1, a2, a3]
    return polyvalder(coeffs, x)


def m(x, wL, wR, L):

    A_y = Ay(wL, wR, L)
    C1 = -(L**3 / 360.0) * (7.0 * wL + 8.0 * wR)

    a0 = C1
    a1 = 0.0
    a2 = A_y / 2.0
    a3 = -wL / 6.0
    a4 = -(wR - wL) / (24.0 * L)

    coeffs = [a0, a1, a2, a3, a4]
    return polyvalder(coeffs, x)


def y(x, wL, wR, L):

    A_y = Ay(wL, wR, L)
    C1 = -(L**3 / 360.0) * (7.0 * wL + 8.0 * wR)

    a0 = 0.0
    a1 = C1
    a2 = 0.0
    a3 = A_y / 6.0
    a4 = -wL / 24.0
    a5 = -(wR - wL) / (120.0 * L)

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
