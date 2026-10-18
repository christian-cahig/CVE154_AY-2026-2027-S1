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

__AUTHOR__ = "Group 17"

def Ay(wl, wr, L):
	return (wr - (2 * wl)) * L / 6

def By(wl, wr, L):
	return ((2 * wr) - wl) * L / 6

def polyvalder(coeffs, x):
    p = 0; dp = 0
    for a in reversed(coeffs):
        dp = (x * dp) + p
        p = (x * p) + a
    return np.array([p, dp])

def nu(x, wl, wr, L):
    a = [
        (wr - (2 * wl)) * L / 6,
        wl,
        -(wl + wr) / (2 * L)
    ]
    return polyvalder(a, x)

def mu(x, wl, wr, L):
    a = [
        0,
        (wr - (2 * wl)) * L / 6,
        wl / 2,
        -(wl + wr) / (6 * L)
    ]
    return polyvalder(a, x)

def m(x, wl, wr, L):
    a = [
        ((8 * wl) - (7 * wr)) * (L**3) / 360,
        0,
        (wr - (2 * wl)) * L / 12,
        wl / 6,
        -(wl + wr) / (24 * L)
    ]
    return polyvalder(a, x)

def y(x, wl, wr, L):
    a = [
        0,
        ((8 * wl) - (7 * wr)) * (L**3) / 360,
        0,
        (wr - (2 * wl)) * L / 36,
        wl / 24,
        -(wl + wr) / (120 * L)
    ]
    return polyvalder(a, x)

if __name__ == "__main__":
    CASES = {
        "1" : (34, 18, 38),
        "2" : (18, 34, 42),
        "3" : (37, 37, 42),
        "4" : (21, 21, 4),
        "5" : (17, 9, 24),
    }

    case = 4
    wl, wr, L = CASES[str(int(case))]

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


    eps = 1e-7; Kmax = 214

    f = lambda x : nu(x, wl, wr, L)[0]
    df = lambda x : nu(x, wl, wr, L)[1]
    g = lambda x : m(x, wl, wr, L)[0]
    dg = lambda x : m(x, wl, wr, L)[1]

    print(f"{' '*3}Local extrema of mu(x)")
    for x0 in np.linspace(0, L, num=5, endpoint=True):
        x_maxmom, x_maxmom_info = spo.newton(f, x0, fprime=df, tol=eps, maxiter=Kmax, full_output=True, disp=False)
        if x_maxmom_info.converged and (0 <= x_maxmom) and (x_maxmom <= L):
            print(
                f"{' '*6}{mu(x_maxmom, wl, wr, L)[0]:.7f} "
                f"@ x = {x_maxmom:.7f}",
                sep="\t"
            )

    print(f"{' '*3}Local extrema of y(x)")
    for x0 in np.linspace(0, L, num=5, endpoint=True):
        x_maxdef, x_maxdef_info = spo.newton(g, x0, fprime=dg, tol=eps, maxiter=Kmax, full_output=True, disp=False)
        if x_maxdef_info.converged and (0 <= x_maxdef) and (x_maxdef <= L):
            print(
                f"{' '*6}{mu(x_maxdef, wl, wr, L)[0]:.7f} "
                f"@ x = {x_maxdef:.7f}",
                sep="\t"
            )
