"""
CVE154 (A.Y. 2026-2027, S1)
Template script for Programming Activity No. 02

Prepared by Christian Cahig

This file belongs to the repository
https://github.com/christian-cahig/CVE154_AY-2026-2027-S1.
"""
import math as mt

_AUTHOR_ = "Group 2"

def Ay(u, x, P=10, H=15):
    if 0 <= x <= P:
        dist = H - x
        Ay_value = u * dist / H
        return Ay_value

    elif P < x <= 2 * P:
        dist = 2 * P - x
        Ay_value = u * dist * (H - P) / (P * H)
        return Ay_value

    else:
        return 0

def Ey(u, x, P=10, H=15):
    Ey_value = u - Ay(u, x, P, H)

    return Ey_value

def Em(u, x, P=10, H=15):
    Ey_value = Ey(u, x, P, H)
    Em_value =  u * x - 4 * P * Ey_value

    return Em_value

def Fy(u, x, P=10, H=15):
    if 0 <= x <= P:
        Fy_value = u * x / H
        return Fy_value

    elif P < x <= 2 * P:
        dist = 2 * P - x
        Fy_value = u * dist / H
        return Fy_value

    else:
        return 0

def mu_G(u, x, P=10, H=15):
    if 0 <= x <= P:
        mu_value = (-u * x * (5 * P - 2 * H)/ (2 * H))
        return mu_value

    elif P < x <= 2 * P:
        dist = 2 * P - x

        mu_value = mu_value = -u * dist * (5 * P - 2 * H) / (2 * H) - u * (x - P) / 2
        return mu_value

    elif 2 * P < x <= 3 * P:
        dist = 3 * P - x
        mu_value = -u * dist / 2
        return mu_value

    else:
        return 0

if __name__ == "__main__":

    load_mag = 1
    load_loc = 20
    panel_len = 10
    hinge_loc = 15

    print(f"4 panels @ {panel_len} ft; hinge @ H = {hinge_loc} ft")
    print(f"{load_mag} kip @ x = {load_loc} ft")
    print(f"{" "*3}Ay = {Ay(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"{" "*3}Ey = {Ey(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"{" "*3}Em = {Em(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"{" "*3}Fy = {Fy(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"{" "*3}mu_G = {mu_G(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip-ft")