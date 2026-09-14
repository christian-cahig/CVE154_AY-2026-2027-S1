
import math

AUTHOR = "Group 5" 


def split_load(u, x, P):
    points = [0, P, 2 * P, 3 * P, 4 * P]
    loads = [0, 0, 0, 0, 0]

    panel = min(int(x // P), 3)
    left_point = points[panel]
    right_point = points[panel + 1]

    loads[panel] = u * (right_point - x) / P
    loads[panel + 1] = u * (x - left_point) / P

    return loads 


def reactions(u, x, P=10, H=15):
    R_A, R_B, R_C, R_D, R_E = split_load(u, x, P)

    Ay = (H * R_A + (H - P) * R_B) / H

    Ey = u - Ay

    Em = u * x - 4 * P * Ey

    Fy = abs(Ay - R_A - R_B)

    mu_G = Ay * 2.5 * P - R_A * 2.5 * P - R_B * 1.5 * P - R_C * 0.5 * P

    return {"Ay": Ay, "Ey": Ey, "Em": Em, "Fy": Fy, "mu_G": mu_G}


if __name__ == "__main__":
    u = 5   # load magnitude (kip)
    x = 20  # load location (ft)
    P = 20   # panel length (ft)
    H = 20.1   # hinge location (ft)

    r = reactions(u, x, P, H)

    print(AUTHOR)
    print(f"u={u} kip, x={x} ft, P={P} ft, H={H} ft")
    print("-" * 50)
    for name, value in r.items():
        print(f"{name:5} = {value:.3f}")

    print("-" * 50)
    print("Check ΣFy:", r["Ay"] + r["Ey"] - u)
    print("Check ΣM_A:", 4 * P * r["Ey"] + r["Em"] - u * x)
