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
    return (L / 6) * (2 * wL - wR)

def By(wL, wR, L):
    return (L / 6) * (wL - 2 * wR)

def get_nu(wL, wR, L):
    c0 = (L / 6) * (2 * wL - wR)
    c1 = -wL
    c2 = (wL + wR) / (2 * L)
    return npp.Polynomial([c0, c1, c2])

def get_mu(wL, wR, L):
    c0 = 0.0
    c1 = (L / 6) * (2 * wL - wR)
    c2 = -wL / 2.0
    c3 = (wL + wR) / (6 * L)
    return npp.Polynomial([c0, c1, c2, c3])

def get_m(wL, wR, L):
    c0 = -(L**3 / 360) * (8 * wL - 7 * wR)
    c1 = 0.0
    c2 = (L / 12) * (2 * wL - wR)
    c3 = -wL / 6.0
    c4 = (wL + wR) / (24 * L)
    return npp.Polynomial([c0, c1, c2, c3, c4])

def get_y(wL, wR, L):
    c0 = 0.0
    c1 = -(L**3 / 360) * (8 * wL - 7 * wR)
    c2 = 0.0
    c3 = (L / 36) * (2 * wL - wR)
    c4 = -wL / 24.0
    c5 = (wL + wR) / (120 * L)
    return npp.Polynomial([c0, c1, c2, c3, c4, c5])
    
if __name__ == "__main__":
    pass
