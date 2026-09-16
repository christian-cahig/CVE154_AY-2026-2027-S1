"""
CVE154 (A.Y. 2026-2027, S1)
Template script for Programming Activity No. 02

Prepared by Christian Cahig

This file belongs to the repository
https://github.com/christian-cahig/CVE154_AY-2026-2027-S1.
"""

import math as mt

__AUTHOR__ = "Group 17"

def floor_beam_forces(u, x, P):
    # Computes the forces developed in the floor beams
    Qa, Qb, Qc, Qd, Qe = 0, 0, 0, 0, 0
    xP = x / P

    if (0 <= x) and (x <= P):
        Qa = (1 - xP) * u
        Qb = xP * u
    elif (P <= x) and (x <= 2*P):
        Qb = (2 - xP) * u
        Qc = (xP - 1) * u
    elif (2*P <= x) and (x <= 3*P):
        Qc = (3 - xP) * u
        Qd = (xP - 2) * u
    elif (3*P <= x) and (x <= 4*P):
        Qd = (4 - xP) * u
        Qe = (xP - 3) * u
    else: raise Exception("Invalid load location")

    return (Qa, Qb, Qc, Qd, Qe)

def Ay(u, x, P = 10, H = 15):
    Qa, Qb, Qc, Qd, Qe = floor_beam_forces(u, x, P)

    return Qa + (1 - (P/H)) * Qb

def Ey(u, x, P = 10, H = 15):
    Qa, Qb, Qc, Qd, Qe = floor_beam_forces(u, x, P)

    return ((P/H) * Qb) + Qc + Qd + Qe

def Em(u, x, P = 10, H = 15):
    Qa, Qb, Qc, Qd, Qe = floor_beam_forces(u, x, P)

    return -((P/H) * ((4*P) - H) * Qb) - (2 * P * Qc) - (P * Qd)

def Fy(u, x, P = 10, H = 15):
    Qa, Qb, Qc, Qd, Qe = floor_beam_forces(u, x, P)

    return (P/H) * Qb

def mu_G(u, x, P = 10, H = 15):
    Qa, Qb, Qc, Qd, Qe = floor_beam_forces(u, x, P)

    return (((-2.5 * (P**2) / H) + P) * Qb) - (0.5 * P * Qc)

if __name__ == "__main__":
    load_mag = 1
    load_loc = 20
    panel_len = 10
    hinge_loc = 15

    print(f"4 panels @ {panel_len} ft; hinge @ H = {hinge_loc} ft")
    print(f"{load_mag} kip @ x = {load_loc} ft")
    print(f"{" "*3}Floor beam forces: {floor_beam_forces(load_mag, load_loc, panel_len)} kip")
    print(f"{" "*3}Ay = {Ay(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"{" "*3}Ey = {Ey(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"{" "*3}Em = {Em(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"{" "*3}Fy = {Fy(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"{" "*3}mu_G = {mu_G(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip-ft")
