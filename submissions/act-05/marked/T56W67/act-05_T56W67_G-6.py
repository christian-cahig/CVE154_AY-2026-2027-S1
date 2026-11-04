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
    return (L / 6.0) * (2.0 * wL - wR)

def By(wL, wR, L):
    return (L / 6.0) * (wL - 2.0 * wR)

def get_nu(wL, wR, L):
    c0 = Ay(wL, wR, L)
    c1 = -wL
    c2 = (wL + wR) / (2.0 * L)
    return npp.Polynomial([c0, c1, c2])

def get_mu(wL, wR, L):
    nu = get_nu(wL, wR, L)
    return nu.integ(1, k=[0.0])

def get_m(wL, wR, L):
    mu = get_mu(wL, wR, L)
    m0 = (L**3 / 360.0) * (7.0 * wR - 8.0 * wL)
    return mu.integ(1, k=[m0])

def get_y(wL, wR, L):
    m = get_m(wL, wR, L)
    return m.integ(1, k=[0.0])
    
if __name__ == "__main__":
    pass
