"""
CVE154 (A.Y. 2026-2027, S1)
Template script for Programming Activity No. 02

Prepared by Christian Cahig

This file belongs to the repository
https://github.com/christian-cahig/CVE154_AY-2026-2027-S1.
"""

import math as mt

__Author__ = "Group 1"

def get_panel_reactions(u, x, P):
    """Calculates floor beam load reactions at panel points A, B, C, D, E."""
    R_A = R_B = R_C = R_D = R_E = 0.0

    if 0 <= x < P:
        R_A = u * (1 - x / P)
        R_B = u * (x / P)
    elif P <= x < 2 * P:
        R_B = u * (2 - x / P)
        R_C = u * (x / P - 1)
    elif 2 * P <= x < 3 * P:
        R_C = u * (3 - x / P)
        R_D = u * (x / P - 2)
    elif 3 * P <= x <= 4 * P:
        R_D = u * (4 - x / P)
        R_E = u * (x / P - 3)

    return R_A, R_B, R_C, R_D, R_E


def Ay(u, x, P=10, H=15):
    R_A, R_B, R_C, R_D, R_E = get_panel_reactions(u, x, P)
    panel_coords = [0, P, 2 * P, 3 * P, 4 * P]
    reactions = [R_A, R_B, R_C, R_D, R_E]

    moment_sum = 0.0
    for R, x_i in zip(reactions, panel_coords):
        if x_i < H:
            moment_sum += R * (H - x_i)

    return moment_sum / H


def Ey(u, x, P=10, H=15):
    R_A, R_B, R_C, R_D, R_E = get_panel_reactions(u, x, P)
    total_load = R_A + R_B + R_C + R_D + R_E
    return total_load - Ay(u, x, P, H)


def Em(u, x, P=10, H=15):
    R_A, R_B, R_C, R_D, R_E = get_panel_reactions(u, x, P)
    ay_val = Ay(u, x, P, H)

    # Reaction moment at fixed support E
    m_ay = ay_val * (4 * P)
    m_loads = R_A * (4 * P) + R_B * (3 * P) + R_C * (2 * P) + R_D * (1 * P)

    return - m_loads + m_ay


def Fy(u, x, P=10, H=15):
    R_A, R_B, R_C, R_D, R_E = get_panel_reactions(u, x, P)
    ay_val = Ay(u, x, P, H)

    panel_coords = [0, P, 2 * P, 3 * P, 4 * P]
    reactions = [R_A, R_B, R_C, R_D, R_E]

    loads_left_of_hinge = sum(
        R for R, x_i in zip(reactions, panel_coords) if x_i <= H
    )
    return abs(ay_val - loads_left_of_hinge)


def mu_G(u, x, P=10, H=15):
    R_A, R_B, R_C, R_D, R_E = get_panel_reactions(u, x, P)
    ey_val = Ey(u, x, P, H)
    em_val = Em(u, x, P, H)

    # Bending moment at G (x = 2.5 * P) considering right cut (G to E)
    return em_val - ey_val * (1.5 * P) + R_D * (0.5 * P) + R_E * (1.5 * P)


# Part 3: Input Variables
load_mag = 1.0
load_loc = 10.0
panel_len = 5.0
hinge_loc = 9.9999

if __name__ == "__main__":

    print(f"4 panels @ {panel_len} ft; hinge @ H = {hinge_loc} ft")
    print(f"{load_mag} kip @ x = {load_loc} ft")
    print(f"{" "*3}Ay = {Ay(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"{" "*3}Ey = {Ey(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"{" "*3}Em = {Em(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"{" "*3}Fy = {Fy(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"{" "*3}mu_G = {mu_G(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip-ft")
