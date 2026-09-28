"""Audit natural S4 representation and conditional doublet/singlet weights.
Exact finite character test; no files written.
"""
from itertools import permutations
from fractions import Fraction as F

# Three partitions of four labels into two unordered pairs.
partitions = {
    frozenset((frozenset((0,1)), frozenset((2,3)))),
    frozenset((frozenset((0,2)), frozenset((1,3)))),
    frozenset((frozenset((0,3)), frozenset((1,2)))),
}
def image(p, partition):
    return frozenset(frozenset(p[i] for i in pair) for pair in partition)

mismatches = []
for p in permutations(range(4)):
    natural = sum(p[i] == i for i in range(4))
    inversions = sum(p[i] > p[j] for i in range(4) for j in range(i+1,4))
    sign = (-1)**inversions
    # Permutation representation on pair partitions = trivial + 2D irrep.
    doublet = sum(image(p, part) == part for part in partitions) - 1
    proposed = 1 + sign + doublet
    if natural != proposed:
        mismatches.append((p, natural, proposed))
assert mismatches
transposition = (1,0,2,3)
assert (transposition,2,0) in mismatches
print(f'Natural 4-point representation differs from 1+sign+2 on {len(mismatches)}/24 permutations.')
print('Transposition: natural character=2, proposed character=0.')
print('Natural split is constant line plus 3D sum-zero subspace.')

# Conditional on the usual SM matter representation, with a common positive
# weight d for weak-doublet states and s for singlet states, per generation:
# weak trace = 2d; hypercharge = (2/3)d + (8/3)s.
def mixing(d, s):
    c2 = 2*d
    cy = F(2,3)*d + F(8,3)*s
    return c2/(c2+cy)
assert mixing(F(1),F(1)) == F(3,8)
assert mixing(F(1),F(9,4)) == F(3,13)
print('Doublet/singlet weights: sin^2(theta)=3d/[4(d+s)].')
print('Target 3/13 requires s/d=9/4. This ratio is inferred from the target.')
