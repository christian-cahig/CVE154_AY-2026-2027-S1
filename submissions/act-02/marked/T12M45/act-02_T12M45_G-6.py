"""
CVE154 (A.Y. 2026-2027, S1)
Template script for Programming Activity No. 02

Prepared by Christian Cahig

This file belongs to the repository
https://github.com/christian-cahig/CVE154_AY-2026-2027-S1.
"""

import math as mt

__AUTHOR__ = "Group 6"

def Ay(u, x, P=10.0, H=15.0):
    # Check if parameters chosen are invalid or not.
    p_invalid = P <= 0
    h_invalid = H <= 0 or H >= 4 * P
    x_invalid = x < 0 or x > 4 * P
    if p_invalid:
        print(f"Warning: panel_len P = {P} must be greater than 0.")
    if h_invalid:
        print(f"Warning: hinge_loc H = {H} is out of bounds (0, {4*P}).")
    if x_invalid:
        print(f"Warning: load_loc x = {x} is out of bounds [0, {4*P}].")
    if p_invalid or h_invalid:
        return float('nan')         # Not An Answer or Invalid Geometry
    if x_invalid:
        return 0.0                  # No Load
        
    R_a = R_b = R_c = R_d = R_e = 0.0
    if 0 <= x <= P:                 # Pannel AB
        R_a = u * (P - x) / P
        R_b = u * x / P
    elif P <= x <= 2 * P:           # Pannel BC
        R_b = u * (2 * P - x) / P
        R_c = u * (x - P) / P
    elif 2 * P <= x <= 3 * P:       # Pannel CD
        R_c = u * (3 * P - x) / P
        R_d = u * (x - 2 * P) / P
    elif 3 * P <= x <= 4 * P:       # Pannel DE
        R_d = u * (4 * P - x) / P
        R_e = u * (x - 3 * P) / P
    else:
        R_a = R_b = R_c = R_d = R_e = 0.0
    return ((R_a * H) + (R_b * (H - P))) / H


def Ey(u, x, P=10.0, H=15.0):
    # Check if parameters chosen are invalid or not.
    p_invalid = P <= 0
    h_invalid = H <= 0 or H >= 4 * P
    x_invalid = x < 0 or x > 4 * P
    if p_invalid:
        print(f"Warning: panel_len P = {P} must be greater than 0.")
    if h_invalid:
        print(f"Warning: hinge_loc H = {H} is out of bounds (0, {4*P}).")
    if x_invalid:
        print(f"Warning: load_loc x = {x} is out of bounds [0, {4*P}].")
    if p_invalid or h_invalid:
        return float('nan')         # Not An Answer or Invalid Geometry
    if x_invalid:
        return 0.0                  # No Load
        
    R_a = R_b = R_c = R_d = R_e = 0.0
    if 0 <= x <= P:                 # Pannel AB
        R_a = u * (P - x) / P
        R_b = u * x / P
    elif P <= x <= 2 * P:           # Pannel BC
        R_b = u * (2 * P - x) / P
        R_c = u * (x - P) / P
    elif 2 * P <= x <= 3 * P:       # Pannel CD
        R_c = u * (3 * P - x) / P
        R_d = u * (x - 2 * P) / P
    elif 3 * P <= x <= 4 * P:       # Pannel DE
        R_d = u * (4 * P - x) / P
        R_e = u * (x - 3 * P) / P
    else:
        R_a = R_b = R_c = R_d = R_e = 0.0
    Fy_value = Fy(u, x, P, H)
    return Fy_value + R_c + R_d + R_e


def Em(u, x, P=10.0, H=15.0):       # Moment Reaction at E
    # Check if parameters chosen are invalid or not.
    p_invalid = P <= 0
    h_invalid = H <= 0 or H >= 4 * P
    x_invalid = x < 0 or x > 4 * P
    if p_invalid:
        print(f"Warning: panel_len P = {P} must be greater than 0.")
    if h_invalid:
        print(f"Warning: hinge_loc H = {H} is out of bounds (0, {4*P}).")
    if x_invalid:
        print(f"Warning: load_loc x = {x} is out of bounds [0, {4*P}].")
    if p_invalid or h_invalid:
        return float('nan')         # Not An Answer or Invalid Geometry
    if x_invalid:
        return 0.0                  # No Load
        
    R_a = R_b = R_c = R_d = R_e = 0.0
    if 0 <= x <= P:                 # Pannel AB
        R_a = u * (P - x) / P
        R_b = u * x / P
    elif P <= x <= 2 * P:           # Pannel BC
        R_b = u * (2 * P - x) / P
        R_c = u * (x - P) / P
    elif 2 * P <= x <= 3 * P:       # Pannel CD
        R_c = u * (3 * P - x) / P
        R_d = u * (x - 2 * P) / P
    elif 3 * P <= x <= 4 * P:       # Pannel DE
        R_d = u * (4 * P - x) / P
        R_e = u * (x - 3 * P) / P
    else:
        R_a = R_b = R_c = R_d = R_e = 0.0
    Fy_value = Fy(u, x, P, H)
    return (- R_d * P) - (R_c * 2 * P) - (Fy_value * 4 * P - H)

    
def Fy(u, x, P=10.0, H=15.0):
    # Check if parameters chosen are invalid or not.
    p_invalid = P <= 0
    h_invalid = H <= 0 or H >= 4 * P
    x_invalid = x < 0 or x > 4 * P
    if p_invalid:
        print(f"Warning: panel_len P = {P} must be greater than 0.")
    if h_invalid:
        print(f"Warning: hinge_loc H = {H} is out of bounds (0, {4*P}).")
    if x_invalid:
        print(f"Warning: load_loc x = {x} is out of bounds [0, {4*P}].")
    if p_invalid or h_invalid:
        return float('nan')         # Not An Answer or Invalid Geometry
    if x_invalid:
        return 0.0                  # No Load
        
    R_a = R_b = R_c = R_d = R_e = 0.0
    if 0 <= x <= P:                 # Pannel AB
        R_a = u * (P - x) / P
        R_b = u * x / P
    elif P <= x <= 2 * P:           # Pannel BC
        R_b = u * (2 * P - x) / P
        R_c = u * (x - P) / P
    elif 2 * P <= x <= 3 * P:       # Pannel CD
        R_c = u * (3 * P - x) / P
        R_d = u * (x - 2 * P) / P
    elif 3 * P <= x <= 4 * P:       # Pannel DE
        R_d = u * (4 * P - x) / P
        R_e = u * (x - 3 * P) / P
    else:
        R_a = R_b = R_c = R_d = R_e = 0.0
    Ay_value = Ay(u, x, P, H)
    return - Ay_value + R_a + R_b

    
def mu_G(u, x, P=10.0, H=15.0):     # Bending Moment at G
    # Check if parameters chosen are invalid or not.
    p_invalid = P <= 0
    h_invalid = H <= 0 or H >= 4 * P
    x_invalid = x < 0 or x > 4 * P
    if p_invalid:
        print(f"Warning: panel_len P = {P} must be greater than 0.")
    if h_invalid:
        print(f"Warning: hinge_loc H = {H} is out of bounds (0, {4*P}).")
    if x_invalid:
        print(f"Warning: load_loc x = {x} is out of bounds [0, {4*P}].")
    if p_invalid or h_invalid:
        return float('nan')         # Not An Answer or Invalid Geometry
    if x_invalid:
        return 0.0                  # No Load

    R_a = R_b = R_c = R_d = R_e = 0.0
    if 0 <= x <= P:                 # Pannel AB
        R_a = u * (P - x) / P
        R_b = u * x / P
    elif P <= x <= 2 * P:           # Pannel BC
        R_b = u * (2 * P - x) / P
        R_c = u * (x - P) / P
    elif 2 * P <= x <= 3 * P:       # Pannel CD
        R_c = u * (3 * P - x) / P
        R_d = u * (x - 2 * P) / P
    elif 3 * P <= x <= 4 * P:       # Pannel DE
        R_d = u * (4 * P - x) / P
        R_e = u * (x - 3 * P) / P
    else:
        R_a = R_b = R_c = R_d = R_e = 0.0
    Ey_value = Ey(u, x, P, H)
    Em_value = Em(u, x, P, H)
    return (- R_d * 0.5 * P) - (R_e * 1.5 * P) + (Ey_value * 1.5 * P) + Em_value


if __name__ == "__main__":
    
    load_mag = 10.0     # u
    load_loc = 20.0    # x  : must not be x < 0 or x > 4 * P, no load
    panel_len = 5.0    # P  : must not be P <= 0, negative lenght
    hinge_loc = 7.5    # H  : must not be H <= 0 or H >= 4 * P, no hinge or hinge at supports

    print(f"4 panels @ {panel_len} ft; hinge @ H = {hinge_loc} ft")
    print(f"{load_mag} kip @ x = {load_loc} ft")
    print(f"{' '*3}Ay = {Ay(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"{' '*3}Ey = {Ey(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"{' '*3}Em = {Em(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip-ft")
    print(f"{' '*3}Fy = {Fy(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"{' '*3}mu_G = {mu_G(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip-ft")

