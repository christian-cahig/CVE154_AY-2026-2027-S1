"""
CVE154 (A.Y. 2026-2027, S1)
Template script for Programming Activity No. 02

Prepared by Christian Cahig

This file belongs to the repository
https://github.com/christian-cahig/CVE154_AY-2026-2027-S1
"""

import math as mt

_AUTHOR_ = "Group 5"


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
    return u


def Em(u, x, P, H):
    total_span = 4 * P

    if x <= H:
        return Fy(u, x, P, H) * (total_span - H)
    return u * (total_span - x)


def mu_G(u, x, P, H):
    x_G = 2.5 * P
    total_span = 4 * P

    ey = Ey(u, x, P, H)
    em = Em(u, x, P, H)

    m_g = ey * (total_span - x_G) - em

    if x > x_G:
        m_g -= u * (x - x_G)

    return m_g


load_mag = 1.0
load_loc = 20.0
panel_len = 10.0
hinge_loc = 17.0


if __name__ == "__main__":
 
    print(f"4 panels @ {panel_len} ft; hinge @ H = {hinge_loc} ft")
    print(f"{load_mag} kip @ x = {load_loc} ft")
    print(f"{" "*3}Ay = {Ay(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"{" "*3}Ey = {Ey(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"{" "*3}Em = {Em(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"{" "*3}Fy = {Fy(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"{" "*3}mu_G = {mu_G(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip-ft")