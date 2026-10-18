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
    return (wR - 2.0 * wL) * L / 6.0


def By(wL, wR, L):
    return (2.0 * wR - wL) * L / 6.0


def polyvalder(coeffs, s):
    val = 0.0
    der = 0.0
    for a in coeffs[::-1]:
        der = der * s + val
        val = val * s + a
    return np.array([val, der])


def nu(x, wL, wR, L):
    coeffs = [
        Ay(wL, wR, L),
        wL,
        -(wL + wR) / (2.0 * L),
    ]
    return polyvalder(coeffs, x)


def mu(x, wL, wR, L):
    coeffs = [
        0.0,
        Ay(wL, wR, L),
        wL / 2.0,
        -(wL + wR) / (6.0 * L),
    ]
    return polyvalder(coeffs, x)


def m(x, wL, wR, L):
    coeffs = [
        (8.0 * wL - 7.0 * wR) * L * L * L / 360.0,
        0.0,
        Ay(wL, wR, L) / 2.0,
        wL / 6.0,
        -(wL + wR) / (24.0 * L),
    ]
    return polyvalder(coeffs, x)


def y(x, wL, wR, L):
    coeffs = [
        0.0,
        (8.0 * wL - 7.0 * wR) * L * L * L / 360.0,
        0.0,
        Ay(wL, wR, L) / 6.0,
        wL / 24.0,
        -(wL + wR) / (120.0 * L),
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
    