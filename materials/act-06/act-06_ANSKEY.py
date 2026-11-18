"""
CVE154 (A.Y. 2026-2027, S1)
Template script for Programming Activity No. 06

Prepared by Christian Cahig

This file belongs to the repository
https://github.com/christian-cahig/CVE154_AY-2026-2027-S1.
"""

import math as mt
import numpy as np
import numpy.linalg as npla

__AUTHOR__ = "Group 21"

NUM_MEMBERS = 15; NUM_JOINTS = 9

def _get_rlengths():
    """Member lengths as multiples of D"""
    # Sequence of members
    #   IG, IH,
    #   GH,
    #   GD, GE, HE, HF,
    #   DE, EF,
    #   DA, DB, FB, FC,
    #   AB, BC
    _ov3 = 1 / 3; _2ov3 = 2 * _ov3
    _rt10 = mt.sqrt(10); _rt10ov3 = _rt10 * _ov3
    _rt13ov3 = mt.sqrt(13) * _ov3
    
    return [
        _rt10ov3, _rt10ov3,
        _2ov3,
        _rt10ov3, _rt10ov3, _rt10ov3, _rt10ov3,
        _2ov3, _2ov3,
        _rt10ov3, _rt13ov3, _rt13ov3, _rt10ov3,
        1, 1
    ]

def _get_rjcoords():
    """Coordinates of joints as multiples of D"""
    # Sequence of joints: A, B, ..., H, I
    _ov3 = 1 / 3
    return [
        [0, 0],
        [1, 0],
        [2, 0],
        [_ov3, 1],
        [1, 1],
        [5 * _ov3, 1],
        [2 * _ov3, 2],
        [4 * _ov3, 2],
        [1, 3],
    ]

def _get_incidence():
    """Members as tuples of joint indices"""
    # Sequence of members
    #   IG, IH,
    #   GH,
    #   GD, GE, HE, HF,
    #   DE, EF,
    #   DA, DB, FB, FC,
    #   AB, BC
    return [
        (6, 8), (7, 8),
        (6, 7),
        (3, 6), (4, 6), (4, 7), (5, 7),
        (3, 4), (4, 5),
        (0, 3), (1, 3), (1, 5), (2, 5),
        (0, 1), (1, 2)
    ]

def _get_rxns(D, Fh, Fv, Mc):
    """Support reactions at joints"""
    # Sequence of joints: A, B, ..., H, I
    jcoords = D * np.array(_get_rjcoords())
    Cy = ((Fh * jcoords[:, 1]).sum() - (Fv * jcoords[:, 0]).sum() - Mc.sum()) / jcoords[2, 0]
    Cx = -Fh.sum()
    Ay = -Fv.sum() - Cy

    Rx = [0 for i in range(NUM_JOINTS)]
    Ry = [0 for i in range(NUM_JOINTS)]
    Rx[2] = Cx; Ry[0] = Ay; Ry[2] = Cy

    return Rx, Ry

def _get_rweights():
    """Weights concentrated at joints, as multiples of γD"""
    # Sequence of joints: A, B, ..., H, I
    rlengths = _get_rlengths()
    return [
        (rlengths[-6] + rlengths[-2]) / 2,
        (rlengths[-2] + rlengths[-1] + rlengths[-4] + rlengths[-5]) / 2,
        (rlengths[-1] + rlengths[-3]) / 2,
        (rlengths[-6] + rlengths[-5] + rlengths[-8] + rlengths[3]) / 2,
        (rlengths[-8] + rlengths[-7] + rlengths[4] + rlengths[5]) / 2,
        (rlengths[-3] + rlengths[-4] + rlengths[-7] + rlengths[7]) / 2,
        (rlengths[0] + rlengths[2] + rlengths[3] + rlengths[4]) / 2,
        (rlengths[1] + rlengths[2] + rlengths[5] + rlengths[6]) / 2,
        (rlengths[0] + rlengths[1]) / 2
    ]

def build_Ab(D = 1, Fh = [], Fv = [], Mc = []):
    # Sequence of members
    #   IG, IH,
    #   GH,
    #   GD, GE, HE, HF,
    #   DE, EF,
    #   DA, DB, FB, FC,
    #   AB, BC
    # Sequence of joints: A, B, ..., H, I
    Fh = np.array(Fh) if (len(Fh) != 0) else np.zeros((NUM_JOINTS))
    Fv = np.array(Fv) if (len(Fv) != 0) else np.zeros((NUM_JOINTS))
    Mc = np.array(Mc) if (len(Mc) != 0) else np.zeros((NUM_JOINTS))

    # Support reactions
    Rxh, Rxv = _get_rxns(D, Fh, Fv, Mc)

    # Net forces (rightward, upward) at joints
    Hs = Fh + np.array(Rxh); Vs = Fv + np.array(Rxv)

    # Force-balance equations at joints
    #   [Ah; Av] x = [bh; bv]
    Ah = np.zeros((NUM_JOINTS, NUM_MEMBERS))
    Av = np.zeros((NUM_JOINTS, NUM_MEMBERS))
    bh = -Hs; bv = -Vs
    rjcoords = _get_rjcoords(); rlengths = _get_rlengths()
    for m, (f, t) in enumerate(_get_incidence()):
        rx = rjcoords[t][0] - rjcoords[f][0]
        ry = rjcoords[t][1] - rjcoords[f][1]
        cos_alfa = rx / rlengths[m]; cos_beta = ry / rlengths[m]
        Ah[f, m] = cos_alfa; Av[f, m] = cos_beta
        Ah[t, m] = -cos_alfa; Av[t, m] = -cos_beta

    # Trim down number of equations to m (number of members)
    # Remove equations corresponding to support reactions
    A = np.concat((Ah[:2], Ah[3:], Av[1:2], Av[3:]), axis=0)
    b = np.concat((bh[:2], bh[3:], bv[1:2], bv[3:]), axis=0)
    # Other alternative approaches. Be sure to try these for yourselves.
    # These often lead to determinants that are closer to zero
    # than those produced by the above strategy.
    #   1. Alternate equations for horizontal forces with those for vertical forces,
    #   then consider only m of those equations.
    # A = np.reshape(np.concat((Ah, Av), axis=1), (2*NUM_JOINTS, NUM_MEMBERS))[:NUM_MEMBERS, :]
    # b = np.concat((bh[:, None], bv[:, None]), axis=1).ravel()[:NUM_MEMBERS]
    #   2. If there are M horizontal reaction forces,
    #   remove M from the balance equations for horizontal forces.
    #   Similarly, if there are N vertical reactions,
    #   remove N from the balance equations for vertical forces.
    # A = np.concat((Ah[1:], Av[2:]), axis=0)
    # b = np.concat((bh[1:], bv[2:]), axis=0)
    #   3. Random combo
    # A = np.reshape(np.concat((Ah, Av), axis=1), (2*NUM_JOINTS, NUM_MEMBERS))
    # A = np.delete(A, [1, 2, 3], axis=0)
    # b = np.concat((bh[:, None], bv[:, None]), axis=1).ravel()
    # b = np.delete(b, [1, 2, 3], axis=0)
    #   4. Random combo
    # A = np.reshape(np.concat((Ah, Av), axis=1), (2*NUM_JOINTS, NUM_MEMBERS))[1:NUM_MEMBERS+1, :]
    # b = np.concat((bh[:, None], bv[:, None]), axis=1).ravel()[1:NUM_MEMBERS+1]

    return A, b

if __name__ == "__main__":
    CASES = {
        "0" : (9, 0),
        "1" : (3, 3),
        "2" : (4, 2),
        "3" : (5, 1)
    }

    CASE = 1
    D, gamma = CASES[str(CASE)]

    Fh = [0 for _ in range(NUM_JOINTS)]
    Fv = [0 for _ in range(NUM_JOINTS)]
    Mc = [0 for _ in range(NUM_JOINTS)]
    if CASE == 0:
        Fh[3] = 30; Fh[6] = 30; Fh[8] = 30
        Fv[-1] = -50
    else:
        Fh[0] = 5; Fh[3] = 6.7; Fh[6] = 8.3; Fh[8] = 10
        Fv = [v - (gamma * D * w) for v, w in zip(Fv, _get_rweights())]
        Mc = [0, -1.0, 0, 0, 3.0, 0, 0, 0, 0]

    A, b = build_Ab(D = D, Fh = Fh, Fv = Fv, Mc = Mc)
    x = npla.solve(A, b)

    __INDENT__ = ' ' * 3
    print(f"Case {CASE}: D = {D} m; γ = {gamma} N/m")
    print(f"{__INDENT__}det(A) = {npla.det(A)}")
    print(f"{__INDENT__}Κ(A): {npla.cond(A)}")
    print(f"{__INDENT__}Member forces (N):")
    print(f"{__INDENT__*2}AB = {x[13]}")
    print(f"{__INDENT__*2}BC = {x[14]}")
    print(f"{__INDENT__*2}AD = {x[9]}")
    print(f"{__INDENT__*2}BD = {x[10]}")
    print(f"{__INDENT__*2}BF = {x[11]}")
    print(f"{__INDENT__*2}CF = {x[12]}")
    print(f"{__INDENT__*2}DE = {x[7]}")
    print(f"{__INDENT__*2}EF = {x[8]}")
    print(f"{__INDENT__*2}DG = {x[3]}")
    print(f"{__INDENT__*2}EG = {x[4]}")
    print(f"{__INDENT__*2}EH = {x[5]}")
    print(f"{__INDENT__*2}FH = {x[6]}")
    print(f"{__INDENT__*2}GH = {x[2]}")
    print(f"{__INDENT__*2}GI = {x[0]}")
    print(f"{__INDENT__*2}HI = {x[1]}")