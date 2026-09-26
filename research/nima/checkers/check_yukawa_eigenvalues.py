"""
Compute Yukawa eigenvalues from fibration phases in the S12 carrier.
The three S4 copies (generations) have relative phases that determine
the exponential hierarchy between generations.
"""
import numpy as np
import math

r, l, s, c = 11, 12, 4, 10

# The Gram base matrix for one generation (4 states of S4)
# Under S4 decomposition: 4 = 1 + 1 + 2 (sign + sign' + standard)
# The overlaps between these states are given by the Gram numbers

def build_generation_gram():
    """Build the 4x4 Gram matrix for one S4 generation."""
    # The 4 states: singlet_a(t), singlet_b(u), doublet_c, doublet_d (up/down)
    # Overlaps are determined by the Gram numbers
    G = np.zeros((4, 4), dtype=complex)
    
    # Self-overlaps (diagonal) = G_self
    G_self = r * s  # 11 * 4 = 44, the self-overlap scale
    for i in range(4):
        G[i, i] = G_self
    
    # Cross-overlaps within same generation = G_cross
    # Different states within one S4 have overlaps determined by
    # the cube-root relations from the Gram characteristic polynomial
    G_cross = c  # 10, from U(1) trace
    for i in range(4):
        for j in range(4):
            if i != j:
                G[i, j] = G_cross
    
    return G

def build_cross_generation_gram(theta):
    """Build off-diagonal 4x4 blocks between generations with phase theta."""
    G = np.zeros((4, 4), dtype=complex)
    
    # Base cross-generation overlap = l  (12, the U(1) eigenvalue)
    G_base = l
    
    # Apply fibration phase
    phase = np.exp(1j * theta)
    for i in range(4):
        for j in range(4):
            G[i, j] = G_base * phase
    
    return G

def full_gram(theta12, theta23, theta31):
    """Build the full 12x12 Gram matrix for 3 generations."""
    G = np.zeros((12, 12), dtype=complex)
    
    # Diagonal blocks (same generation)
    G_gen = build_generation_gram()
    G[0:4, 0:4] = G_gen
    G[4:8, 4:8] = G_gen
    G[8:12, 8:12] = G_gen
    
    # Off-diagonal blocks (cross generation)
    G[0:4, 4:8] = build_cross_generation_gram(theta12)
    G[4:8, 0:4] = build_cross_generation_gram(-theta12)  # conjugate
    
    G[4:8, 8:12] = build_cross_generation_gram(theta23)
    G[8:12, 4:8] = build_cross_generation_gram(-theta23)
    
    G[0:4, 8:12] = build_cross_generation_gram(theta31)
    G[8:12, 0:4] = build_cross_generation_gram(-theta31)
    
    return G

def yukawa_eigenvalues(theta12, theta23):
    """Compute Yukawa eigenvalues given two fibration phases."""
    theta31 = -(theta12 + theta23)  # closure: sum to 0
    
    G = full_gram(theta12, theta23, theta31)
    
    # The Yukawa eigenvalues are the singular values of the Gram matrix
    # projected onto the fermion sector (the 6 left-handed x 6 right-handed space)
    # For simplicity, take eigenvalues of the full Gram
    eigenvals = np.sort(np.linalg.eigvalsh(G))[::-1]
    
    return eigenvals

print("=== YUKAWA EIGENVALUES FROM FIBRATION PHASES ===")
print()

# Scan over fibration phases and compute eigenvalues
print("Scanning fibration phases (0 to pi)...")
print()
print(f"{'theta12':>8} {'theta23':>8} {'ev1':>10} {'ev2':>10} {'ev3':>10} {'ev4':>10} {'ev5':>10} {'ev6':>10}")
print("-" * 70)

# Try specific phase values
phases_to_try = [
    (0, 0),           # No phases
    (0.1, 0.05),      # Small phases
    (0.5, 0.3),       # Medium phases
    (np.pi/3, np.pi/6),  # 60, 30 degrees
    (np.pi/4, np.pi/4),  # 45, 45 degrees
    (np.pi/2, np.pi/3),  # 90, 60 degrees
    (np.pi/2, np.pi/4),  # 90, 45 degrees
    (np.pi/2, np.pi/6),  # 90, 30 degrees
    (2*np.pi/3, np.pi/3), # 120, 60 degrees
    (np.pi/2, np.pi/2),  # 90, 90 degrees
]

for t12, t23 in phases_to_try:
    ev = yukawa_eigenvalues(t12, t23)
    print(f"{t12:8.3f} {t23:8.3f} {ev[0]:10.2f} {ev[1]:10.2f} {ev[2]:10.2f} {ev[3]:10.2f} {ev[4]:10.2f} {ev[5]:10.2f}")

# The Gram base ratios for the 3 generations:
# Up-type: l_U1 : r_S12 : C_U1 = 12 : 11 : 10
# Down-type: involves l_SU2
# The fibration phases multiply these base values

print()
print("Base ratios from Gram numbers:")
print(f"  Up-type generations: y_t : y_c : y_u = {l} : {r} : {c}")
print(f"  Down-type: y_b : y_s : y_d = {s} : {s*r//l} : {s*c//r} (approx)")

# Let's compute the actual eigenvalue ratios from a specific phase configuration
# and compare to observed Yukawa ratios

# Observed Yukawa couplings at M_Z (renormalized):
# y_t = 0.99, y_c = 0.007, y_u = 0.000013
# y_b = 0.024, y_s = 0.0005, y_d = 0.000025

print()
print("Comparing to observed Yukawas at M_Z:")
print(f"  y_t = 0.99, y_c = 0.007, y_u = 1.3e-5")
print(f"  y_b = 0.024, y_s = 5e-4, y_d = 2.5e-5")

# The fibration phases should produce the hierarchy
# y_t : y_c : y_u = 12*F1 : 11*F2 : 10*F3
# where F_i are the suppression factors from phases

# Let's find the phase that gives the correct ratio y_c/y_t = 0.007
# We need F2/F1 = (0.007/0.99) * (12/11) = 0.00707 * 1.09 = 0.0077

# For the Gram matrix, the SU(2) projection gives the 2:1:1 splitting
# and the phases determine the further splitting

print()
print("Fibration phase configuration from stationary condition:")
print("The capacity-weighted Grassmannian cost is minimized when")
print("the fibration phases satisfy the Gram consistency condition:")
print("  sum_i exp(i*theta_i) = 0  (balanced phases)")
print("  and |theta_ij| = 2pi/3 for the three generations")

# Check if 2pi/3 phases give the right ratios
t12 = 2*math.pi/3
t23 = 2*math.pi/3
ev = yukawa_eigenvalues(t12, t23)
print(f"{t12:8.3f} {t23:8.3f} {ev[0]:10.2f} {ev[1]:10.2f} {ev[2]:10.2f} {ev[3]:10.2f} {ev[4]:10.2f} {ev[5]:10.2f}")
print(f"  Eigenvalue ratios (top 3): {ev[0]/ev[0]:.3f} : {ev[1]/ev[0]:.4f} : {ev[2]/ev[0]:.4f}")
print(f"  Observed up-type: 1 : 0.007 : 1.3e-5")