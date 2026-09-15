"""
CVE154 (A.Y. 2026-2027, S1)
Template script for Programming Activity No. 02

Prepared by Christian Cahig

This file belongs to the repository
https://github.com/christian-cahig/CVE154_AY-2026-2027-S1.
"""
import math as mt

__AUTHOR___ = "Group 4"

def R_a (u, x, P): 
    if 0 <= x <= P:
        R_a = u - u * x / P
    elif P <= x <= 2 * P:
        R_a = 0
    elif 2 * P <= x <= 3 * P:
        R_a = 0
    elif 3 * P <= x <= 4 * P: 
        R_a = 0

def R_b (u, x, P):
    if 0 <= x <= P:
        R_b = u * x / P 
    elif P <= x <= 2 * P:
        R_b = u - u * (x - P) / P
    elif 2 * P <= x <= 3 * P:
        R_b = 0
    elif 3 * P <= x <= 4 * P: 
        R_b = 0
    
def R_c (u, x, P):
    if 0 <= x <= P:
        R_c = 0
    elif P <= x <= 2 * P:
        R_c = u * (x - P) / P
    elif 2 * P <= x <= 3 * P:
        R_c = u - u * (x - 2*P)/ P
    elif 3 * P <= x <= 4 * P: 
        R_c = 0

def R_d (u, x, P):
    if 0 <= x <= P:
        R_d = 0
    elif P <= x <= 2 * P:
        R_d = 0
    elif 2 * P <= x <= 3 * P:
        R_d = u * (x - 2*P) / P
    elif 3 * P <= x <= 4 * P: 
        R_d = u - u * (x - 3*P) / P

def R_e (u, x, P):
    if 0 <= x <= P:
        R_e = 0
    elif P <= x <= 2 * P:
        R_e = 0
    elif 2 * P <= x <= 3 * P:
        R_e = 0 
    elif 3 * P <= x <= 4 * P: 
        R_e = u * (x - 3*P)/ P

    return R_a, R_b, R_c, R_d, R_e
    
def Ay(u, x, P=10, H=15):
    if x < H:
        Ay_value = u * (1 - x / H)
    elif x >  H:
        Ay_value = 0
    else:
        Ay_value = 0

    return Ay_value

def Ey(u, x, P=10, H=15):
    if x < H:
        Ey_value = u * x / H
    elif x > H:
        Ey_value = u
    else:
        Ey_value = u

    return Ey_value


def Em(u, x, P=10, H=15):
    if x < H:
        Em_value = u * x * (1 - 4 * P / H)
    elif x > H:
        Em_value = u * (x - 4 * P)
    else:
        Em_value = u * (H - 4 * P)

    return Em_value


def Fy(u, x, P=10, H=15):
    if x < H:
        Fy_value = u * x / H
    elif x > H:
        Fy_value = 0
    else:
        Fy_value = u

    return Fy_value


def mu_G(u, x, P=10, H=15):
    G = 5 * P / 2

    if x < H:
        mu_G_value = 0
    elif x > H:
        mu_G_value = u * (G - x)
    else:
        mu_G_value = 0

    return mu_G_value


if __name__ == "__main__":

    load_mag = 1
    load_loc = 10
    panel_len = 15
    hinge_loc = 15
    
    print(f"4 panels @ {panel_len} ft; hinge @ H = {hinge_loc} ft")
    print(f"{load_mag} kip @ x = {load_loc} ft")
    print(f"{" "*3}Ay = {Ay(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"{" "*3}Ey = {Ey(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"{" "*3}Em = {Em(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"{" "*3}Fy = {Fy(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"{" "*3}mu_G = {mu_G(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip-ft")
