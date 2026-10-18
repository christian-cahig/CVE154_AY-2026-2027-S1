"""
CVE154 (A.Y. 2026-2027, S1)
Template script for Programming Activity No. 04

Prepared by Christian Cahig

This file belongs to the repository
https://github.com/christian-cahig/CVE154_AY-2026-2027-S1.
"""


# =====================================================================
# Part 1. Core
# =====================================================================

import math as mt
import scipy.optimize as spo
import numpy as np

__AUTHOR__ = "Group 5"


def Ay(wL, wR, L):
    return L * (wR - 2.0 * wL) / 6.0


def By(wL, wR, L):
    return L * (2.0 * wR - wL) / 6.0


def polyvalder(a, s):
    p = 0.0
    dp = 0.0
    for c in reversed(a):
        dp = dp * s + p
        p = p * s + c
    return np.array([p, dp])


def nu(x, wL, wR, L):
    k = (wL + wR) / L
    A = L * (wR - 2.0 * wL) / 6.0
    coeffs = [A, wL, -k / 2.0]
    return polyvalder(coeffs, x)


def mu(x, wL, wR, L):
    k = (wL + wR) / L
    A = L * (wR - 2.0 * wL) / 6.0
    coeffs = [0.0, A, wL / 2.0, -k / 6.0]
    return polyvalder(coeffs, x)


def m(x, wL, wR, L):
    k = (wL + wR) / L
    A = L * (wR - 2.0 * wL) / 6.0
    C3 = L * L * L * (8.0 * wL - 7.0 * wR) / 360.0
    coeffs = [C3, 0.0, A / 2.0, wL / 6.0, -k / 24.0]
    return polyvalder(coeffs, x)


def y(x, wL, wR, L):
    k = (wL + wR) / L
    A = L * (wR - 2.0 * wL) / 6.0
    C3 = L * L * L * (8.0 * wL - 7.0 * wR) / 360.0
    coeffs = [0.0, C3, 0.0, A / 6.0, wL / 24.0, -k / 120.0]
    return polyvalder(coeffs, x)


# =====================================================================
# Part 2. Synthesis
# =====================================================================

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
