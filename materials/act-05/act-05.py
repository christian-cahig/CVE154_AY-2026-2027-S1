"""
CVE154 (A.Y. 2026-2027, S1)
Template script for Programming Activity No. 05

Prepared by Christian Cahig

This file belongs to the repository
https://github.com/christian-cahig/CVE154_AY-2026-2027-S1.
"""

if __name__ == "__main__":
    pass
    print(f"wL = {wl} N/m; wR = {wr} N/m; L = {L} m")
    print(
        f"{' '*3}Ay: {Ay(wl, wr, L):.7f}",
        f"By: {By(wl, wr, L):.7f}",
        sep="\t"
    )
    for fx, fun in zip(["nu", "mu", "m", "y"], [nu, mu, m, y]):
        print(f"{' '*3}{fx}(x) = {fun.__str__()}")
        for x in np.linspace(0, L, num=5, endpoints=True):
            print(f"{' '*6}@ x = {x} m: {fun(x):.7f}")
    