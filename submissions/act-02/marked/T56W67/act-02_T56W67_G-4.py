"""
CVE154 (A.Y. 2026-2027, S1)
Template script for Programming Activity No. 02

Prepared by Christian Cahig

This file belongs to the repository
https://github.com/christian-cahig/CVE154_AY-2026-2027-S1.
"""

import math as mt

__AUTHOR__ = "Group 4"


def _get_panel_loads(u, x, P):
    if x < 0 or x > 4 * P:
        return 0.0, 0.0, 0.0, 0.0, 0.0

    if x == 4 * P:
        return 0.0, 0.0, 0.0, 0.0, float(u)

    idx = mt.floor(x / P)
    if idx > 3:
        idx = 3

    a = x - (idx * P)
    left_share = u * (P - a) / P
    right_share = u * a / P

    loads = [0.0] * 5
    loads[idx] += left_share
    loads[idx + 1] += right_share
    return tuple(loads)


def Ay(u, x, P=10, H=15):
    LA, LB, LC, LD, LE = _get_panel_loads(u, x, P)
    return LA + LB * (H - P) / H


def Fy(u, x, P=10, H=15):
    LA, LB, LC, LD, LE = _get_panel_loads(u, x, P)
    ay_value = Ay(u, x, P, H)
    return mt.fabs(ay_value - LA - LB)


def Ey(u, x, P=10, H=15):
    LA, LB, LC, LD, LE = _get_panel_loads(u, x, P)
    total_on_bridge = LA + LB + LC + LD + LE
    ay_value = Ay(u, x, P, H)
    return total_on_bridge - ay_value


def Em(u, x, P=10, H=15):
    LA, LB, LC, LD, LE = _get_panel_loads(u, x, P)
    ay_value = Ay(u, x, P, H)
    return ay_value * (4 * P) - (LA * 4 * P + LB * 3 * P + LC * 2 * P + LD * P)


def mu_G(u, x, P=10, H=15):
    LA, LB, LC, LD, LE = _get_panel_loads(u, x, P)
    ay_value = Ay(u, x, P, H)
    return ay_value * (2.5 * P) - (LA * 2.5 * P + LB * 1.5 * P + LC * 0.5 * P)
    

if __name__ == "__main__":
    load_mag = 1.0
    load_loc = 25.0
    panel_len = 10.0
    hinge_loc = 15.0



    print(f"4 panels @ {panel_len} ft; hinge @ H = {hinge_loc} ft")
    print(f"{load_mag} kip @ x = {load_loc} ft")
    print(f"{" "*3}Ay = {Ay(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"{" "*3}Ey = {Ey(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"{" "*3}Em = {Em(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"{" "*3}Fy = {Fy(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"{" "*3}mu_G = {mu_G(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip-ft")