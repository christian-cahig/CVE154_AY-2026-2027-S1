"""
CVE154 (A.Y. 2026-2027, S1)
Template script for Programming Activity No. 05

Prepared by Christian Cahig

This file belongs to the repository
https://github.com/christian-cahig/CVE154_AY-2026-2027-S1.
"""

# =====================================================================
# Part 0. Formulations (summary)
# ---------------------------------------------------------------------
# Beam A-B, length L, hinged at both ends, x measured from A.
# Load: DOWNWARD intensity w_L at x = 0, UPWARD intensity w_R at x = L.
# Same sign convention as before: +y is upward, so the load f(x) and the
# deflection y(x) are positive upward, and (with EI = 1)
#       nu' = f,   mu' = nu,   m' = mu,   y' = m
#     f(x) = -w_L + k x,   k = (w_L + w_R) / L
#     A_y = L (2 w_L - w_R) / 6        B_y = L (w_L - 2 w_R) / 6
#     nu(x) = A_y - w_L x + k x^2 / 2
#     mu(x) = A_y x - w_L x^2 / 2 + k x^3 / 6
#      m(x) = C3 + A_y x^2 / 2 - w_L x^3 / 6 + k x^4 / 24
#      y(x) = C3 x + A_y x^3 / 6 - w_L x^4 / 24 + k x^5 / 120
#     C3 = L^3 (7 w_R - 8 w_L) / 360    (from y(0) = y(L) = 0)
# =====================================================================

# =====================================================================
# Part 1. Core
# =====================================================================

import numpy as np
import numpy.polynomial as npp

__AUTHOR__ = "Group 5"


def Ay(wL, wR, L):
    return L * (2.0 * wL - wR) / 6.0


def By(wL, wR, L):
    return L * (wL - 2.0 * wR) / 6.0


def get_nu(wL, wR, L):
    k = (wL + wR) / L
    A = L * (2.0 * wL - wR) / 6.0
    return npp.Polynomial([A, -wL, k / 2.0])


def get_mu(wL, wR, L):
    k = (wL + wR) / L
    A = L * (2.0 * wL - wR) / 6.0
    return npp.Polynomial([0.0, A, -wL / 2.0, k / 6.0])


def get_m(wL, wR, L):
    k = (wL + wR) / L
    A = L * (2.0 * wL - wR) / 6.0
    C3 = L * L * L * (7.0 * wR - 8.0 * wL) / 360.0
    return npp.Polynomial([C3, 0.0, A / 2.0, -wL / 6.0, k / 24.0])


def get_y(wL, wR, L):
    k = (wL + wR) / L
    A = L * (2.0 * wL - wR) / 6.0
    C3 = L * L * L * (7.0 * wR - 8.0 * wL) / 360.0
    return npp.Polynomial([0.0, C3, 0.0, A / 6.0, -wL / 24.0, k / 120.0])


# =====================================================================
# Part 2. Synthesis
# =====================================================================

if __name__ == "__main__":
    pass
