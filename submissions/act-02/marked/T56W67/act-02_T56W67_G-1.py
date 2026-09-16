#!/usr/bin/env python
# coding: utf-8

# In[17]:


"""
CVE154 (A.Y. 2026-2027, S1)
Template script for Programming Activity No. 02

Prepared by Christian Cahig

This file belongs to the repository
https://github.com/christian-cahig/CVE154_AY-2026-2027-S1.
"""

import math as mt

__AUTHOR__ = "Group 1"

load_mag = 10
load_loc = 15
panel_len = 10
hinge_loc = 15

u = load_mag
x = load_loc
P = panel_len
H = hinge_loc

def Ay(u, x, P=10, H=15):
    if 0 <= x <= P:
        return (H * u - u * x) / H
    elif P <= x <= 2 * P:
        return u * (2 * P - x) / P - u * (2 * P - x) / H
    elif 2 * P <= x <= 3 * P:
        return 0
    elif 3 * P <= x <= 4 * P:
        return 0


def Ey(u, x, P=10, H=15):
    if 0 <= x <= P:
        return (u * x) / H
    elif P <= x <= 2 * P:
        return (x - P) * u / P + u * (2 * P - x) / H
    elif 2 * P <= x <= 3 * P:
        return u
    elif 3 * P <= x <= 4 * P:
        return u


def Em(u, x, P=10, H=15):
    if 0 <= x <= P:
        return -u * x * (4 * P - H) / H
    elif P <= x <= 2 * P:
        return -u * (2 * P - x) * (4 * P - H) / H - 2 * u * (x - P)
    elif 2 * P <= x <= 3 * P:
        return -u * (4 * P - x)
    elif 3 * P <= x <= 4 * P:
        return -u * (4 * P - x)


def Fy(u, x, P=10, H=15):
    if 0 <= x <= P:
        return (u * x) / H
    elif P <= x <= 2 * P:
        return u * (2 * P - x) / H
    elif 2 * P <= x <= 3 * P:
        return 0
    elif 3 * P <= x <= 4 * P:
        return 0


def mu_G(u, x, P=10, H=15):
    if 0 <= x <= P:
        return u * x * (H - 2.5 * P) / H
    elif P <= x <= 2 * P:
        return u * (2.5 * H * P - 1.5 * H * x - 5 * P**2 + 2.5 * P * x)/ H
    elif 2 * P <= x <= 3 * P:
        return 0.5 * u * (x - 3 * P)
    elif 3 * P <= x <= 4 * P:
        return 0

if __name__ == "__main__":

    print(f"4 panels @ {panel_len} ft; hinge @ H = {hinge_loc} ft")
    print(f"{load_mag} kip @ x = {load_loc} ft")
    print(f"{" "*3}Ay = {Ay(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"{" "*3}Ey = {Ey(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"{" "*3}Em = {Em(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"{" "*3}Fy = {Fy(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"{" "*3}mu_G = {mu_G(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip-ft")


# In[ ]:




