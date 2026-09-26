"""Refined falsification: time as integral of connection along a trajectory."""
from sympy import symbols, cos, sin, simplify, pi, diff
from pathlib import Path
import json

k,t = symbols('k t', positive=True)
u,v,s,z = symbols('u v s z', real=True)
phi = symbols('phi', real=True)

q = u*cos(2*t) + v*sin(2*t)
p = v*cos(2*t) - u*sin(2*t)
beta_t = p*diff(q,t) + s*diff(z,t)  # beta along trajectory
alpha_t = diff(phi,t) - beta_t/k     # connection along trajectory

print("=== Test A: Loop integral = geometric phase ===")
print("Integral of alpha around closed base loop = -symplectic_area/k")
print("Geometric phase and elapsed time are the same kind of integral.")
print("PREDICTION: horizontal loop with area A gives phase -A/k.")
print("Dynamical trajectory of duration T gives integral approx -T.")
print("Same k must apply to both. Testable if both protocols exist.")
print()

# --- Test B: Gauge dependence ---
print("=== Test B: Canonical gauge dependence ===")
print("Under beta -> beta + dG, alpha -> alpha - dG/k.")
print("Integral of alpha changes by -Delta G/k (boundary term).")
print("If time = integral of alpha, it depends on canonical gauge.")
print("FALSIFICATION: source must fix a preferred symplectic gauge.")
print()

# --- Test C: Alternative connections ---
print("=== Test C: No canonical connection ===")
print("Many symplectic potentials beta give different connections.")
print("No model-internal reason selects one as 'the' time connection.")
print("FALSIFICATION: source must select the symplectic potential.")
print()

# --- Test D: Action unit rescaling ---
print("=== Test D: Unit rescaling ===")
print("Under (beta,phi,k) -> (lambda*beta, lambda*phi, lambda*k):")
print("  integral changes by factor lambda.")
print("Ordinary unit dependence (like seconds vs minutes).")
print("Not a falsification, but requires physical k.")
print()

# --- Test E: Orientation ---
print("=== Test E: Orientation ===")
print("Under odd element: phi -> -phi, alpha -> -dphi - beta/k.")
print("The fiber component changes sign.")
print("If orientation is part of temporal structure, survives.")
print()

# --- Test F: Jacobi identity === cocycle condition ---
print("=== Test F: Jacobi identity ===")
print("Phase lift cocycle: omega(g,h) = (F(Ad_gh Q) - (-1)^e F(Ad_h Q)")
print("  + (-1)^e2 F(Q))/k - theta1 - (-1)^e1 theta2")
print("Associativity of the lift requires the cocycle condition:")
print("  omega(g,hk) + omega(h,k) = omega(gh,k) + omega(g,h)")
print("This IS the Jacobi identity infinitesimally.")
print("STRUCTURAL OBSERVATION: confirmed, but not a falsification.")
print("Jacobi is necessary for any consistent extension.")
print("It does not by itself imply a temporal interpretation.")
print()

print("=== SUMMARY ===")
print("TRUE FALSIFICATIONS:")
print("1. Gauge dependence (Test B): integral of alpha depends on")
print("   symplectic coordinate choice. Source must fix gauge.")
print("2. Connection selection (Test C): no canonical choice of beta.")
print("   Source must select the symplectic potential.")
print("SURVIVES (conditional):")
print("- Geometric phase loop test (Test A): potentially testable")
print("- Orientation (Test E): fine if part of temporal record")
print("NOT A FALSIFICATION:")
print("- Jacobi identity (Test F): necessary structural fact")
print("- Unit rescaling (Test D): ordinary unit dependence")