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
    return (wR - 2 * wL) * L / 6


def By(wL, wR, L):
    return (2 * wR - wL) * L / 6


def polyvalder(a, s):
    p = a[-1]
    dp = 0

    for c in a[-2::-1]:
        dp = dp * s + p
        p = p * s + c

    return np.array([p, dp])


def nu(x, wL, wR, L):
    s = x / L

    a = [
        Ay(wL, wR, L),
        wL * L,
        -(wL + wR) * L / 2
    ]

    result = polyvalder(a, s)

    return np.array([result[0], result[1] / L])


def mu(x, wL, wR, L):
    s = x / L

    a = [
        0,
        Ay(wL, wR, L) * L,
        wL * L * L / 2,
        -(wL + wR) * L * L / 6
    ]

    result = polyvalder(a, s)

    return np.array([result[0], result[1] / L])


def m(x, wL, wR, L):
    s = x / L

    c1 = -(
        Ay(wL, wR, L) * L * L / 6
        + wL * L * L * L / 24
        - (wL + wR) * L * L * L / 120
    )

    a = [
        c1,
        0,
        Ay(wL, wR, L) * L * L / 2,
        wL * L * L * L / 6,
        -(wL + wR) * L * L * L / 24
    ]

    result = polyvalder(a, s)

    return np.array([result[0], result[1] / L])


def y(x, wL, wR, L):
    s = x / L

    c1 = -(
        Ay(wL, wR, L) * L * L / 6
        + wL * L * L * L / 24
        - (wL + wR) * L * L * L / 120
    )

    a = [
        0,
        c1 * L,
        0,
        Ay(wL, wR, L) * L * L * L / 6,
        wL * L * L * L / 24,
        -(wL + wR) * L * L * L * L / 120
    ]

    result = polyvalder(a, s)

    return np.array([result[0], result[1] / L])


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
    