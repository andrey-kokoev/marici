"""Derive mass hierarchy from S4 x S4 x S4 subgroup Gram structure."""
from pathlib import Path
import json
import math
import numpy as np

ROOT = Path(__file__).resolve().parents[1]

# The 12-point carrier: 3 generations × 4 states per generation.
# Subgroup H = S4 × S4 × S4 acts on each generation independently.

# Gram entries under H:
# - Same point (i=j, same gen, same state): |H|_self
# - Same gen, different point: |H|_same_gen  
# - Different gen: |H|_cross_gen

# |H| = |S4|^3 = 24^3 = 13824

# For a state (gen=i, state_type=t) in the 12-point carrier:
# Self: stabilized by S3 × S4 × S4  (|S3| = 6)
# Same gen, different state: stabilized by S1??? Actually different:
#   For point i (type a) and point j (type b) in same S4:
#   Need sigma(a)=b and sigma arbitrary on other 2 points, 
#   then all of the other two S4's are free.
#   |S4|^2 * |S3| = 576 * 6 = 3456? Wait, S3 is the stabilizer of which?

# Let me compute properly.
# In S4 acting on 4 points {0,1,2,3}:
# |{sigma in S4 : sigma(0)=0}| = |S3| = 6 (fixes point 0)
# |{sigma in S4 : sigma(0)=1}| = |S3| = 6 (maps 0 to 1, then permutes {1,2,3}... wait)

# For sigma(0)=1: sigma sends 0 to 1. The remaining 3 points {1,2,3} 
# can be permuted arbitrarily among the 3 points {0,2,3}. 
# This is |S3| = 6.

# So for S4 on 4 points:
# |{sigma: sigma(0)=0}| = 6 (fixes 0)
# |{sigma: sigma(0)=1}| = 6 (maps 0 to 1)

# They're ALL 6! Because for any i, j, the number of permutations sending i to j is (4-1)! = 3! = 6.

# For the 4-point carrier:
# G_ii (same point) = (4-1)! = 6
# G_ij (i != j) = (4-2)! = 2

# For the full S12 action:
# G_ii = (12-1)! = 11! = 39916800
# G_ij = (12-2)! = 10! = 3628800 (for ALL i != j, regardless of generation)

# So for S12, ALL off-diagonals are equal. No generation structure visible.

# For the SUBGROUP H = S4 x S4 x S4:
# H has |H| = 24^3 = 13824 elements acting on 12 points.

# For a point (gen=r, type=t):
# Self (same gen, same type):
# |{h in H : h(r,t) = (r,t)}| = |S4| for the gen r that fixes t, times |S4| x |S4| for the other two
# = 6 x 24 x 24 = 3456

# Same gen, different type:
# |{h in H : h(r,t1) = (r,t2), t1 != t2}| = 2 x 24 x 24 = 1152
# (since in S4, |{sigma: sigma(t1)=t2}| = (4-2)! = 2)

# Different gen:
# |{h in H : h(r1,t1) = (r2,t2), r1 != r2}| 
# = |S4| x 1 x |S4| = 24 x 1 x 24 = 576
# (need sigma_{r1}(t1) = t2, and sigma_{r2} free, other gen free)

# So the Gram under H has THREE distinct values:
# G_self = 3456
# G_same_gen = 1152
# G_cross_gen = 576

# Ratios: 3456 : 1152 : 576 = 6 : 2 : 1

print("=== Gram entries under S4 x S4 x S4 subgroup ===")
print(f"|S4| = 24")
print(f"|H| = |S4^3| = {24**3}")
print()

print("Gram submatrix entries:")
print(f"  Same point (self):       G_self = {6 * 24 * 24} = 6|S4|^2 = 3456")
print(f"  Same gen, diff type:     G_same = {2 * 24 * 24} = 2|S4|^2 = 1152")
print(f"  Different gen:           G_cross = {1 * 24 * 24} = |S4|^2 = 576")
print(f"  Ratio self:same:cross = 3456:1152:576 = 6:2:1")
print()

# The 3x3 mass matrix for a specific fermion type across 3 generations:
# Diagonal: connects states within the same generation -> G_same_gen = 1152
# Off-diagonal: connects states across generations -> G_cross_gen = 576

# Let's construct the 3x3 mass matrix
G_self = 3456
G_same = 1152
G_cross = 576

# The mass matrix for a given fermion type:
# M_ij = G_same if i=j, G_cross if i!=j
# (for up-type: connecting u_R of gen i to Q_L of gen j)
# (for down-type: connecting d_R of gen i to Q_L of gen j)

M = np.array([
    [G_same, G_cross, G_cross],
    [G_cross, G_same, G_cross],
    [G_cross, G_cross, G_same]
])

evals = np.linalg.eigvalsh(M)
print("Mass matrix (base, no phases):")
print(M)
print(f"Eigenvalues: {sorted(evals, reverse=True)}")
print(f"  Heavy (top-like):  {evals[2]:.0f}")
print(f"  Medium (charm-like): {evals[1]:.0f}")  
print(f"  Light (up-like):   {evals[0]:.0f}")
print()

# The mass hierarchy from base Gram alone:
# One heavy generation at G_same + 2*G_cross = 1152 + 1152 = 2304
# Two light generations at G_same - G_cross = 1152 - 576 = 576
# Ratio: 2304 : 576 : 576 = 4 : 1 : 1

heavy = G_same + 2*G_cross
light = G_same - G_cross
print(f"Base mass ratio: {heavy}:{light}:{light} = {heavy/light:.0f}:1:1")
print(f"Observed: m_t:m_c:m_u ~ 173:1.27:0.002 = 136220:1000:1.6 (much more hierarchical)")
print()

# The hierarchy is not enough from the base Gram alone.
# The fibration phases (with their different assignments for up vs down)
# break the degeneracy between 1st and 2nd generation.
# The Higgs Yukawa mechanism gives the overall scale.

# With phases: each M_ij -> M_ij * exp(i(phi_j - phi_i))
# The eigenvalues become complex and can split further.
# For the mass eigenvalues to split into 3 distinct values (not 2+1),
# the off-diagonal phases must break the symmetry.

# With phases: phi_1, phi_2, phi_3
# M_phases_ij = M_ij * exp(i(phi_j - phi_i))
# This is a unitary transformation of M, so eigenvalues are REAL and SAME as M!

# Wait - U = diag(exp(i*phi_1), exp(i*phi_2), exp(i*phi_3))
# M_phases = U M U^dag
# This DOES NOT change eigenvalues (unitary transformation).

# So the phases alone cannot split the eigenvalues further!
# Something else is needed.

# What if the phase DIFFERENCES affect not just the eigenvectors
# but also the magnitude of the off-diagonals?

# For the CKM: the UP and DOWN sectors have DIFFERENT phase configurations.
# The CKM = V_up^dag V_down where V_up diagonalizes M_up and V_down diagonalizes M_down.
# M_up and M_down are the SAME matrix M (same eigenvalues).
# Their eigenvectors are related by the phase transformation U_up and U_down.

# So CKM = U_up^dag * U_down? No, eigenvectors of the same matrix M
# are related by the degeneracy. Since M has degenerate eigenvalues
# (576, 576, 2304), its eigenvectors are not uniquely defined - any
# rotation in the 2D degenerate subspace (576, 576) gives valid eigenvectors.

# The phases break this degeneracy by picking specific eigenvectors.
# The CKM matrix IS the rotation between the eigenvectors picked by
# the up-type phases and the down-type phases.

# But the eigenvalues remain: heavy = 2304, light = 576 (two degenerate copies).
# This means m_t:m_c:m_u = 2304:576:576 = 4:1:1.
# The top is heavier, but charm and up are degenerate.
# The observed hierarchy requires charm >> up, not charm = up.

# So the base Gram under S4xS4xS4 gives the right FORM (3 generations with 1 heavy, 2 light)
# but the wrong DETAILS (charm/up degenerate instead of hierarchical).

# For the full hierarchy, we need either:
# (a) A larger subgroup than S4xS4xS4 within S12
# (b) Additional breaking from the fibration phases in a non-unitary way
# (c) Different Gram submatrix sizes for different S4 irrep pairings

# Let me check (c): the Gram entry between 1_a and 2 (for down-type) vs 1_b and 2 (for up-type)
# In the S4 action, 1_a (trivial), 1_b (sign), and 2 (doublet) are DIFFERENT irreps.
# The number of group elements mapping one to another might depend on the irreps.

# For sigma in S4: |{sigma: sigma(state_type) = state_type}|
# This is 6 for ANY state type (same stabilizer for any point).
# So G for 1_a-1_a = G for 1_b-1_b = G for 2-2 = same.

# The irreps don't give different Gram entries for the base action.
# The differences come from the fibration phases only.

print("=== Conclusion ===")
print("The S4 x S4 x S4 subgroup Gram gives three distinct values:")
print(f"  G_self        = {G_self}")
print(f"  G_same_gen    = {G_same}")
print(f"  G_cross_gen   = {G_cross}")
print()
print(f"This produces a 3-generation mass matrix with eigenvalues:")
print(f"  Heavy: {heavy:.0f}, Light(x2): {light:.0f}")
print(f"  Ratio: {heavy/light:.0f}:1:1 (top:c:u = 4:1:1)")
print()
print("The fibration phases (unitary transformation) DO NOT change eigenvalues.")
print("They only rotate eigenvectors, giving CKM/PMNS from misalignment between")
print("up-type and down-type phase assignments.")
print()
print("The observed mass hierarchy (m_t >> m_c >> m_u) requires additional")
print("structure beyond the base Gram and its unitary phase rotation.")
print("This is the open problem.")

result = {
    'schema': 'marici.nima.subgroup_gram_hierarchy.v1',
    'classification': 'S4xS4xS4_subgroup_Gram_gives_2_1_pattern_not_full_hierarchy',
    'G_self': G_self,
    'G_same_gen': G_same,
    'G_cross_gen': G_cross,
    'mass_eigenvalues': [int(light), int(light), int(heavy)],
    'predicted_ratio': '4:1:1',
    'observed_ratio': '136000:1000:1',
    'status': 'The S4xS4xS4 subgroup produces a 2+1 mass pattern (one heavy, two degenerate), not the full 3-tier hierarchy. The fibration phases do not split eigenvalues (unitary). Additional structure required.',
}

out = ROOT / 'results/subgroup-gram-hierarchy.json'
out.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(f"\n{json.dumps(result, indent=2)}")