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

__AUTHOR__ = "Group 2"

def Ay(wL, wR, L):
    return L * (wR - (2 * wL)) / 6


def By(wL, wR, L):
    return L * ((2 * wR) - wL) / 6


def polyvalder(coeffs, s):
    p = coeffs[-1]
    dp = 0.0

    for i in range(len(coeffs) - 2, -1, -1):
        dp = dp * s + p
        p = p * s + coeffs[i]

    return np.array([p, dp])


def nu(x, wL, wR, L):
    a0 = Ay(wL, wR, L)
    a1 = wL
    a2 = -(wL + wR) / (2 * L)

    return polyvalder([a0, a1, a2], x)


def mu(x, wL, wR, L):
    a0 = 0.0
    a1 = Ay(wL, wR, L)
    a2 = wL / 2
    a3 = -(wL + wR) / (6 * L)

    return polyvalder([a0, a1, a2, a3], x)


def m(x, wL, wR, L):
    c = (L**3) * ((8 * wL) - (7 * wR)) / 360

    a0 = c
    a1 = 0.0
    a2 = Ay(wL, wR, L) / 2
    a3 = wL / 6
    a4 = -(wL + wR) / (24 * L)

    return polyvalder([a0, a1, a2, a3, a4], x)


def y(x, wL, wR, L):
    c = (L * L * L) * ((8 * wL) - (7 * wR)) / 360

    a0 = 0.0
    a1 = c
    a2 = 0.0
    a3 = Ay(wL, wR, L) / 6
    a4 = wL / 24
    a5 = -(wL + wR) / (120 * L)

    return polyvalder([a0, a1, a2, a3, a4, a5], x)

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
