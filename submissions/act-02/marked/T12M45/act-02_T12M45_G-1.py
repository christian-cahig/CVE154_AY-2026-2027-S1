"""
CVE154 (A.Y. 2026-2027, S1)
Template script for Programming Activity No. 02

Prepared by Christian Cahig

This file belongs to the repository
https://github.com/christian-cahig/CVE154_AY-2026-2027-S1.
"""

import math as mt 

__AUTHOR__ = "Group 1" 

def forces(u, x, P):
    if 0 <= x <= P:
        return (u * (P - x)) / P, (u * (x / P)), 0, 0, 0 
    elif P < x <= 2 * P: 
        return 0, (u * ((2 * P) - x)) / P, (u * (x - P)) / P, 0, 0 
    elif 2 * P < x <= 3 * P: 
        return 0, 0, (u * ((3 * P) - x)) / P, (u * (x - (2 * P))) / P, 0 
    else: 
        return 0, 0, 0, (u * ((4 * P) - x)) / P, (u * (x - 3 * P)) / P 
    


def Ay(u, x, P=10, H=15): 
    Ra, Rb, Rc, Rd, Re = forces(u, x, P)
    return Ra + (Rb * (H - P) / H) 


def Ey(u, x, P=10, H=15): 
    Ra, Rb, Rc, Rd, Re = forces(u, x, P)
    
    return (Rb * (P / H)) + Rc + Rd + Re


def Em(u, x, P=10, H=15): 
    Ra, Rb, Rc, Rd, Re = forces(u, x, P)
    return Rb * (P / H) * (4 * P - H) + Rc * 2 * P + Rd * P 


def Fy(u, x, P=10, H=15): 
    Ra, Rb, Rc, Rd, Re = forces(u, x, P)
    return Rb * (P / H) 


def mu_G(u, x, P=10, H=15): 
    Ra, Rb, Rc, Rd, Re = forces(u, x, P)
    
    
    Em_val = Rb * (P / H) * (4 * P - H) + Rc * 2 * P + Rd * P 
    Ey_val = (Rb * (P / H)) + Rc + Rd + Re 
    
    return Em_val - (Ey_val * 1.5 * P) + Rd * 0.5 * P + Re * 1.5 * P 


load_mag = 1.0   # Value for u in kips
load_loc = 14.0    # Value for x in ft 
panel_len = 7.0  # Value for P in ft
hinge_loc = 11  # Value for H in ft


if __name__ == "__main__":

    print(f"4 panels @ {panel_len} ft; hinge @ H = {hinge_loc} ft")
    print(f"{load_mag} kip @ x = {load_loc} ft")
    print(f"   Ay = {Ay(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"   Ey = {Ey(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"   Em = {Em(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"   Fy = {Fy(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"   mu_G = {mu_G(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip-ft")