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
    c0 = Ay(wL, wR, L)
    c1 = -wL
    c2 = (wL + wR) / (2 * L)
    return npp.Polynomial([c0, c1, c2])

def get_mu(wL, wR, L):
    c0 = 0.0
    c1 = Ay(wL, wR, L)
    c2 = -wL / 2
    c3 = (wL + wR) / (6 * L)
    return npp.Polynomial([c0, c1, c2, c3])

def get_m(wL, wR, L):
    C1 = -(L**3) * (8 * wL - 7 * wR) / 360
    c0 = C1
    c1 = 0.0
    c2 = Ay(wL, wR, L) / 2
    c3 = -wL / 6
    c4 = (wL + wR) / (24 * L)
    return npp.Polynomial([c0, c1, c2, c3, c4])

def get_y(wL, wR, L):
    C1 = -(L**3) * (8 * wL - 7 * wR) / 360
    c0 = 0.0
    c1 = C1
    c2 = 0.0
    c3 = Ay(wL, wR, L) / 6
    c4 = -wL / 24
    c5 = (wL + wR) / (120 * L)
    return npp.Polynomial([c0, c1, c2, c3, c4, c5])


if __name__ == "__main__":
    pass
