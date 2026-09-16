"""
CVE154 (A.Y. 2026-2027, S1)
Template script for Programming Activity No. 02

Prepared by Christian Cahig

This file belongs to the repository
https://github.com/christian-cahig/CVE154_AY-2026-2027-S1.
"""


import math as mt


_AUTHOR_ = "Group 6"  

def Ay(u, x, P, H):
    if x <= H:
        return u * (H - x) / H
    return 0.0


def Fy(u, x, P, H):
    if x <= H:
        return u * x / H
    return 0.0


def Ey(u, x, P, H):
    if x <= H:
        return Fy(u, x, P, H)
    else:
        return u


def Em(u, x, P, H):
    total_span = 4 * P
    if x <= H:
        return Fy(u, x, P, H) * (total_span - H)
    else:
        return u * (total_span - x)


def mu_G(u, x, P, H):
    x_G = 2.5 * P
    total_span = 4 * P

    ey = Ey(u, x, P, H)
    em = Em(u, x, P, H)
    m_g = ey * (total_span - x_G) - em

    if x > x_G:
        m_g = u * (x - x_G)

    return m_g


load_mag = 2 
load_loc = 21
panel_len = 7  
hinge_loc = 8

if __name__ == "__main__":

    print(f" Ay : {Ay(load_mag, load_loc, panel_len, hinge_loc)} kips")
    print(f" Ey : {Ey(load_mag, load_loc, panel_len, hinge_loc)} kips")
    print(f" Em : {Em(load_mag, load_loc, panel_len, hinge_loc)} kips-ft")
    print(f" Fy : {Fy(load_mag, load_loc, panel_len, hinge_loc)} kips")
    print(f" mu_G : {mu_G(load_mag, load_loc, panel_len, hinge_loc)} kips-ft")