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
    """Vertical reaction at the left hinge A."""
    return L * (2.0 * wL - wR) / 6.0


def By(wL, wR, L):
    """Vertical reaction at the right hinge B."""
    return L * (wL - 2.0 * wR) / 6.0


def get_nu(wL, wR, L):
    """Internal shear nu(x) as a Polynomial."""
    return npp.Polynomial([Ay(wL, wR, L), -wL, (wL + wR) / (2.0 * L)])


def get_mu(wL, wR, L):
    """Bending moment mu(x) as a Polynomial."""
    return npp.Polynomial([0.0, Ay(wL, wR, L), -wL / 2.0, (wL + wR) / (6.0 * L)])


def get_m(wL, wR, L):
    """Slope m(x) as a Polynomial."""
    c1 = L * L * L * (7.0 * wR - 8.0 * wL) / 360.0
    return npp.Polynomial(
        [c1, 0.0, Ay(wL, wR, L) / 2.0, -wL / 6.0, (wL + wR) / (24.0 * L)]
    )


def get_y(wL, wR, L):
    """Deflection y(x) as a Polynomial."""
    c1 = L * L * L * (7.0 * wR - 8.0 * wL) / 360.0
    return npp.Polynomial(
        [0.0, c1, 0.0, Ay(wL, wR, L) / 6.0, -wL / 24.0, (wL + wR) / (120.0 * L)]
    )


if __name__ == "__main__":
    pass
