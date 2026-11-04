"""
CVE154 (A.Y. 2026-2027, S1)
Template script for Programming Activity No. 05

Prepared by Christian Cahig

This file belongs to the repository
https://github.com/christian-cahig/CVE154_AY-2026-2027-S1.
"""

import numpy as np
import numpy.polynomial as npp

__AUTHOR__ = "Group 5"  

def Ay(wL, wR, L):
    return L * (2 * wL - wR) / 6.0


def By(wL, wR, L):
    return L * (wL - 2 * wR) / 6.0


def get_nu(wL, wR, L):
    ay = Ay(wL, wR, L)
    c0 = ay
    c1 = -wL
    c2 = (wL + wR) / (2.0 * L)
    return npp.Polynomial([c0, c1, c2])


def get_mu(wL, wR, L):
    ay = Ay(wL, wR, L)
    c0 = 0.0
    c1 = ay
    c2 = -wL / 2.0
    c3 = (wL + wR) / (6.0 * L)
    return npp.Polynomial([c0, c1, c2, c3])


def get_m(wL, wR, L):
    ay = Ay(wL, wR, L)
    c0 = - (L**3) * (7.0 * wL - 3.0 * wR) / 360.0
    c1 = 0.0
    c2 = ay / 2.0
    c3 = -wL / 6.0
    c4 = (wL + wR) / (24.0 * L)
    return npp.Polynomial([c0, c1, c2, c3, c4])


def get_y(wL, wR, L):
    ay = Ay(wL, wR, L)
    c0 = 0.0
    c1 = - (L**3) * (7.0 * wL - 3.0 * wR) / 360.0
    c2 = 0.0
    c3 = ay / 6.0
    c4 = -wL / 24.0
    c5 = (wL + wR) / (120.0 * L)
    return npp.Polynomial([c0, c1, c2, c3, c5])

    nu = get_nu(wl, wr, L)
    mu = get_mu(wl, wr, L)
    m = get_m(wl, wr, L)
    y = get_y(wl, wr, L)

if __name__ == "__main__":
    pass
