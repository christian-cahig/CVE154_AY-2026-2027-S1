"""
CVE154 (A.Y. 2026-2027, S1)
Template script for Programming Activity No. 05

Prepared by Christian Cahig

This file belongs to the repository
https://github.com/christian-cahig/CVE154_AY-2026-2027-S1.
"""
import numpy as np
import numpy.polynomial as npp

__AUTHOR__ = "Group 1"

def Ay(wL, wR, L):
    return L * (2 * wL - wR) / 6

def By(wL, wR, L):
    return L * (wL - 2 * wR) / 6

def get_nu(wL, wR, L):
    ay = Ay(wL, wR, L)
    coefficients = [ay, -wL, (wL + wR) / (2 * L)]

    return npp.Polynomial(coefficients)

def get_mu(wL, wR, L):
    ay = Ay(wL, wR, L)
    coefficients = [0, ay, -wL / 2, (wL + wR) / (6 * L)]

    return npp.Polynomial(coefficients)

def get_m(wL, wR, L):
    ay = Ay(wL, wR, L)
    C2 = (-ay * L**2 / 6 + wL * L**3 / 24 - (wL + wR) * L**3 / 120)
    coefficients = [C2, 0, ay / 2, -wL / 6, (wL + wR) / (24 * L)]

    return npp.Polynomial(coefficients)

def get_y(wL, wR, L):
    ay = Ay(wL, wR, L)
    C2 = (-ay * L**2 / 6 + wL * L**3 / 24 - (wL + wR) * L**3 / 120)
    coefficients = [0, C2, 0, ay / 6, -wL / 24, (wL + wR) / (120 * L)]

    return npp.Polynomial(coefficients)

if __name__ == "__main__":
    pass
