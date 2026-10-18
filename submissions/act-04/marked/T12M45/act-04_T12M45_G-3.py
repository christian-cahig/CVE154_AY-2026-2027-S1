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

__AUTHOR__ = "Group 3"

def Ay(w_L, w_R, L):
    return ((w_R - 2.0 * w_L) / 6.0) * L

def By(w_L, w_R, L):
    return ((2.0 * w_R - w_L) / 6.0) * L

def polyvalder(coeffs, s):
    val = 0.0
    der = 0.0
    curr_s_val = 1.0
    curr_s_der = 1.0
    
    for i in range(len(coeffs)):
        val += coeffs[i] * curr_s_val
        if i > 0:
            der += coeffs[i] * i * curr_s_der
            curr_s_der = curr_s_der * s
        curr_s_val = curr_s_val * s
        
    return np.array([val, der])

def nu(x, w_L, w_R, L):
    coeffs = [
        ((w_R - 2.0 * w_L) / 6.0) * L,
        w_L,
        -(w_L + w_R) / (2.0 * L)
    ]
    return polyvalder(coeffs, x)

def mu(x, w_L, w_R, L):
    coeffs = [
        0.0,
        ((w_R - 2.0 * w_L) / 6.0) * L,
        w_L / 2.0,
        -(w_L + w_R) / (6.0 * L)
    ]
    return polyvalder(coeffs, x)

def m(x, w_L, w_R, L):
    coeffs = [
        ((8.0 * w_L - 7.0 * w_R) / 360.0) * (L * L * L),
        0.0,
        ((w_R - 2.0 * w_L) / 12.0) * L,
        w_L / 6.0,
        -(w_L + w_R) / (24.0 * L)
    ]
    return polyvalder(coeffs, x)

def y(x, w_L, w_R, L):
    coeffs = [
        0.0,
        ((8.0 * w_L - 7.0 * w_R) / 360.0) * (L * L * L),
        0.0,
        ((w_R - 2.0 * w_L) / 36.0) * L,
        w_L / 24.0,
        -(w_L + w_R) / (120.0 * L)
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
    