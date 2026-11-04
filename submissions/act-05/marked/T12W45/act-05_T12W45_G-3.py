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


def Ay(wL, wR, L):
    return L * (2 * wL - wR) / 6


def By(wL, wR, L):
    return L * (wL - 2 * wR) / 6


def get_nu(wL, wR, L):
    return npp.Polynomial([Ay(wL, wR, L), -wL, (wL + wR) / (2 * L)])


def get_mu(wL, wR, L):
    return get_nu(wL, wR, L).integ(k=0)


def get_m(wL, wR, L):
    C1 = L * L * L * (7 * wR - 8 * wL) / 360
    return get_mu(wL, wR, L).integ(k=C1)


def get_y(wL, wR, L):
    return get_m(wL, wR, L).integ(k=0)


if __name__ == "__main__":
    pass
