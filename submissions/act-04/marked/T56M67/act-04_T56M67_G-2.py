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
    """Computes the support reaction Ay at x = 0."""
    return (-1.0/3.0 * wL + 1.0/6.0 * wR) * L


def By(wL, wR, L):
    """Computes the support reaction By at x = L."""
    return (1.0/3.0 * wR - 1.0/6.0 * wL) * L


def polyvalder(coeffs, s):
    """
    Evaluates the value and derivative of a polynomial given its coefficients.
    Coefficients are expected in the order: a_0, a_1, ..., a_n.
    """
    val = 0.0
    der = 0.0
    s_pow = 1.0
    s_pow_der = 0.0
    
    for i in range(len(coeffs)):
        val += coeffs[i] * s_pow
        if i > 0:
            der += coeffs[i] * i * s_pow_der
            
        s_pow_der = s_pow
        s_pow *= s
        
    return np.array([val, der])


def nu(x, wL, wR, L):
    """Computes the internal shear and its derivative at location x."""
    ay = Ay(wL, wR, L)
    # Coefficients for nu(x) = Ay + wL*x - ((wL + wR)/(2*L))*x^2
    coeffs = [ay, wL, -(wL + wR) / (2.0 * L)]
    return polyvalder(coeffs, x)


def mu(x, wL, wR, L):
    """Computes the bending moment and its derivative at location x."""
    ay = Ay(wL, wR, L)
    # Coefficients for mu(x) = 0 + Ay*x + (wL/2)*x^2 - ((wL + wR)/(6*L))*x^3
    coeffs = [0.0, ay, wL / 2.0, -(wL + wR) / (6.0 * L)]
    return polyvalder(coeffs, x)


def m(x, wL, wR, L):
    """Computes the slope and its derivative at location x."""
    ay = Ay(wL, wR, L)
    # Integration constant C1 obtained from boundary condition y(L) = 0
    c1 = (1.0/45.0) * wL * (L * L * L) - (7.0/360.0) * wR * (L * L * L)
    # Coefficients for m(x) = C1 + 0*x + (Ay/2)*x^2 + (wL/6)*x^3 - ((wL + wR)/(24*L))*x^4
    coeffs = [c1, 0.0, ay / 2.0, wL / 6.0, -(wL + wR) / (24.0 * L)]
    return polyvalder(coeffs, x)


def y(x, wL, wR, L):
    """Computes the deflection and its derivative at location x."""
    ay = Ay(wL, wR, L)
    c1 = (1.0/45.0) * wL * (L * L * L) - (7.0/360.0) * wR * (L * L * L)
    # Coefficients for y(x) = 0 + C1*x + 0*x^2 + (Ay/6)*x^3 + (wL/24)*x^4 - ((wL + wR)/(120*L))*x^5
    coeffs = [0.0, c1, 0.0, ay / 6.0, wL / 24.0, -(wL + wR) / (120.0 * L)]
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
