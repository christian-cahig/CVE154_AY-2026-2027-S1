"""
CVE154 (A.Y. 2026-2027, S1)
Template script for Programming Activity No. 05

Prepared by Christian Cahig

This file belongs to the repository
https://github.com/christian-cahig/CVE154_AY-2026-2027-S1.
"""

import numpy as np
import numpy.polynomial as npp

__AUTHOR__ = "Group 17"

def Ay(wl, wr, L):
	return (wr - (2 * wl)) * L / 6

def By(wl, wr, L):
	return ((2 * wr) - wl) * L / 6

def get_nu(wl, wr, L):
    coeffs = [
        (wr - (2 * wl)) * L / 6,
        wl,
        -(wl + wr) / (2 * L)
    ]
    return npp.Polynomial(coeffs)

def get_mu(wl, wr, L):
    coeffs = [
        0,
        (wr - (2 * wl)) * L / 6,
        wl / 2,
        -(wl + wr) / (6 * L)
    ]
    return npp.Polynomial(coeffs)

def get_m(wl, wr, L):
    coeffs = [
        ((8 * wl) - (7 * wr)) * (L**3) / 360,
        0,
        (wr - (2 * wl)) * L / 12,
        wl / 6,
        -(wl + wr) / (24 * L)
    ]
    return npp.Polynomial(coeffs)

def get_y(wl, wr, L):
    coeffs = [
        0,
        ((8 * wl) - (7 * wr)) * (L**3) / 360,
        0,
        (wr - (2 * wl)) * L / 36,
        wl / 24,
        -(wl + wr) / (120 * L)
    ]
    return npp.Polynomial(coeffs)

if __name__ == "__main__":
    CASES = {
        "1" : (17, 21, 37, 2.14),
        "2" : (18, 34, 42, 9.11),
        "3" : (27, 37, 42, 4.21),
        "4" : (21, 27, 47, 1.57),
        "5" : (2.1, 2.7, 4.7, .157),
    }

    CASE = 5
    wl, wr, L, gamma = CASES[str(int(CASE))]
    nu, mu, m, y = [f(-wl-gamma, -wr+gamma, L) for f in [get_nu, get_mu, get_m, get_y]]

    print(f"Case {CASE}: wL = {wl} N/m; wR = {wr} N/m; L = {L} m; γ = {gamma} N/m")
    # Reactions
    print(f"{' '*3}", end="")
    print(*[f"{fun.__name__} = {fun(-wl, -wr, L):.7f} N" for fun in [Ay, By]], sep="\t")
    # ν(x), μ(x), m(x), and y(x), and their representative values
    for fx, fun, unit in zip(["ν", "μ", "m", "y"], [nu, mu, m, y], ["N", "N-m", "rad.", "m"]):
        print(f"{' '*3}{fx}(x) = {fun.__str__()} {unit}")
        for x in np.linspace(0, L, num=5, endpoint=True):
            print(f"{' '*6}@ x = {x:.3f} m:", f"{fun(x):.7f} {unit}", sep="\t")
    # Roots of ν(x)
    print(f"{' '*3}Roots of ν(x):", end=f"\n{' '*6}")
    print(*[f"{r:.3f}" for r in nu.roots()], sep="\t")
    # Local extrema of μ(x)
    print(f"{' '*3}Local extrema of μ(x):")
    for r in [r for r in nu.roots() if (0 <= r) and (r <= L)]:
        print(
            f"{' '*6}@ x = {r.real:.7f} m:",
            f"ν(x) = {nu(r.real):.7f} N",
            f"μ(x) = {mu(r.real):.7f} N-m",
            sep="\t"
        )
    # Roots of m(x)
    print(f"{' '*3}Roots of m(x):", end=f"\n{' '*6}")
    print(*[f"{r:.3f}" for r in m.roots()], sep="\t")
    # Local extrema of y(x)
    print(f"{' '*3}Local extrema of y(x):")
    for r in [r for r in m.roots() if (0 <= r) and (r <= L)]:
        print(
            f"{' '*6}@ x = {r.real:.7f} m:",
            f"m = {m(r.real):.7f} rad.",
            f"y = {y(r.real):.7f} m",
            sep="\t"
        )