"""Breaking the 4:1:1 hierarchy: what additional structure is needed."""
from pathlib import Path
import json
import math
import numpy as np

ROOT = Path(__file__).resolve().parents[1]

# The S4 x S4 x S4 subgroup gives a 2+1 mass pattern (4:1:1).
# Full S12 gives 1:1:1 (completely degenerate).
# The fibration phases are unitary and don't split eigenvalues.

# What breaks the degeneracy and gives the full hierarchy?

# Candidate: Gram entries between different S4 irrep types might differ
# because the WREATH PRODUCT structure of S12 is more complex than S4 x S4 x S4.

# S12 contains S4 wr S3 (the wreath product) as a maximal subgroup,
# not just the direct product S4 x S4 x S4.
# The wreath product S4 wr S3 ALSO permutes the three S4 blocks among themselves,
# not just acting within each block.

# Under S4 wr S3 acting on 12 points:
# Points within the same S4 block have MORE correlations:
# - G_self (same gen, same point) = ...
# - G_same_gen (same gen, diff point) = ...
# - G_diff_gen_diff_block (diff gen) = ...
# - G_diff_gen_same_block (S3 permutes the blocks) = ???

# The wreath product S4 wr S3 has |S4|^3 * |S3| = 24^3 * 6 = 82944 elements.
# Under this action:
# - Self: |Stab| = 6*6*6*1? No, = ...
# Let me compute properly.

# S4 wr S3 = (S4 x S4 x S4) semidirect S3
# where S3 permutes the three S4 factors.

# For a point (gen=r, type=t):
# Self: stabilizer in S4 wr S3
# = S3 x S3 x S3 (three S3 stabilizers, one per S4, for the point type)
#   but S3 also permutes the blocks
# = Actually: need sigma_r(t) = t, and if r is acted on by S3,
#   then sigma_sec(r)(t) = t as well.
# This is more complex.

# Let me just compute numerically.

# We can't compute the wreath product action easily without group theory library.
# But we can reason about the structure.

# The wreath product S4 wr S3 adds S3 permutations of the three generations.
# This gives:
# - Same gen, same point: same as before (3456)
# - Same gen, diff point: same as before (1152)
# - Different gen, SAME block (S3 permutes gen blocks): 
#   The S3 acts on the block labels. The entry between (gen1, type_a) and (gen2, type_a)
#   gets contributions from S3 elements that swap the blocks.
#   This should ADD to the previous cross-gen entry (576).

# So the wreath product gives LARGER cross-gen entries than the direct product.
# This DECREASES the hierarchy (makes cross-gen couplings stronger),
# which is the WRONG direction.

# The hierarchy comes from SUBGROUP structure, not larger group structure.
# Larger groups give more symmetry, more degeneracy.

# So we need to break the symmetry FURTHER, not restore it.
# This means breaking S4 x S4 x S4 to a smaller subgroup.

# The next subgroup: S4 x S4 x S4 -> S3 x S3 x S3 x U(1)^3?
# S3 is the stabilizer of a point, giving SU(3) color.
# Each S3 acts on the 3 remaining points within a generation.

# Under S3 x S3 x S3 (the color stabilizers):
# Points within the same generation but different types are in the same S3 orbit.
# Points of the same type across generations are in different S3 orbits.

# The Gram under S3 x S3 x S3:
# - S3 on 3 points: G_self = (3-1)! = 2, G_off = (3-2)! = 1
# - Each S3 factor has 6 elements
# |S3^3| = 6^3 = 216

# For the full 12-point carrier under S3^3:
# Self: stabilized by S2 x S3 x S3 = 2 * 6 * 6 = 72
# Same S3 factor (same gen, diff type): 1 * 6 * 6 = 36
# Different S3 factor: 0 (the S3 of gen1 doesn't act on points in gen2)

# Wait - if we're using S3 x S3 x S3, the Gram between different generations
# is ZERO (S3 of gen i doesn't move points in gen j).
# This would give a DIAGONAL Gram with NO cross-generation mixing - no CKM!

# So we need the FULL S12 (or at least cross-generation couplings via the
# wreath product) for mixing to exist at all.

# The hierarchy puzzle:
# 1. We need cross-generation couplings (for CKM mixing)
# 2. Cross-generation couplings reduce the hierarchy
# 3. We need a LARGE hierarchy (4:1:1 -> 136000:1)
# 4. Cross-gen couplings must be SMALL relative to same-gen couplings

# The ratio G_cross/G_same = 576/1152 = 0.5 under S4 x S4 x S4
# This gives the 4:1:1 pattern.

# Observed: m_t : m_c : m_u ~ 173 : 1.27 : 0.002
# The mass matrix eigenvalues are:
# heavy ~ m_t, light1 ~ m_c, light2 ~ m_u
# To get m_c >> m_u, the two light eigenvalues must be split.
# This requires the mass matrix to not have the symmetric J_3 structure.

# A symmetric matrix M = a*I + b*(J - I) has eigenvalues a+2b, a-b, a-b.
# The eigenvalues are split 2+1, not 3-tier.
# To get 3 distinct eigenvalues, we need the off-diagonals to be DIFFERENT.

# M = [a, b, c; b, a, d; c, d, a]
# with b != c != d
# Then eigenvalues split into 3 distinct values.

# So we need DIFFERENT cross-gen couplings between (1,2), (1,3), (2,3).

print("=== Breaking the 4:1:1 symmetry ===")
print()
print("The S4 x S4 x S4 subgroup gives a symmetric Gram with")
print("equal cross-gen couplings (576) between all pairs.")
print()
print("To get the observed hierarchy (m_t >> m_c >> m_u):")
print("  - G_cross_12, G_cross_13, G_cross_23 must be DIFFERENT")
print("  - The ratios between them must give the mass splitting")
print()
print("Candidate: the FULL S12 Gram projected onto the three generations")
print("gives OFF-DIAGONAL Gram entries that depend on the IRREP PAIRING")
print("between the fermion types, not just on the generation indices.")
print()

# For the up-type mass matrix: coupling between u_R (1_b) and Q_L (2) 
# For the down-type mass matrix: coupling between d_R (1_a) and Q_L (2)
# These are DIFFERENT 3x3 blocks of the 12x12 Gram.

# Under S12 (not the subgroup), the Gram entry for ANY pair of distinct
# points is 10!. So the up-type and down-type submatrices have IDENTICAL
# entries. No distinction.

# Under S4 x S4 x S4: any cross-generation Gram entry is 576 regardless
# of which irrep pair. Again identical.

# So the base Gram doesn't distinguish between up-type and down-type.
# The distinction must come from the FIBRATION PHASES.
# But phases are unitary and don't change eigenvalues!

# UNLESS: the phases for up-type and down-type involve not just a unitary
# transformation but a NON-HERMITIAN scaling (like the Yukawa coupling).

# In the SM: the mass matrix M = Y * v, where Y is the Yukawa coupling.
# Y is NOT Hermitian in general. M M^dag is Hermitian but M is not.
# The Gram is Hermitian. The Yukawa matrix is not.
# So M is NOT the Gram itself, but a non-Hermitian transformation of it.

print("=== Key insight ===")
print("The Gram is Hermitian. The mass matrix M = Y*v is NOT Hermitian.")
print("M^dag M is Hermitian but M itself is not.")
print("The Yukawa matrix Y is a NON-HERMITIAN deformation of the Gram.")
print()
print("The hierarchy comes from the Yukawa coupling pattern:")
print("  M_up = G * D_up   where D_up is a non-unitarian diagonal scaling")
print("  M_down = G * D_down  (different scaling)")
print()
print("The diagonal scalings D_up = diag(y_u, y_c, y_t) and")
print("D_down = diag(y_d, y_s, y_b) break the Gram's symmetric structure")
print("and split the eigenvalues into the full 3-tier hierarchy.")
print()

# The Yukawa couplings (running at mu = m_Z):
# y_t ~ 1.0, y_c ~ 0.007, y_u ~ 0.000013
# y_b ~ 0.025, y_s ~ 0.00055, y_d ~ 0.000028

y_t, y_c, y_u = 1.0, 0.007, 0.000013
y_b, y_s, y_d = 0.025, 0.00055, 0.000028

print("Yukawa couplings (top:charm:up):")
print(f"  y_t : y_c : y_u = {y_t:.0f} : {y_c/y_u:.0f} : {y_u:.6f}")
print(f"  y_b : y_s : y_d = {y_b:.3f} : {y_s:.5f} : {y_d:.6f}")
print()
print("These are NOT determined by the carrier geometry.")
print("They are the free parameters of the flavor sector in the SM.")
print("The carrier framework reproduces their FORM (3x3 matrix, CKM structure)")
print("but not their VALUES.")
print()

# The ratio y_t/y_c ~ 143, y_c/y_u ~ 538
# These ratios might be related to the S4 character values or Gram eigenvalue ratios

print("Yukawa ratios:")
print(f"  y_t / y_c = {y_t/y_c:.0f}")
print(f"  y_c / y_u = {y_c/y_u:.0f}")
print(f"  y_t / y_u = {y_t/y_u:.0f}")
print()

# The Gram eigenvalue ratio from S4 is 12/4 = 3
# The Gram ratio G_self/G_off = 11
# The subgroup Gram ratio G_same/G_cross = 2
# These don't match the Yukawa ratios (143, 538)

# BUT: the Yukawa ratios might come from the Gram eigenvalues of the
# FULL 12x12 S12 Gram, not the subgroup.

# S12 Gram eigenvalues: 79833600 (multiplicity 1) and 36288000 (multiplicity 11)
# Ratio: 79833600/36288000 ≈ 2.2

# That's also not 143 or 538.

# The hierarchy is set by the Higgs Yukawa couplings, which are
# free parameters in the Standard Model. The carrier framework
# doesn't predict them.

print("=== Conclusion ===")
print("The 4:1:1 hierarchy from the subgroup Gram is broken to the")
print("full observed hierarchy by the NOND-HERMITIAN Yukawa couplings.")
print("These are free parameters in both the SM and the carrier framework.")
print()
print("The carrier framework predicts:")
print("  - The FORM: 3x3 mass matrix with CKM mixing from Gram misalignment")
print("  - The PATTERN: 2+1 heavy-light splitting from S4xS4xS4 subgroup")
print("  - The ROUGH SCALE: G_self / G_cross ~ 3456/576 = 6")
print()
print("It does NOT predict:")
print("  - The specific Yukawa ratios (y_t/y_c = 143, y_c/y_u = 538)")
print("  - These are the flavor puzzle, open in both SM and carrier framework")

result = {
    'schema': 'marici.nima.hierarchy_breakdown.v1',
    'classification': 'subgroup_Gram_gives_2_1_pattern_Yukawas_are_non_Hermitian_deformation',
    'subgroup_hierarchy_ratio': '4:1:1',
    'observed_ratio': '136000:1000:1',
    'yukawa_ratio_t_c': int(y_t/y_c),
    'yukawa_ratio_c_u': int(y_c/y_u),
    'status': 'The 2+1 mass pattern is from the subgroup Gram. The full 3-tier hierarchy requires the non-Hermitian Yukawa couplings, which are free parameters in both the SM and the carrier framework. The flavor puzzle remains open.',
}

out = ROOT / 'results/hierarchy-breakdown.json'
out.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(f"\n{json.dumps(result, indent=2)}")