"""
CVE154 (A.Y. 2026-2027, S1)
Template script for Programming Activity No. 03

Prepared by Christian Cahig

This file belongs to the repository
https://github.com/christian-cahig/CVE154_AY-2026-2027-S1.
"""

import math as mt
import scipy.optimize as spo

__AUTHOR__ = "Group 2"



# Part 1. Core


def fun(x, ed=0.01, Re=5000, D=1):
    return ( x + 2 * mt.log10( ed / (3.7 * D) + (2.51 * x) / Re))


def dfun(x, ed=0.01, Re=5000, D=1):
    A = ed / (3.7 * D) + (2.51 * x) / Re

    return (1 + (2 / mt.log(10))* (2.51 / Re)/ A)



#Part 2. Synthesis:

# Part 2-1. Bisection Method:

e_bs = 10 ** -7

x0_bs = (0.001, 10)

K_bs = mt.ceil(mt.log( (x0_bs[1] - x0_bs[0]) / e_bs,2))

#relative roughness
ed_bs = 0.0123456789

#Reynolds Number
Re_bs = 9876.543210

#Diameter
D_bs = 1

z_bs = lambda x: fun(
    x,
    ed=ed_bs,
    Re=Re_bs,
    D=D_bs)
x_bs, x_bs_info = spo.bisect(
    z_bs,
    x0_bs[0],
    x0_bs[1],
    xtol=e_bs,
    rtol=e_bs,
    maxiter=K_bs,
    full_output=True)
f_bs = 1/(x_bs)**2

print("Part 2-1. Bisection")
print(f"{' ' * 3}rel. rough.: {0.0123456789}")
print(f"{' ' * 3}Reynolds n.: {9876.543210}")
print(f"{' ' * 3}init. guess: {x0_bs}")
print(f"{' ' * 3}max. iters.: {K_bs}")
print(f"{' ' * 3}z({x_bs}) = {z_bs(x_bs)} in {x_bs_info.iterations} iters.")
print(f"{' ' * 3}value of x.: {x_bs} ")
print(f"{' ' * 3}fric. fact.: {f_bs} ")


# Part 2-2: Newton_Raphson

# Given values
relative_roughness = 0.0456789123
R = 6789.54321
e_nr = 10**-7
x0_nr = 4
K_nr = K_bs + 3

# Functions with the given parameters fixed
z_nr = lambda x: fun(x, relative_roughness, R)
dz_nr = lambda x: dfun(x, relative_roughness, R)

# Newton-Raphson
x_nr, x_nr_info = spo.newton(
    z_nr,
    x0_nr,
    fprime=dz_nr,
    tol=e_nr,
    maxiter=K_nr,
    full_output=True
)

print("Part 2-2. Newton-Raphson")
print(f"{' ' * 3}rel. rough.: {0.0456789123}")
print(f"{' ' * 3}Reynolds n.: {6789.543210}")
print(f"{' ' * 3}init. guess: {x0_nr}")
print(f"{' ' * 3}max. iters.: {K_nr}")
print(f"{' ' * 3}z({x_nr}) = {z_nr(x_nr)} in {x_nr_info.iterations} iters.")
print(f"{' ' * 3}value of x.: {x_nr}")
print(f"{' ' * 3}fric. fact.: {1/(x_nr)**2}")



# Part 2-3. Secant Method:
e_sc = 10 ** -7
x0_sc = (x_bs, x_nr)
K_sc = K_nr + 2

z_sc = lambda x: fun(x, 0.0213789456, 4567.890123)

x_sc, x_sc_info = spo.newton(
    z_sc,
    x0=x0_sc[1],
    x1=x0_sc[0],
    tol=e_sc,
    maxiter=K_sc,
    full_output=True
)

print("Part 2-3. Secant")
print(f"{' ' * 3}rel. rough.: {0.0213789456}")
print(f"{' ' * 3}Reynolds n.: {4567.890123}")
print(f"{' ' * 3}init. guess: {x0_sc}")
print(f"{' ' * 3}max. iters.: {K_sc}")
print(f"{' ' * 3}z({x_sc}) = {z_sc(x_sc)} in {x_sc_info.iterations} iters.")
print(f"{' ' * 3}value of x.: {x_sc}")
print(f"{' ' * 3}fric. fact.: {1/(x_sc)**2}")


# Part 2-4. TOMS Algorithm 748:

e_to = 1e-7
x0_to = (1.0, 100.0)  # Initial interval [a0, b0]
K_to = mt.ceil(mt.log((x0_to[1] - x0_to[0]) / e_to, 2))
ed_to = 0.0321789456
Re_to = 12345.6789

z_to = lambda x: fun(x, ed=ed_to, Re=Re_to)

x_to, x_to_info = spo.toms748(
        z_to,
        a=x0_to[0],
        b=x0_to[1],
        rtol=e_to,
        xtol=e_to,
        k=2,
        maxiter=K_to,
        full_output=True,
    )

print("Part 2-4. TOMS Algorithm 748")
print(f"{' ' * 3}rel. rough.: {0.0321789456}")
print(f"{' ' * 3}Reynolds n.: {12345.6789}")
print(f"{' ' * 3}init. guess: {x0_to}")
print(f"{' ' * 3}max. iters.: {K_to}")
print(f"{' ' * 3}z({x_to}) = {z_to(x_to)} in {x_to_info.iterations} iters.")
print(f"{' ' * 3}value of x.: {x_to}")
print(f"{' ' * 3}fric. fact.: {1.0 / (x_to ** 2)}")


