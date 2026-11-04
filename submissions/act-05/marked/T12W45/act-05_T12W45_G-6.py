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
    coeffs = [
        Ay(wL, wR, L),
        -wL,
        (wL + wR) / (2.0 * L),
    ]
    return npp.Polynomial(coeffs)


def get_mu(wL, wR, L):
    coeffs = [
        0.0,
        Ay(wL, wR, L),
        -wL / 2.0,
        (wL + wR) / (6.0 * L),
    ]
    return npp.Polynomial(coeffs)


def get_m(wL, wR, L):
    coeffs = [
        (7.0 * wR - 8.0 * wL) * L * L * L / 360.0,
        0.0,
        Ay(wL, wR, L) / 2.0,
        -wL / 6.0,
        (wL + wR) / (24.0 * L),
    ]
    return npp.Polynomial(coeffs)


def get_y(wL, wR, L):
    coeffs = [
        0.0,
        (7.0 * wR - 8.0 * wL) * L * L * L / 360.0,
        0.0,
        Ay(wL, wR, L) / 6.0,
        -wL / 24.0,
        (wL + wR) / (120.0 * L),
    ]
    return npp.Polynomial(coeffs)


if __name__ == "__main__":
    pass
