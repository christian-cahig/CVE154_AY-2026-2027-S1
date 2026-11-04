"""
CVE154 (A.Y. 2026-2027, S1)
Template script for Programming Activity No. 05

Prepared by Christian Cahig

This file belongs to the repository
https://github.com/christian-cahig/CVE154_AY-2026-2027-S1.
"""

import numpy as np
import numpy.polynomial as npp

__AUTHOR__ = "Group 2"

def Ay(wl, wr, L):
    return L * (2 * wl - wr) / 6

def By(wl, wr, L):
    return L * (wl - 2 * wr) / 6

def get_nu(wl, wr, L):
    return npp.Polynomial([Ay(wl, wr, L), -wl, (wl + wr) / (2 * L)])

def get_mu(wl, wr, L):
    return npp.Polynomial([0, Ay(wl, wr, L), -wl / 2, (wl + wr) / (6 * L)])

def get_m(wl, wr, L):
    C = -L**3 * (8 * wl - 7 * wr) / 360
    return npp.Polynomial(
        [C, 0, Ay(wl, wr, L) / 2, -wl / 6, (wl + wr) / (24 * L)]
    )

def get_y(wl, wr, L):
    C = -L**3 * (8 * wl - 7 * wr) / 360
    return npp.Polynomial(
        [0, C, 0, Ay(wl, wr, L) / 6, -wl / 24, (wl + wr) / (120 * L)]
    )

if __name__ == "__main__":  
    pass
