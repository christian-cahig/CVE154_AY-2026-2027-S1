"""
CVE154 (A.Y. 2026-2027, S1)
Template script for Programming Activity No. 05

Prepared by Christian Cahig

This file belongs to the repository
https://github.com/christian-cahig/CVE154_AY-2026-2027-S1.
"""

import numpy as np
import numpy.polynomial as npp

__AUTHOR__ = "Group 3"


def Ay(wl, wr, L):
    return (2.0 * wl - wr) * L / 6.0

def By(wl, wr, L):
    return (2.0 * wr - wl) * L / 6.0

def get_nu(wl, wr, L):
    ay = Ay(wl, wr, L)
    coeffs = [ay, -wl, (wl + wr) / (2.0 * L)]
    return npp.Polynomial(coeffs)


def get_mu(wl, wr, L):
    ay = Ay(wl, wr, L)
    coeffs = [0.0, ay, -wl / 2.0, (wl + wr) / (6.0 * L)]
    return npp.Polynomial(coeffs)


def get_m(wl, wr, L):
    ay = Ay(wl, wr, L)
    C1 = (7.0 * wr - 8.0 * wl) * (L * L * L) / 360.0
    coeffs = [C1, 0.0, ay / 2.0, -wl / 6.0, (wl + wr) / (24.0 * L)]
    return npp.Polynomial(coeffs)



if __name__ == "__main__":
    pass
