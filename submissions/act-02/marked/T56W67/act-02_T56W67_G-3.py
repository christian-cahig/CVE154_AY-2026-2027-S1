"""
CVE154 (A.Y. 2026-2027, S1)
Template script for Programming Activity No. 02

Prepared by Christian Cahig

This file belongs to the repository
https://github.com/christian-cahig/CVE154_AY-2026-2027-S1.
"""

import math as mt

__AUTHOR__ = "Group 3"

def Ay(u, x, P=10, H=15):
    AY = u*x*(H-P)/H*P
    return AY
def Ey(u, x, P=10, H=15):
    EY = (u*(x-P)/P) + (u*(x-2*P)/P) + (u*x/P) - (u*x*(H-P)/(H*P))
    return EY
def Em(u, x, P=10, H=15):
    EM = (u*P*(x-P)) + (u*(x-2*P)) + (((u*x/P) - (u*x*(H-P)/(H*P)))*(4*P - H))
    return EM
def Fy(u, x, P=10, H=15):
    FY = (u*x/P) - (u*x*(H-P)/(H*P))
    return FY
def mu_G(u, x, P=10, H=15):
    FY = (u*x/P) - (u*x*(H-P)/(H*P))
    EY = (u*(x-P)/P) + (u*(x-2*P)/P) + (u*x/P) - (u*x*(H-P)/(H*P))
    EM = (u*P*(x-P)) + (u*(x-2*P)) + (((u*x/P) - (u*x*(H-P)/(H*P)))*(4*P - H))
    MU_G = FY*(2.5*P - H) + ((u*(x-P)/P)*(P/2)) - ((u*(x-2*P)/P)*(P/2)) + (1.5*P)*EY - EM
    return MU_G


if __name__ == "__main__":

    load_mag = 2
    load_loc = 15
    panel_len = 7
    hinge_loc = 8

    u = load_mag
    x = load_loc 
    P = panel_len
    H = hinge_loc



    print(f"4 panels @ {panel_len} ft; hinge @ H = {hinge_loc} ft")
    print(f"{load_mag} kip @ x = {load_loc} ft")
    print(f"{" "*3}Ay = {Ay(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"{" "*3}Ey = {Ey(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"{" "*3}Em = {Em(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"{" "*3}Fy = {Fy(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"{" "*3}mu_G = {mu_G(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip-ft")
