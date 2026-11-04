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

def Ay(w_L, w_R, L):
    return L * (2.0 * w_L - w_R) / 6.0

def By(w_L, w_R, L):
    return L * (w_L - 2.0 * w_R) / 6.0

def get_nu(w_L, w_R, L):
    coeffs = [Ay(w_L, w_R, L), -w_L, (w_L + w_R) / (2.0 * L)]
    return npp.Polynomial(coeffs)

def get_mu(w_L, w_R, L):
    coeffs = [0.0, Ay(w_L, w_R, L), -w_L / 2.0, (w_L + w_R) / (6.0 * L)]
    return npp.Polynomial(coeffs)

def get_m(w_L, w_R, L):
    C3 = ((7.0 * w_R - 8.0 * w_L) / 360.0) * (L ** 3)
    coeffs = [C3, 0.0, Ay(w_L, w_R, L) / 2.0, -w_L / 6.0, (w_L + w_R) / (24.0 * L)]
    return npp.Polynomial(coeffs)

def get_y(w_L, w_R, L):
    C3 = ((7.0 * w_R - 8.0 * w_L) / 360.0) * (L ** 3)
    coeffs = [0.0, C3, 0.0, Ay(w_L, w_R, L) / 6.0, -w_L / 24.0, (w_L + w_R) / (120.0 * L)]
    return npp.Polynomial(coeffs)


if __name__ == "__main__":
    pass
