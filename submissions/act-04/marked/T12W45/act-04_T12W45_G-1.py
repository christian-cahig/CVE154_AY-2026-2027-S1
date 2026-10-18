
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

__AUTHOR__ = "Group 4"


def Ay(wL, wR, L):
    return L * (wR - 2 * wL) / 6


def By(wL, wR, L):
    return L * (2 * wR - wL) / 6


def polyvalder(coefficients, s):
    p = coefficients[-1]
    dp = 0

    for i in range(len(coefficients) - 2, -1, -1):
        dp = dp * s + p
        p = p * s + coefficients[i]

    return np.array([p, dp])


def nu(x, wL, wR, L):
    ay = Ay(wL, wR, L)
    coefficients = [ay, wL, - (wL + wR) / (2 * L)]

    return polyvalder(coefficients, x)


def mu(x, wL, wR, L):
    ay = Ay(wL, wR, L)
    coefficients = [0, ay, wL / 2, -(wL + wR) / (6 * L)]

    return polyvalder(coefficients, x)


def m(x, wL, wR, L):
    ay = Ay(wL, wR, L)
    C2 = ( -ay * L * L / 6 -wL * L * L * L / 24 + (wL + wR) * L * L * L / 120)
    coefficients = [C2, 0, ay / 2, wL / 6, - (wL + wR) / (24 * L)]

    return polyvalder(coefficients, x)


def y(x, wL, wR, L):
    ay = Ay(wL, wR, L)
    C2 = ( -ay * L * L / 6 -wL * L * L * L / 24 + (wL + wR) * L * L * L / 120)
    coefficients = [0, C2, 0, ay / 6, wL / 24, -(wL + wR) / (120 * L)]

    return polyvalder(coefficients, x)


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
    