"""
CVE154 (A.Y. 2026-2027, S1)
Template script for Programming Activity No. 05

Prepared by Christian Cahig

This file belongs to the repository
https://github.com/christian-cahig/CVE154_AY-2026-2027-S1.
"""

import numpy as np
import numpy.polynomial as npp

_AUTHOR_ = "Group 2"

def Ay(wl, wr, L):
    return L * (2 * wl - wr) / 6


def By(wl, wr, L):
    return L * (wl - 2 * wr) / 6


def get_nu(wl, wr, L):
    f = npp.Polynomial([-wl, (wl + wr) / L])
    return f.integ(m=1, k=[Ay(wl, wr, L)])


def get_mu(wl, wr, L):
    return get_nu(wl, wr, L).integ(m=1, k=[0])


def get_m(wl, wr, L):
    return get_y(wl, wr, L).deriv(m=1)


def get_y(wl, wr, L):
    y_base = get_mu(wl, wr, L).integ(m=2, k=[0, 0])
    A = np.array([
        [0, 1],
        [L, 1]
    ])
    b = np.array([-y_base(0), -y_base(L)])
    m0, y0 = np.linalg.solve(A, b)
    return y_base + npp.Polynomial([y0, m0])

if __name__ == "__main__":
    pass
