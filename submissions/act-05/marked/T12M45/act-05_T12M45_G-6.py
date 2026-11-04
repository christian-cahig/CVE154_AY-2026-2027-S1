"""
CVE154 (A.Y. 2026-2027, S1)
Template script for Programming Activity No. 05

Prepared by Christian Cahig

This file belongs to the repository
https://github.com/christian-cahig/CVE154_AY-2026-2027-S1.
"""

import numpy as np
import numpy.polynomial as npp

__AUTHOR__ = "Group 6"

def Ay(wL, wR, L):
    return (2.0 * wL - wR) * L / 6.0

def By(wL, wR, L):
    return (wL - 2.0 * wR) * L / 6.0

def get_nu(wL, wR, L):
    a0 = (2.0 * wL - wR) * L / 6.0
    a1 = -wL
    a2 = (wL + wR) / (2.0 * L)
    return npp.Polynomial([a0, a1, a2])

def get_mu(wL, wR, L):
    a0 = 0.0
    a1 = (2.0 * wL - wR) * L / 6.0
    a2 = -wL / 2.0
    a3 = (wL + wR) / (6.0 * L)
    return npp.Polynomial([a0, a1, a2, a3])

def get_m(wL, wR, L):
    a0 = (7.0 * wR - 8.0 * wL) * (L**3.0) / 360.0
    a1 = 0.0
    a2 = ((2.0 * wL - wR) * L / 6.0) / 2.0
    a3 = -wL / 6.0
    a4 = (wL + wR) / (24.0 * L)
    return npp.Polynomial([a0, a1, a2, a3, a4])

def get_y(wL, wR, L):
    a0 = 0.0
    a1 = (7.0 * wR - 8.0 * wL) * (L**3.0) / 360.0
    a2 = 0.0
    a3 = ((2.0 * wL - wR) * L / 6.0) / 6.0
    a4 = -wL / 24.0
    a5 = (wL + wR) / (120.0 * L)
    return npp.Polynomial([a0, a1, a2, a3, a4, a5])

if __name__ == "__main__":
    pass
