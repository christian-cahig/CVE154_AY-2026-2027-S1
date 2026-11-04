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

# -----------------------------------------------------------------------------
# Formulation (unit flexural rigidity: EI = 1, i.e. 1 N*m^2, so that units stay
# homogeneous: x, L, y in m; wL, wR in N/m; Ay, By, nu in N; mu in N*m; m in rad)
#
# Sign convention implied by  EI d4y/dx4 = f(x):
#   x runs from A (x = 0) to B (x = L); load intensity f, deflection y, slope m,
#   shear nu and the reactions Ay, By are positive upward; mu is positive when
#   it makes the beam sag (EI y'' = mu).
#
#   f(x)  = -wL + (wL + wR) * x / L           (wL downward at A, wR upward at B)
#   Ay    = L * (2*wL - wR) / 6               (from sum Fy = 0 and sum M_A = 0)
#   By    = L * (wL - 2*wR) / 6
#   nu(x) = Ay + (integral of f from 0 to x)  (EI y''' = nu)
#   mu(x) = integral of nu from 0 to x        (hinge at A: mu(0) = 0)
#   m(x)  = (integral of mu) + C1             (m = y')
#   y(x)  = integral of m, with y(0) = 0 and C1 fixed by y(L) = 0
# -----------------------------------------------------------------------------


def Ay(w_left, w_right, length):
    """Vertical reaction at hinge A (upward positive)."""
    return length * (2 * w_left - w_right) / 6


def By(w_left, w_right, length):
    """Vertical reaction at hinge B (upward positive)."""
    return length * (w_left - 2 * w_right) / 6


def get_nu(w_left, w_right, length):
    """Internal shear nu(x) as a Polynomial."""
    # nu(x) = Ay - wL * x + (wL + wR) / (2 L) * x^2
    return npp.Polynomial([
        Ay(w_left, w_right, length),
        -w_left,
        (w_left + w_right) / (2 * length),
    ])


def get_mu(w_left, w_right, length):
    """Bending moment mu(x) as a Polynomial."""
    # mu(0) = 0 because A is a hinge, so the integration constant is zero.
    return get_nu(w_left, w_right, length).integ()


def get_m(w_left, w_right, length):
    """Slope m(x) = dy/dx as a Polynomial (EI = 1)."""
    moment = get_mu(w_left, w_right, length)
    # y(x) = (double integral of mu) + C1 * x, and y(L) = 0 gives C1.
    c1 = -moment.integ(2)(length) / length
    return moment.integ(k=[c1])


def get_y(w_left, w_right, length):
    """Deflection y(x) (elastic curve) as a Polynomial (EI = 1)."""
    # y(0) = 0 because A is a hinge, so the integration constant is zero.
    return get_m(w_left, w_right, length).integ()

if __name__ == "__main__":
    pass
