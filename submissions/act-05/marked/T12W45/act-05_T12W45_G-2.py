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


def Ay(wL, wR, L):
    return L * (2*wL - wR) / 6


def By(wL, wR, L):
    return L * (wL - 2*wR) / 6


def get_nu(wL, wR, L):
    load = npp.Polynomial([wL, -(wL + wR)/L])
    return Ay(wL, wR, L) - load.integ()


def get_mu(wL, wR, L):
    return get_nu(wL, wR, L).integ()


def get_m(wL, wR, L):
    mu = get_mu(wL, wR, L)

    base_m = -mu.integ()
    base_y = base_m.integ()

    C = -base_y(L) / L

    return base_m + C


def get_y(wL, wR, L):
    return get_m(wL, wR, L).integ()

if __name__ == "__main__":
    pass
