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

__AUTHOR__ = "Group 1"

def Ay(wL, wR, L):
    return L * (wR - 2 * wL) / 6.0

def By(wL, wR, L):
    return L * (2 * wR - wL) / 6.0

def polyvalder(coeffs, s):
    val = 0.0
    der = 0.0
    s_pow_val = 1.0   
    s_pow_der = 1.0   
    
    for i in range(len(coeffs)):
        val = val + coeffs[i] * s_pow_val
        s_pow_val = s_pow_val * s
        
        if i > 0:
            der = der + coeffs[i] * i * s_pow_der
            s_pow_der = s_pow_der * s
            
    return np.array([val, der])

def nu(x, wL, wR, L):
    ay = Ay(wL, wR, L)
    coeffs = [ay, wL, -(wL + wR) / (2.0 * L)]
    return polyvalder(coeffs, x)

def mu(x, wL, wR, L):
    ay = Ay(wL, wR, L)
    coeffs = [0.0, ay, wL / 2.0, -(wL + wR) / (6.0 * L)]
    return polyvalder(coeffs, x)

def m(x, wL, wR, L):
    ay = Ay(wL, wR, L)
    c3 = (8.0 * wL - 7.0 * wR) * (L * L * L) / 360.0
    coeffs = [c3, 0.0, ay / 2.0, wL / 6.0, -(wL + wR) / (24.0 * L)]
    return polyvalder(coeffs, x)

def y(x, wL, wR, L):
    ay = Ay(wL, wR, L)
    c3 = (8.0 * wL - 7.0 * wR) * (L * L * L) / 360.0
    coeffs = [0.0, c3, 0.0, ay / 6.0, wL / 24.0, -(wL + wR) / (120.0 * L)]
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
