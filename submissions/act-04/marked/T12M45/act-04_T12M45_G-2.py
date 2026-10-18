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
    return L * (wR - 2 * wL) / 6


def By(wL, wR, L):
    return L * (2 * wR - wL) / 6


def polyvalder(coefficients, s):
    value = 0
    derivative = 0
    power = 1
    d_power = 0
    for a in coefficients:
        value = value + a * power
        derivative = derivative + a * d_power
        d_power = d_power * s + power
        power = power * s
    return np.array([value, derivative])


def nu(x, wL, wR, L):
    coefficients = [Ay(wL, wR, L), wL, -(wL + wR) / (2 * L)]
    return polyvalder(coefficients, x)


def mu(x, wL, wR, L):
    coefficients = [0, Ay(wL, wR, L), wL / 2, -(wL + wR) / (6 * L)]
    return polyvalder(coefficients, x)


def m(x, wL, wR, L):
    C = L * L * L * (8 * wL - 7 * wR) / 360
    coefficients = [C, 0, Ay(wL, wR, L) / 2, wL / 6,
                    -(wL + wR) / (24 * L)]
    return polyvalder(coefficients, x)


def y(x, wL, wR, L):
    C = L * L * L * (8 * wL - 7 * wR) / 360
    coefficients = [0, C, 0, Ay(wL, wR, L) / 6,
                    wL / 24, -(wL + wR) / (120 * L)]
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
    