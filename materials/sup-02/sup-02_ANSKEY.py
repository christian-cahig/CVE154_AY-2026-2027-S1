"""
CVE154 (A.Y. 2026-2027, S1)
Template script for Supplemental Material No. 02

Prepared by Christian Cahig

This file belongs to the repository
https://github.com/christian-cahig/CVE154_AY-2026-2027-S1.
"""

import math as mt
import scipy.optimize as spo

__AUTHOR__ = "Christian Cahig"

def uptown_func(x, d = 7, l = 10, V = 17):
    r = d / 2; rr = r ** 2
    v_ = l * ((rr * mt.pi / 2) - (rr * mt.asin(x / r)) - (x * mt.sqrt(rr - (x ** 2))))

    return v_ - V

def daft_func(x, d = 7, l = 10, V = 17):
    r = d / 2
    return - 2 * l * mt.sqrt((r**2) - (x**2))

def wet_per(h, d):
    r = d / 2
    return r * (mt.pi - (2 * mt.asin(h/r)))

if __name__ == "__main__":
    # Part 2
    dia, len, vol = 1, 3, 1

    iter_budget = 1000
    lb, ub = 0, dia / 2
    x0 = (lb + ub) / 2

    # Part 3
    f = lambda x : uptown_func(x, d = dia, l = len, V = vol)
    df = lambda x : daft_func(x, d = dia, l = len, V = vol)

    # Part 4
    h_bs, h_bs_info = spo.bisect(f, lb, ub, maxiter = iter_budget, full_output = True, disp = False)
    f_bs = f(h_bs)
    p_bs = wet_per(h_bs, dia)
    df_bs = df(h_bs)

    # Part 5
    h_nr, h_nr_info = spo.newton(f, x0, fprime = df, maxiter = iter_budget, full_output = True, disp = False)
    f_nr = f(h_nr)
    p_nr = wet_per(h_nr, dia)
    df_nr = df(h_nr)

    # Part 6
    h_sc, h_sc_info = spo.newton(f, x0, x1 = lb, maxiter = iter_budget, full_output = True, disp = False)
    f_sc = f(h_sc)
    p_sc = wet_per(h_sc, dia)
    df_sc = df(h_sc)

    # Part 7
    h_to, h_to_info = spo.toms748(f, lb, ub, maxiter = iter_budget, full_output = True, disp = False)
    f_to = f(h_to)
    p_to = wet_per(h_to, dia)
    df_to = df(h_to)

    print("Trough parameters:")
    print(f"{" "*3}diameter: {dia} m")
    print(f"{" "*3}length: {len} m")
    print(f"{" "*3}volume: {vol} m")

    print("Initial guesses:")
    print(f"{" "*3}interval: {lb}, {ub}")
    print(f"{" "*3}point: {x0}")

    print("Bisection:")
    print(f"{" "*3}h = {h_bs}")
    print(f"{" "*3}f = {f_bs}")
    print(f"{" "*3}P = {p_bs}")
    print(f"{" "*3}f' = {df_bs}")

    print("Newton-Raphson:")
    print(f"{" "*3}h = {h_nr}")
    print(f"{" "*3}f = {f_nr}")
    print(f"{" "*3}P = {p_nr}")
    print(f"{" "*3}f' = {df_nr}")

    print("Secant:")
    print(f"{" "*3}h = {h_sc}")
    print(f"{" "*3}f = {f_sc}")
    print(f"{" "*3}P = {p_sc}")
    print(f"{" "*3}f' = {df_sc}")

    print("TOMS Algorithm 748:")
    print(f"{" "*3}h = {h_to}")
    print(f"{" "*3}f = {f_to}")
    print(f"{" "*3}P = {p_to}")
    print(f"{" "*3}f' = {df_to}")
