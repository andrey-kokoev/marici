"""Compute Gram entries from S12 carrier geometry directly."""
from pathlib import Path
import json
import math
import itertools

ROOT = Path(__file__).resolve().parents[1]

# The 12-point carrier with S12 automorphism.
# We label the 12 points as: Gen1 = {0,1,2,3}, Gen2 = {4,5,6,7}, Gen3 = {8,9,10,11}
# Each 4-point block (generation) has S4 automorphism, with sub-types:
#   0, 4, 8  = 1_a (trivial of S4)  -> d_R^c, e_R^c
#   1, 5, 9  = 1_b (sign of S4)     -> u_R^c, nu_R^c
#   2, 6, 10 = 2 components (doublet of S4) -> Q_L, L_L components
#   3, 7, 11 = 2 components (doublet of S4)

# The Gram entries are determined by the S12 permutation action:
# G_ij = number of permutations sigma in S12 such that sigma(i) = j
# For i=j: (12-1)! = 11!
# For i!=j: (12-2)! = 10!

fact_11 = math.factorial(11)
fact_10 = math.factorial(10)

print("=== S12 Gram entries from carrier geometry ===")
print(f"G_ii (same point) = {fact_11} = 11!")
print(f"G_ij (i != j)     = {fact_10} = 10!")
print(f"Ratio G_ij/G_ii   = 1/11 = {1/11:.6f}")
print()

# Now restrict to S4 x S4 x S4 subgroup.
# Within a generation (S4 block): all off-diagonals are the same (fact_10).
# Between generations: also all off-diagonals are the same (fact_10).
# So the base Gram gives NO preferred mixing — all off-diagonals equal.

# The hierarchical mixing comes from the FIBRATION ROTATION:
# Each point i has a phase theta_i. The physical Gram is:
# G_physical_ij = G_ij * exp(i(theta_j - theta_i))

# For CKM: up-type and down-type quarks have DIFFERENT phases.
# The up and down Gram bases are related by the fibration phase difference.

# Let's assign phases to the 12 points:
# Within a generation, the 4 states have different phases:
#   theta_1a = 0  (trivial)
#   theta_1b = phi_s (sign, sterile phase)
#   theta_2a = phi_d1 (doublet component 1)
#   theta_2b = phi_d2 (doublet component 2)
# Different generations have their own phase shifts.

# The CKM matrix comes from comparing the up-type and down-type quarks.
# In our assignment:
#   u_R is in 1_b (sign) 
#   d_R is in 1_a (trivial)
#   Q_L (u_L, d_L) is in 2 (doublet)

# The mass matrix for up-type couples u_R (1_b) to Q_L (2_doublet):
# G_up = G_base * exp(i(theta_1b - theta_2))
# For down-type: G_down = G_base * exp(i(theta_1a - theta_2))

# The CKM = eigenvector difference between G_up and G_down
# This depends ONLY on the phase difference (theta_1b - theta_1a) within each generation
# and the different phase assignments across generations.

# Let's assign generation-dependent phases:
# Gen 1: theta_1a = 0,     theta_1b = delta_g1
# Gen 2: theta_1a = 0,     theta_1b = delta_g2  
# Gen 3: theta_1a = 0,     theta_1b = delta_g3
# The relative phases between generations give the mixing.

print("=== CKM from fibration rotation phases ===")
print("The base Gram gives equal off-diagonals.")
print("CKM arises from the fibration phase difference between")
print("1_a (trivial, down-type) and 1_b (sign, up-type) states.")
print()

# The 3x3 Gram for the UP sector connects 1_b (u_R) states across 3 generations.
# G_up has diagonal = fact_11, off-diagonal = fact_10 * exp(i(delta_gi - delta_gj))
# For the DOWN sector: 1_a states have zero phase, so G_down has all off-diagonals = fact_10 (real)

# The DOWN sector Gram is symmetric (all phases zero):
# G_down = diag(fact_11) + offdiag(fact_10)
# Its eigenvectors are the same for any symmetric matrix with equal off-diagonals.

# The UP sector Gram has phase-dependent off-diagonals:
# G_up = diag(fact_11) + offdiag(fact_10 * exp(i(delta_gi - delta_gj)))

# The CKM comes from eigenvector misalignment between G_down and G_up.
# G_down has eigenvectors: one uniform (1,1,1)/sqrt(3) and two orthogonal.
# G_up has eigenvectors rotated by the phases.

# For phases delta_g = [delta_g1, delta_g2, delta_g3]:
# The mixing angles are determined by the phase differences.

# In the limit of small phases: theta_12 ~ |delta_g1 - delta_g2|
#                              theta_23 ~ |delta_g2 - delta_g3|
#                              theta_13 ~ |delta_g1 - delta_g3|

# Observed CKM angles: theta_12 ~ 0.227 rad (13.0 deg)
#                       theta_23 ~ 0.041 rad (2.35 deg)
#                       theta_13 ~ 0.0036 rad (0.49 deg)

# These phase differences are:
# |delta_g1 - delta_g2| = theta_12 * fact_10 / fact_11 * correction
# Actually, for small phases, the mixing angle is directly the phase difference
# in the off-diagonal entries.

# Let me compute numerically.

import numpy as np

fact_11 = 39916800  # 11!
fact_10 = 3628800  # 10!

# Base Gram (same for up and down without phases)
G_base = np.ones((3, 3)) * fact_10 + np.diag([fact_11 - fact_10] * 3)
# Normalize: divide by fact_10
G_base_norm = np.ones((3, 3)) + np.diag([10] * 3)

# For the DOWN sector: all phases zero
G_down = G_base_norm.copy()

# For the UP sector: off-diagonal phases = delta_gi - delta_gj
# Given observed CKM angles, find the implied phase differences

# From CKM angles (in rad):
theta12 = 0.227  # 13.0 deg
theta23 = 0.041  # 2.35 deg
theta13 = 0.0036  # 0.49 deg

# The CKM matrix (absolute values):
ckm = np.array([
    [0.974, 0.225, 0.0036],
    [0.225, 0.973, 0.041],
    [0.0086, 0.040, 0.999]
])

# The phase differences that produce these mixing angles:
# For a 3x3 Gram with equal diagonal and small off-diagonal phases,
# the mixing angle ij ~ |phase_i - phase_j| * (off_diag / diag)

# G_up_ij / G_up_ii = exp(i(delta_gi - delta_gj)) * fact_10 / fact_11
#                   = exp(i(delta_gi - delta_gj)) / 11

# The mixing comes from the imaginary part of G_up:
# Im(G_up_ij) = sin(delta_gi - delta_gj) * fact_10
# Re(G_up_ij) = cos(delta_gi - delta_gj) * fact_10

# For small phase differences: sin(dphi) ~ dphi
# The mixing angle ~ Im(G_up_ij) / (G_ii - G_jj + Re(G_up_ij)) ~ dphi / 11

# This gives dphi ~ 11 * theta
delta_12 = 11 * theta12  # ~ 2.5 rad
delta_23 = 11 * theta23  # ~ 0.45 rad
delta_13 = 11 * theta13  # ~ 0.04 rad

print(f"Fibration phase differences from CKM:")
print(f"  delta_g1 - delta_g2 = {delta_12:.4f} rad = {math.degrees(delta_12):.1f} deg")
print(f"  delta_g2 - delta_g3 = {delta_23:.4f} rad = {math.degrees(delta_23):.1f} deg")
print(f"  delta_g1 - delta_g3 = {delta_13:.4f} rad = {math.degrees(delta_13):.1f} deg")
print()

# These phases define the fibration rotation between the 1_a (trivial) and 1_b (sign) states
# across the three S4 factors in S12.

# The full 12-point Gram with phases:
print("=== Full 12-point Gram with fibration phases ===")
print("The phases assign different internal U(1) angles to each carrier point.")
print("The physical Gram = base_Gram * exp(i(phase_j - phase_i))")
print("Particle masses = eigenvalues of the appropriate 3x3 submatrices.")
print("CKM/PMMS = eigenvector misalignment between up and down type submatrices.")
print()
print("The base Gram entries are fixed by S12 automorphism:")
print(f"  G_ii = {fact_11}")
print(f"  G_ij = {fact_10} for i != j")
print(f"  Ratio = 1/11 = {1/11:.6f}")
print()
print("The fibration phases are NOT determined by the carrier geometry alone.")
print("They are the degrees of freedom that break the S4 symmetry within each")
print("generation, producing the observed mass hierarchy and mixing pattern.")

result = {
    'schema': 'marici.nima.Gram_from_carrier_geometry.v1',
    'classification': 'Gram_entries_fixed_by_S12_automorphism_fibration_phases_give_mixing',
    'base_Gram_same_point': fact_11,
    'base_Gram_off_diagonal': fact_10,
    'ratio': 1/11,
    'fibration_phase_differences_from_CKM_rad': {
        'delta_12': round(delta_12, 4),
        'delta_23': round(delta_23, 4),
        'delta_13': round(delta_13, 4),
    },
    'finding': 'The S12 carrier fixes the base Gram entries via the automorphism group action. All off-diagonals are equal (fact_10). The fibration rotation phases theta_i break the symmetry, giving different effective Gram entries for up-type vs down-type sectors. The CKM mixing angles determine the required phase differences between the 1_a (trivial) and 1_b (sign) states across the three generations. The phase differences are of order 2.5 rad, 0.45 rad, and 0.04 rad.',
}

out = ROOT / 'results/gram-from-carrier-geometry.json'
out.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(f"\n{json.dumps(result, indent=2)}")