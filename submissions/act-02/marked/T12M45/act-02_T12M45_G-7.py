"""
CVE154 (A.Y. 2026-2027, S1)
Template script for Programming Activity No. 02

Prepared by Christian Cahig

This file belongs to the repository
https://github.com/christian-cahig/CVE154_AY-2026-2027-S1.
"""

import math as mt

__AUTHOR__= "Group 7"

def _reactions_of_panels(u, x, P, H):
    R_a = R_b = R_c = R_d = R_e = 0.0
    if 0 <= x <= P:
        xl = x - 0
        "xl - x distance from the left"
        R_b = u * xl / P
        R_a = u - R_b
    elif P <= x <= 2 * P:
        xl = x - P
        R_c = u * xl / P
        R_b = u - R_c
    elif 2 * P <= x <= 3 * P:
        xl = x - 2 * P
        R_d = u * xl / P
        R_c = u - R_d
    elif 3 * P <= x <= 4 * P:
        xl = x - 3 * P
        R_e = u * xl / P
        R_d = u - R_e
    else:
        print("The x is not within range of 4P")
    return R_a, R_b, R_c, R_d, R_e


def Ay(u, x, P, H):
    R_a, R_b, R_c, R_d, R_e = _reactions_of_panels(u, x, P, H)
    return R_a + R_b - (R_b * P) / H


def Fy(u, x, P, H):
    R_a, R_b, R_c, R_d, R_e = _reactions_of_panels(u, x, P, H)
    return (R_b * P) / H


def Ey(u, x, P, H):
    R_a, R_b, R_c, R_d, R_e =_reactions_of_panels(u, x, P, H)
    return (R_b * P) / H + R_c + R_d + R_e


def Em(u, x, P, H):
    R_a, R_b, R_c, R_d, R_e = _reactions_of_panels(u, x, P, H)
    return (R_b * P) - (4 * P ** 2 * R_b) / H - 2 * R_c * P - R_d * P

def mu_G(u, x, P, H):
    R_a, R_b, R_c, R_d, R_e = _reactions_of_panels(u, x, P, H)
    return (P * R_b) - (2.5 * P ** 2 * R_b) / H - (0.5 * P * R_c)

if __name__ == "__main__":

    load_mag = 10.0
    load_loc = 21.0
    panel_len = 10.0
    hinge_loc = 18.0

    print(f"4 panels @ {panel_len} ft; hinge @ H = {hinge_loc} ft")
    print(f"{load_mag} kip @ x = {load_loc} ft")
    print(f"{" "*3}Ay = {Ay(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"{" "*3}Ey = {Ey(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"{" "*3}Em = {Em(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"{" "*3}Fy = {Fy(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"{" "*3}mu_G = {mu_G(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip-ft")
