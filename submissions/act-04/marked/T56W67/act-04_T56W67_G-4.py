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
    return (L / 6.0) * (wR - 2.0 * wL)

def By(wL, wR, L):
    return (L / 6.0) * (2.0 * wR - wL)

def polyvalder(coeffs, s):
    val = 0.0
    der = 0.0
    s_pow = 1.0       
    s_pow_der = 1.0   
    
    for i, a in enumerate(coeffs):
        val += a * s_pow
        if i > 0:
            der += i * a * s_pow_der
            s_pow_der = s_pow_der * s
            
        s_pow = s_pow * s
        
    return np.array([val, der])

def nu(x, wL, wR, L):
    c = [Ay(wL, wR, L), wL, -(wL + wR) / (2.0 * L)]
    return polyvalder(c, x)

def mu(x, wL, wR, L):
    c = [0.0, Ay(wL, wR, L), wL / 2.0, -(wL + wR) / (6.0 * L)]
    return polyvalder(c, x)

def m(x, wL, wR, L):
    C1 = (L * L * L) * (wL / 45.0 - 7.0 * wR / 360.0)
    c = [C1, 0.0, Ay(wL, wR, L) / 2.0, wL / 6.0, -(wL + wR) / (24.0 * L)]
    return polyvalder(c, x)

def y(x, wL, wR, L):
    C1 = (L * L * L) * (wL / 45.0 - 7.0 * wR / 360.0)
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
