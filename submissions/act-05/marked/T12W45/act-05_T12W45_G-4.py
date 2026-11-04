"""
CVE154 (A.Y. 2026-2027, S1)
Template script for Programming Activity No. 05

Prepared by Christian Cahig

This file belongs to the repository
https://github.com/christian-cahig/CVE154_AY-2026-2027-S1.
"""

import numpy as np
import numpy.polynomial as npp


__AUTHOR__ = "Group 4"

def Ay(wL, wR, L):
    return (2 * wL - wR) * L / 6

def By(wL, wR, L):
    return (wL - 2 * wR) * L / 6

def get_nu(wL, wR, L):
    coefficients = [Ay(wL, wR, L),-wL,(wL + wR) / (2 * L),]

    return npp.Polynomial(coefficients)

def get_mu(wL, wR, L):
    return get_nu(wL, wR, L).integ()

def get_m(wL, wR, L):
    initial_slope = (7 * wR - 8 * wL) * L ** 3 / 360

    return npp.Polynomial([initial_slope]) + get_mu(wL, wR, L).integ()

def get_y(wL, wR, L):
    return get_m(wL, wR, L).integ()

if __name__ == "__main__":
    pass
