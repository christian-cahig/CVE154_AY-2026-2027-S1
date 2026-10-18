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
    return L * (wR - 2.0 * wL) / 6.0


def By(wL, wR, L):
    return L * (2.0 * wR - wL) / 6.0


def polyvalder(coeffs, s):
    p = coeffs[-1]
    dp = 0.0
    for a in coeffs[-2::-1]:
        dp = dp * s + p
        p = p * s + a
    return np.array([p, dp])


def nu(x, wL, wR, L):
    c = [Ay(wL, wR, L), wL, -(wL + wR) / (2.0 * L)]
    return polyvalder(c, x)


def mu(x, wL, wR, L):
    c = [0.0, Ay(wL, wR, L), wL / 2.0, -(wL + wR) / (6.0 * L)]
    return polyvalder(c, x)


def m(x, wL, wR, L):
    C1 = L * L * L * (8.0 * wL - 7.0 * wR) / 360.0
    c = [C1, 0.0, Ay(wL, wR, L) / 2.0, wL / 6.0, -(wL + wR) / (24.0 * L)]
    return polyvalder(c, x)


def y(x, wL, wR, L):
    C1 = L * L * L * (8.0 * wL - 7.0 * wR) / 360.0
    c = [0.0, C1, 0.0, Ay(wL, wR, L) / 6.0, wL / 24.0, -(wL + wR) / (120.0 * L)]
    return polyvalder(c, x)


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
    