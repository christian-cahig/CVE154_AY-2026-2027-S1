"""
CVE154 (A.Y. 2026-2027, S1)
Programming Activity No. 04 - Bender than that

Prepared by Christian Cahig[cite: 4]
This file belongs to the repository https://github.com/christian-cahig/CVE154_AY-2026-2027-S1.[cite: 4]
"""

# Import Python's built-in math module under the alias 'mt' as required[cite: 6]
import math as mt
# Import SciPy's optimize module under the alias 'spo' as required[cite: 6]
import scipy.optimize as spo
# Import the NumPy library under the alias 'np' as required[cite: 6]
import numpy as np

# Store the required string "Group N" into the special __AUTHOR__ variable[cite: 6]
__AUTHOR__ = "Group 1"

# ==========================================
# Part 1. Core
# ==========================================

# Define a function to compute the vertical support reaction at A[cite: 6]
def Ay(wL, wR, L):
    # Derived using static equilibrium (Sum of moments about B = 0)[cite: 5, 6]
    # The distributed load q(x) = wL - ((wL + wR)/L)*x[cite: 5, 6]
    return -L * (2 * wL - wR) / 6.0

# Define a function to compute the vertical support reaction at B[cite: 6]
def By(wL, wR, L):
    # Derived using static equilibrium (Sum of moments about A = 0)[cite: 5, 6]
    return -L * (wL - 2 * wR) / 6.0

# Define a helper function to evaluate a polynomial's value and its derivative[cite: 6]
# It accepts a list of coefficients (ascending order a0 to an) and a value s[cite: 6]
def polyvalder(coeffs, s):
    # Initialize the polynomial value with the first coefficient (a_0)
    val = coeffs[0]
    # Initialize the derivative value as 0.0 (the derivative of a constant is 0)
    der = 0.0
    
    # Initialize the current power of s (s^1)
    s_pow = s
    # Initialize the previous power of s (s^0 = 1.0) for the derivative calculation
    s_pow_minus_1 = 1.0
    
    # Loop through the remaining coefficients starting from index 1[cite: 6]
    for i in range(1, len(coeffs)):
        # Add the current polynomial term (a_i * s^i) using only addition and multiplication[cite: 6]
        val = val + coeffs[i] * s_pow
        # Add the derivative of the current term (a_i * i * s^(i-1))[cite: 6]
        der = der + coeffs[i] * i * s_pow_minus_1
        
        # Update s_pow_minus_1 to the current s_pow for the next loop iteration
        s_pow_minus_1 = s_pow
        # Multiply s_pow by s to incrementally get the next higher power (s^(i+1))[cite: 6]
        s_pow = s_pow * s
        
    # Return the evaluated value and derivative as a NumPy array[cite: 6]
    return np.array([val, der])

# Define a function to compute internal shear and its derivative at location x[cite: 6]
def nu(x, wL, wR, L):
    # The shear equation is the integral of the load function plus Ay[cite: 5, 6]
    # nu(x) = Ay + wL*x - ((wL + wR) / (2*L)) * x^2
    # Define the coefficients array for [a_0, a_1, a_2]
    coeffs = [Ay(wL, wR, L), wL, -(wL + wR) / (2 * L)]
    # Evaluate and return using the polyvalder helper function[cite: 6]
    return polyvalder(coeffs, x)

# Define a function to compute bending moment and its derivative at location x[cite: 6]
def mu(x, wL, wR, L):
    # The moment equation is the integral of the shear function[cite: 6]
    # mu(x) = 0 + Ay*x + (wL/2)*x^2 - ((wL + wR) / (6*L)) * x^3
    # Define the coefficients array for [a_0, a_1, a_2, a_3]
    coeffs = [0.0, Ay(wL, wR, L), wL / 2.0, -(wL + wR) / (6 * L)]
    # Evaluate and return using the polyvalder helper function[cite: 6]
    return polyvalder(coeffs, x)

# Define a function to compute the slope and its derivative at location x[cite: 6]
def m(x, wL, wR, L):
    # The integration constant C1 is derived from the boundary conditions y(0)=0 and y(L)=0[cite: 5, 6]
    # Avoiding the ** operator here as well just to be perfectly safe with the constraints[cite: 6]
    c1 = (L * L * L * (8 * wL - 7 * wR)) / 360.0
    
    # The slope equation is the integral of the moment function (assuming EI = 1)[cite: 6]
    # m(x) = C1 + 0*x + (Ay/2)*x^2 + (wL/6)*x^3 - ((wL + wR) / (24*L)) * x^4
    # Define the coefficients array for [a_0, a_1, a_2, a_3, a_4]
    coeffs = [c1, 0.0, Ay(wL, wR, L) / 2.0, wL / 6.0, -(wL + wR) / (24 * L)]
    # Evaluate and return using the polyvalder helper function[cite: 6]
    return polyvalder(coeffs, x)

# Define a function to compute deflection and its derivative at location x[cite: 6]
def y(x, wL, wR, L):
    # The same integration constant C1 derived from the boundary conditions[cite: 5, 6]
    c1 = (L * L * L * (8 * wL - 7 * wR)) / 360.0
    
    # The deflection equation is the integral of the slope function (assuming EI = 1)[cite: 6]
    # y(x) = 0 + C1*x + 0*x^2 + (Ay/6)*x^3 + (wL/24)*x^4 - ((wL + wR) / (120*L)) * x^5
    # Define the coefficients array for [a_0, a_1, a_2, a_3, a_4, a_5]
    coeffs = [0.0, c1, 0.0, Ay(wL, wR, L) / 6.0, wL / 24.0, -(wL + wR) / (120 * L)]
    # Evaluate and return using the polyvalder helper function[cite: 6]
    return polyvalder(coeffs, x)


# ==========================================
# Part 2. Synthesis
# ==========================================

# Ensure this block is left unmodified per the instructions for the in-person activity[cite: 6]
if __name__ == "__main__":
    wl, wr, L = 1, 7, 1
    print(f"wL = {wl} N/m; wR = {wr} N/m; L = {L} m")
    print(
        f"{' '*3}Ay: {Ay(wl, wr, L):.7f}",
        f"By: {By(wl, wr, L):.7f}",
        sep="\t"
    )
    for x in np.linspace(0, L, num=5, endpoint=True):
        print(f"{' '*3}@ x = {x} m")
        for fun in [nu, mu, m, y]:
            v, dv = fun(x, wl, wr, L)
            print(
                f"{' '*6}{fun.__name__}: {v:.7f}",
                f"{fun.__name__+"'"}: {dv:.7f}",
                sep="\t"
            )
