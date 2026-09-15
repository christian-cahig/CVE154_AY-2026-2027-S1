"""
CVE154 (A.Y. 2026-2027, S1)
Template script for Programming Activity No. 02

Prepared by Christian Cahig

This file belongs to the repository
https://github.com/christian-cahig/CVE154_AY-2026-2027-S1.
"""

import math as mt

__AUTHOR__ = "Group 3"

def get_panel_loads (u, x, P):
    RA = RB = RC = RD = RE = 0.0
    if x <= P:
        RA = u * ((P - x) / P)
        RB = u * (x / P)
    elif x <= 2 * P:
        RB = u * ((2 * P - x) / P)
        RC = u * ((x - P) / P)
    elif x <= 3 * P:
        RC = u * ((3 * P - x) / P)
        RD = u * ((x - 2 * P) / P)
    else:
        RD = u * ((4 * P - x) / P)
        RE = u * ((x - 3 * P) / P)
    return RA, RB, RC, RD, RE

def Ay (u, x, P = 10, H = 18):
    RA, RB, RC, RD, RE = get_panel_loads (u, x, P)
    return RA + RB * ((H - P) / H)

def Ey (u, x, P = 10, H = 18):
    return u - Ay (u, x, P, H)

def Em (u, x, P = 10, H = 18):
    RA, RB, RC, RD, RE = get_panel_loads (u, x, P)
    return RA * (4 * P) + RB * (3 * P) + RC * (2 * P) + RD * P - Ay (u, x, P, H) * (4 * P)

def Fy (u, x, P = 10, H = 18):
    RA, RB, RC, RD, RE = get_panel_loads (u, x, P)
    return RB * (P / H)

def mu_G (u, x, P = 10, H = 18):
    RA, RB, RC, RD, RE = get_panel_loads (u, x, P)
    return Ay (u, x, P, H) * (2.5 * P) - RA * (2.5 * P) - RB * (1.5 * P) - RC * (0.5 * P)

if __name__ == "__main__":
    load_mag = 1.0
    load_loc = 9.0
    panel_len = 5.0
    hinge_loc = 7.5

    print(f"4 panels @ {panel_len} ft; hinge @ H = {hinge_loc} ft")
    print(f"{load_mag} kip @ x = {load_loc} ft")
    print(f"{" "*3}Ay = {Ay(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"{" "*3}Ey = {Ey(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"{" "*3}Em = {Em(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"{" "*3}Fy = {Fy(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"{" "*3}mu_G = {mu_G(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip-ft")