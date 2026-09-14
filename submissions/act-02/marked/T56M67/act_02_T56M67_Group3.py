"""
CVE154 (A.Y. 2026-2027, S1)
Template script for Programming Activity No. 02

Prepared by Christian Cahig

This file belongs to the repository
https://github.com/christian-cahig/CVE154_AY-2026-2027-S1.
"""

import math as mt

__AUTHOR__ = "Group 3"


def _panel_loads(u, x, P):
   
    if not (0 <= x <= 4 * P):
        raise ValueError

    PA = PB = PC = PD = PE = 0.0
    if x <= P:  
        PA = u * (P - x) / P
        PB = u * x / P
    elif x <= 2 * P:  
        PB = u * (2 * P - x) / P
        PC = u * (x - P) / P
    elif x <= 3 * P:  
        PC = u * (3 * P - x) / P
        PD = u * (x - 2 * P) / P
    else:  
        PD = u * (4 * P - x) / P
        PE = u * (x - 3 * P) / P
    return PA, PB, PC, PD, PE


def Fy(u, x, P=10, H=15):
    _, PB, _, _, _ = _panel_loads(u, x, P)
    return PB * P / H


def Ay(u, x, P=10, H=15):
    PA, PB, _, _, _ = _panel_loads(u, x, P)
    return PA + PB - Fy(u, x, P, H)


def Ey(u, x, P=10, H=15):
    return u - Ay(u, x, P, H)


def Em(u, x, P=10, H=15):
    _, _, PC, PD, _ = _panel_loads(u, x, P)
    return -((4 * P - H) * Fy(u, x, P, H) + 2 * P * PC + P * PD)


def mu_G(u, x, P=10, H=15):
    _, PB, PC, _, _ = _panel_loads(u, x, P)
    return P * PB * (2 * H - 5 * P) / (2 * H) - P * PC / 2


if __name__ == "__main__":

    load_mag = 1     # u, kip
    load_loc = 10    # x, ft
    panel_len = 10   # P, ft
    hinge_loc = 15    # H, ft

    print(f"4 panels @ {panel_len} ft; hinge @ H = {hinge_loc} ft")
    print(f"{load_mag} kip @ x = {load_loc} ft")
    print(f"{" "*3}Ay = {Ay(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"{" "*3}Ey = {Ey(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"{" "*3}Em = {Em(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"{" "*3}Fy = {Fy(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"{" "*3}mu_G = {mu_G(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip-ft")
