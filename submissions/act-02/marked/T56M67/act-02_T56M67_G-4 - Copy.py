"""
CVE154 (A.Y. 2026-2027, S1)
Template script for Programming Activity No. 02

Prepared by Christian Cahig

This file belongs to the repository
https://github.com/christian-cahig/CVE154_AY-2026-2027-S1.
"""


import math as mt

__AUTHOR__ = "Group 4" 


def Ay(u, x, P=10, H=15):
    """Vertical force developed at roller support A."""
    if x <= H:
        return u * (1 - x / H)
    return 0.0


def Ey(u, x, P=10, H=15):
    """Vertical force developed at fixed support E."""
    return u - Ay(u, x, P, H)


def Em(u, x, P=10, H=15):
    """Reaction moment developed at fixed support E."""
    if x <= H:
        return u * x * ((4 * P / H) - 1)
    return u * (4 * P - x)


def Fy(u, x, P=10, H=15):
    """Magnitude of vertical force developed at internal hinge H."""
    if x <= H:
        return u * (x / H)
    return 0.0


def mu_G(u, x, P=10, H=15):
    """Bending moment developed at point G (x_G = 2.5 * P)."""
    x_G = 2.5 * P
    if x <= H:
        return u * x * (1 - (x_G / H))
    elif x <= x_G:
        return u * (x - x_G)
    else:
        return 0.0


load_mag = 5.0   
load_loc = 10.0   
panel_len = 10.0  
hinge_loc = 17.0 

if __name__ == "__main__":
    print(f"4 panels @ {panel_len} ft; hinge @ H = {hinge_loc} ft")
    print(f"{load_mag} kip @ x = {load_loc} ft")
    print(f"{" "*3}Ay = {Ay(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"{" "*3}Ey = {Ey(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"{" "*3}Em = {Em(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip-ft")
    print(f"{" "*3}Fy = {Fy(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"{" "*3}mu_G = {mu_G(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip-ft")

   