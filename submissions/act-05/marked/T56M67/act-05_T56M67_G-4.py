import numpy as np
import numpy.polynomial as npp

__AUTHOR__ = "Group 4"


def Ay(wl, wr, L):
    # Statics: Sum of moments about B = 0
    return (L / 6.0) * (2.0 * wl + wr)


def By(wl, wr, L):
    # Statics: Sum of moments about A = 0
    return (L / 6.0) * (wl + 2.0 * wr)


def get_nu(wl, wr, L):
    ay = Ay(wl, wr, L)
    
    # Polynomial terms: c0 + c1*x + c2*x^2
    c0 = ay
    c1 = -wl
    c2 = -(wr - wl) / (2.0 * L)
    
    return npp.Polynomial([c0, c1, c2])


def get_mu(wl, wr, L):
    ay = Ay(wl, wr, L)
    
    # Integrating shear force V(x)
    c0 = 0.0
    c1 = ay
    c2 = -wl / 2.0
    c3 = -(wr - wl) / (6.0 * L)
    
    return npp.Polynomial([c0, c1, c2, c3])


def get_m(wl, wr, L):
    ay = Ay(wl, wr, L)
    
    # Integration constant C1 from BC y(L) = 0
    c1_const = -(L**3 / 360.0) * (8.0 * wl + 7.0 * wr)
    
    c0 = c1_const
    c1 = 0.0
    c2 = ay / 2.0
    c3 = -wl / 6.0
    c4 = -(wr - wl) / (24.0 * L)
    
    return npp.Polynomial([c0, c1, c2, c3, c4])


def get_y(wl, wr, L):
    ay = Ay(wl, wr, L)
    c1_const = -(L**3 / 360.0) * (8.0 * wl + 7.0 * wr)
    
    # Integrating slope m(x) with BC y(0) = 0
    c0 = 0.0
    c1 = c1_const
    c2 = 0.0
    c3 = ay / 6.0
    c4 = -wl / 24.0
    c5 = -(wr - wl) / (120.0 * L)
    
    return npp.Polynomial([c0, c1, c2, c3, c4, c5])


if __name__ == "__main__":
    pass
