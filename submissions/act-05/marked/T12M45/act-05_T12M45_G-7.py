"""
CVE154 (A.Y. 2026-2027, S1)
Template script for Programming Activity No. 05

Prepared by Christian Cahig

This file belongs to the repository
https://github.com/christian-cahig/CVE154_AY-2026-2027-S1.
"""

import numpy as np
from numpy import polynomial as npp

__AUTHOR__ = "Group 7"

def Ay(wl, wr, L):
    return L * (2 * wl - wr) / 6


def By(wl, wr, L):
    return L * (wl - 2 * wr) / 6


def get_nu(wl, wr, L):
    return npp.Polynomial([Ay(wl, wr, L), -wl, (wl + wr) / (2 * L),])


def get_mu(wl, wr, L):
    return get_nu(wl, wr, L).integ()


def get_m(wl, wr, L):
    slope = get_mu(wl, wr, L).integ()
    provisional_y = slope.integ()
    slope.coef[0] = -provisional_y(L) / L

    return slope

def get_y(wl, wr, L):
    return get_m(wl, wr, L).integ()


if __name__ == "__main__":
    pass
