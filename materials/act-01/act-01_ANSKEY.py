"""
CVE154 (A.Y. 2026-2027, S1)
Template script for Programming Activity No. 01

Prepared by Christian Cahig

This file belongs to the repository
https://github.com/christian-cahig/CVE154_AY-2026-2027-S1.
"""

import math as mt

__AUTHOR__ = "Christian Cahig"

def watvol(r, h, l):
    rr = r ** 2
    return l * (
        (mt.pi * rr / 2) - (h * mt.sqrt(rr - (h ** 2))) - (rr * mt.asin(h / r))
    )

def wetper(d, h):
    r = d / 2
    return r * (mt.pi - (2 * mt.asin(h/r)))

def volper(d, l, h):
    wv = watvol((d * 0.0254) / 2, h / 100, l,)
    wp = wetper(d, h / 2.54)
    
    return [wv, wp]

if __name__ == "__main__":
    pass
