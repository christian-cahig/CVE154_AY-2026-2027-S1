"""
CVE154 (A.Y. 2026-2027, S1)
Template script for Programming Activity No. 02

Prepared by Christian Cahig

This file belongs to the repository
https://github.com/christian-cahig/CVE154_AY-2026-2027-S1.
"""

import math as mt

__AUTHOR__= "Group 2"  


def _panel_reactions(u, x, P):
    """Calculates internal panel loads transferred from stringer to girder floor beams."""
    R_A = R_B = R_C = R_D = R_E = 0.0

    if 0 <= x < P:
        R_A = u * (P - x) / P
        R_B = u * x / P
    elif P <= x < 2 * P:
        R_B = u * (2 * P - x) / P
        R_C = u * (x - P) / P
    elif 2 * P <= x < 3 * P:
        R_C = u * (3 * P - x) / P
        R_D = u * (x - 2 * P) / P
    elif 3 * P <= x <= 4 * P:
        R_D = u * (4 * P - x) / P
        R_E = u * (x - 3 * P) / P

    return R_A, R_B, R_C, R_D, R_E

#Part 2

def Ay(u, x, P=10, H=15):
    """Vertical reaction force developed at roller support A."""
    R_A, R_B, _, _, _ = _panel_reactions(u, x, P)
    return R_A + R_B * (1.0 - P / H)


def Ey(u, x, P=10, H=15):
    """Vertical reaction force developed at fixed support E."""
    return u - Ay(u, x, P, H)


def Em(u, x, P=10, H=15):
    """Reaction moment developed at fixed support E."""
    return -u * (4.0 * P - x) - 4.0 * P * Ay(u, x, P, H)


def Fy(u, x, P=10, H=15):
    """Magnitude of force developed at internal hinge F."""
    _, R_B, _, _, _ = _panel_reactions(u, x, P)
    return R_B * (P / H)


def mu_G(u, x, P=10, H=15):
    """Bending moment developed at point G (midpoint of panel CD at x = 2.5P)."""
    R_A, R_B, R_C, R_D, R_E = _panel_reactions(u, x, P)
    return (((-2.5*(P**2)/H)+P)*R_B)+(1.5*P*R_C)+(P*R_D)
        

# --- Part 3: Synthesis Variables ---
if __name__== "__main__":
    load_mag = 12
    load_loc = 8
    panel_len = 10.0
    hinge_loc = 15

# --- Output / Verification ---

    print(f"Author : {__AUTHOR__}")
    print(f"Ay     : {Ay(load_mag, load_loc, panel_len, hinge_loc):.5f}")
    print(f"Ey     : {Ey(load_mag, load_loc, panel_len, hinge_loc):.5f}")
    print(f"Em     : {Em(load_mag, load_loc, panel_len, hinge_loc):.5f}")
    print(f"Fy     : {Fy(load_mag, load_loc, panel_len, hinge_loc):.5f}")
    print(f"mu_G   : {mu_G(load_mag, load_loc, panel_len, hinge_loc):.5f}")

    #AVILA, BALALA, PUGOY, TACTACON