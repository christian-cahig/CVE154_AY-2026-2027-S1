"""
CVE154 (A.Y. 2026-2027, S1)
Programming Activity No. 05: Weird flex but ok
"""

import numpy as np
import numpy.polynomial as npp

__AUTHOR__ = "Group 1" 


def Ay(wL, wR, L):
    return (L / 6.0) * (2.0 * wL - wR)


def By(wL, wR, L):
    return (L / 6.0) * (wL - 2.0 * wR)


def get_nu(wL, wR, L):
    f = npp.Polynomial([-wL, (wR + wL) / L])
    return f.integ(k=Ay(wL, wR, L))


def get_mu(wL, wR, L):
    nu = get_nu(wL, wR, L)
    return nu.integ(k=0.0)


def get_m(wL, wR, L):
    mu = get_mu(wL, wR, L)
    C1 = (L**3 / 360.0) * (7.0 * wR - 8.0 * wL)
    return mu.integ(k=C1)


def get_y(wL, wR, L):
    m = get_m(wL, wR, L)
    return m.integ(k=0.0)


if __name__ == "__main__":
    pass
