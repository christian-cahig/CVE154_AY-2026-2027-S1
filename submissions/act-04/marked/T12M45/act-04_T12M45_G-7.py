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

__AUTHOR__ = "Group 7"

def Ay(wL, wR, L):
    return L * (wR - 2.0 * wL) / 6.0


def By(wL, wR, L):
    return L * (2.0 * wR - wL) / 6.0


def polyvalder(coeffs, s):
    val = 0.0
    der = 0.0
    s_pow = 1.0 
    s_prev = 0.0 
    k = 0.0 
    for a in coeffs:
        val = val + a * s_pow
        der = der + k * a * s_prev
        s_prev = s_pow
        s_pow = s_pow * s
        k = k + 1.0
    return np.array([val, der])


def nu(x, wL, wR, L):
    C1 = Ay(wL, wR, L)
    coeffs = [C1, wL, -((wL + wR) / L) / 2.0]
    return polyvalder(coeffs, x)


def mu(x, wL, wR, L):
    C1 = Ay(wL, wR, L)
    C2 = 0.0
    coeffs = [C2, C1, wL / 2.0, -((wL + wR) / L) / 6.0]
    return polyvalder(coeffs, x)


def m(x, wL, wR, L):
    C1 = Ay(wL, wR, L)
    C2 = 0.0
    C3 = L * L * L * (8.0 * wL - 7.0 * wR) / 360.0  # from y(L) = 0
    coeffs = [C3, C2, C1 / 2.0, wL / 6.0, -((wL + wR) / L) / 24.0]
    return polyvalder(coeffs, x)


def y(x, wL, wR, L):
    C1 = Ay(wL, wR, L)
    C2 = 0.0
    C3 = L * L * L * (8.0 * wL - 7.0 * wR) / 360.0
    C4 = 0.0
    coeffs = [C4, C3, C2 / 2.0, C1 / 6.0, wL / 24.0, -((wL + wR) / L) / 120.0]
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
    