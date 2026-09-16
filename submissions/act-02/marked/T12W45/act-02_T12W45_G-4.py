#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
CVE154 (A.Y. 2026-2027, S1)
Template script for Programming Activity No. 02

Prepared by Christian Cahig

This file belongs to the repository
https://github.com/christian-cahig/CVE154_AY-2026-2027-S1.
"""

import math as mt

__AUTHOR__ = "Group 4"

def Ay(mu, x, *, P=10, H=15):
    """Vertical reaction at roller A, in kip."""
    if 0 <= x <= P:
        return mu * (1 - x / H)
    if P < x <= 2 * P:
        return mu * (H - P) * (2 * P - x) / (P * H)
    return 0.0


def Ey(mu, x, *, P=10, H=15):
    """Vertical reaction at fixed support E, in kip."""
    return mu - Ay(mu, x, P=P, H=H)


def Em(mu, x, *, P=10, H=15):
    """Reaction moment at E, in kip-ft; CCW is positive."""
    return mu * x - 4 * P * Ey(mu, x, P=P, H=H)


def Fy(mu, x, *, P=10, H=15):
    """Magnitude of the vertical force at hinge F, in kip."""
    if 0 <= x <= P:
        return mu * x / H
    if P < x <= 2 * P:
        return mu * (2 * P - x) / H
    return 0.0


def mu_G(mu, x, *, P=10, H=15):
    """Bending moment at G, in kip-ft; sagging is positive."""
    G = 2.5 * P

    if 0 <= x <= P:
        return mu * x * (1 - G / H)

    if P < x <= 2 * P:
        return mu * (G * (H - P) * (2 * P - x) / (P * H) - (G - x))

    if 2 * P < x <= 3 * P:
        return -0.5 * mu * (3 * P - x)

    return 0.0


# In[32]:


if __name__ == "__main__":

    load_mag = 1            # u, kip
    load_loc = 20            # x, ft
    panel_len = 10           # P, ft
    hinge_loc = 11           # H, ft

    print(f"4 panels @ {panel_len} ft; hinge @ H = {hinge_loc} ft")
    print(f"{load_mag} kip @ x = {load_loc} ft")
    print(f"{" "*3}Ay = {Ay(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"{" "*3}Ey = {Ey(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"{" "*3}Em = {Em(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"{" "*3}Fy = {Fy(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip")
    print(f"{" "*3}mu_G = {mu_G(load_mag, load_loc, P=panel_len, H=hinge_loc):.5f} kip-ft")


# In[ ]:




