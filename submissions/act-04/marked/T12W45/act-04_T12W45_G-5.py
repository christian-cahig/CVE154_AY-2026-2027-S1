import math as mt
import scipy.optimize as spo
import numpy as np

__AUTHOR__ = "Group N"


def Ay(wL, wR, L):
    return ((wR - 2 * wL) / 6) * L


def By(wL, wR, L):
    return ((2 * wR - wL) / 6) * L


def polyvalder(coefficients, s):
    """Return a NumPy array [polynomial value, derivative]."""
    value = 0
    derivative = 0

    for coefficient in reversed(coefficients):
        derivative = derivative * s + value
        value = value * s + coefficient

    return np.array([value, derivative])


def nu(x, wL, wR, L):
    """Return [shear V(x), shear derivative V'(x)]."""
    coefficients = [
        Ay(wL, wR, L),
        wL,
        -(wL + wR) / (2 * L),
    ]
    return polyvalder(coefficients, x)


def mu(x, wL, wR, L):
    """Return [moment M(x), moment derivative M'(x)]."""
    coefficients = [
        0,
        Ay(wL, wR, L),
        wL / 2,
        -(wL + wR) / (6 * L),
    ]
    return polyvalder(coefficients, x)


def m(x, wL, wR, L):
    """Return [slope y'(x), slope derivative y''(x)]."""
    C1 = (L * L * L) * (8 * wL - 7 * wR) / 360

    coefficients = [
        C1,
        0,
        Ay(wL, wR, L) / 2,
        wL / 6,
        -(wL + wR) / (24 * L),
    ]
    return polyvalder(coefficients, x)


def y(x, wL, wR, L):
    """Return [deflection y(x), deflection derivative y'(x)]."""
    C1 = (L * L * L) * (8 * wL - 7 * wR) / 360

    coefficients = [
        0,
        C1,
        0,
        Ay(wL, wR, L) / 6,
        wL / 24,
        -(wL + wR) / (120 * L),
    ]
    return polyvalder(coefficients, x)


wl, wr, L = 1, 7, 1
print(f"wL = {wl} N/m; wR = {wr} N/m; L = {L} m")
print(
    f"{' '*3}Ay: {Ay(wl, wr, L):.7f}",
    f"By: {By(wl, wr, L):.7f}",
    sep="\t"
)
for x in np.linspace(0, L, num=5, endpoint=True):
    print(f"{' '*3}@ x = {x} m")
    for fun in [nu, mu, m, y]:
        v, dv = fun(x, wl, wr, L)
        print(
            f"{' '*6}{fun.__name__}: {v:.7f}",
            f"{fun.__name__+"'"}: {dv:.7f}",
            sep="\t"
        )
