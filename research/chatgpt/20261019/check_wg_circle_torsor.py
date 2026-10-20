#!/usr/bin/env python3
"""Exact finite checks for a four-cycle torsor and its join tower.

Run: python check_wg_circle_torsor.py --output wg_circle_torsor_results.json
Only the Python standard library is required.

Checks graph automorphisms, all four abelian heaps on a labelled four-set,
heap laws, graph covariance, continuous-extension obstruction for the XOR
heap, subdivision compatibility, and finite join incidence. These checks
are NOT an Agda proof, a native Marici derivation, or a computational proof
of the infinite-join/classifying-space theorem. See the accompanying note.
"""
from __future__ import annotations
import argparse
import itertools as it
import json
import math
from collections import Counter
from fractions import Fraction as F
from pathlib import Path

COUNTS: Counter[str] = Counter()

def check(value: bool, label: str) -> None:
    if not value:
        raise AssertionError(label)
    COUNTS[label] += 1

P = tuple(range(4))
EDGES = {frozenset((i, (i + 1) % 4)) for i in P}
PERMS = tuple(it.permutations(P))
AUT = tuple(p for p in PERMS if {frozenset((p[a], p[b])) for a, b in
                                              ((i, (i + 1) % 4) for i in P)} == EDGES)

def sign(p: tuple[int, ...]) -> int:
    """Orientation of the induced map of the four-edge circle."""
    d = [(p[(i + 1) % 4] - p[i]) % 4 for i in P]
    if all(v == 1 for v in d):
        return 1
    if all(v == 3 for v in d):
        return -1
    raise ValueError('Not a cycle automorphism')

ROT = tuple(p for p in AUT if sign(p) == 1)
check(len(AUT) == 8, 'D4_order')
check(len(ROT) == 4, 'intrinsic_rotation_subgroup')
check(not any(all(p[e] == e for p in AUT) for e in P), 'no_equivariant_origin')

def h(x: int, y: int, z: int) -> int:
    candidates = [r for r in ROT if r[y] == x]
    if len(candidates) != 1:
        raise AssertionError('rotation displacement is not unique')
    return candidates[0][z]

for x, y, z in it.product(P, repeat=3):
    check(h(x,y,z) == (x-y+z) % 4, 'intrinsic_heap_matches_coordinate_formula')
    check(h(x,y,z) == h(z,y,x), 'abelian_outer_symmetry')
for x, y in it.product(P, repeat=2):
    check(h(x,y,y) == x and h(y,y,x) == x, 'heap_units')
for x,y,z,u,v in it.product(P, repeat=5):
    check(h(h(x,y,z),u,v) == h(x,y,h(z,u,v)), 'heap_associativity')
for p in AUT:
    for x,y,z in it.product(P, repeat=3):
        check(h(p[x],p[y],p[z]) == p[h(x,y,z)], 'full_D4_equivariance')

TRIPLES = tuple(it.product(P, repeat=3))
TINDEX = {t:i for i,t in enumerate(TRIPLES)}

def transported_table(p: tuple[int,...], kind: str) -> tuple[int,...]:
    inv = tuple(p.index(i) for i in P)
    def op(x: int,y: int,z: int) -> int:
        a,b,c = inv[x],inv[y],inv[z]
        return p[(a-b+c)%4] if kind == 'cyclic' else p[a^b^c]
    return tuple(op(*t) for t in TRIPLES)

def ev(table: tuple[int,...], x: int,y: int,z: int) -> int:
    return table[TINDEX[x,y,z]]

# Every heap with four elements is a torsor for C4 or V4 after choosing
# any origin. Enumerating both groups and all labels is exhaustive.
heaps = {transported_table(p,k) for p in PERMS for k in ('cyclic','xor')}
check(len(heaps) == 4, 'four_abelian_heaps_exhaustively_labelled')
equivariant = [t for t in heaps if all(ev(t,p[x],p[y],p[z]) == p[ev(t,x,y,z)]
                         for p in AUT for x,y,z in TRIPLES)]
check(len(equivariant) == 2, 'two_D4_equivariant_heaps')
cyclic = tuple(h(*t) for t in TRIPLES)
continuous_candidates = [t for t in equivariant if all(
    tuple(ev(t,x,y,z) for z in P) in ROT for x,y in it.product(P,repeat=2))]
check(continuous_candidates == [cyclic], 'unique_circle_extendable_heap')
xor_translation = tuple(1 ^ z for z in P)
check(sign(xor_translation) == -1, 'xor_translation_reverses_circle_orientation')

for level in range(4):
    n = 4 * 2**level
    for x,y,z in it.product(range(n),repeat=3):
        check((2*x-2*y+2*z)%(2*n) == 2*((x-y+z)%n), 'subdivision_covariance')

# Exact rational samples of the continuous formula; the all-real proof is
# the algebraic identity (eps*x+a)-(eps*y+a)+(eps*z+a)=eps*(x-y+z)+a.
grid = tuple(F(k,3) for k in range(12))
for eps,a in it.product((-1,1), P):
    for x,y,z in it.product(grid,repeat=3):
        g = lambda s: (eps*s+a)%4
        check((g(x)-g(y)+g(z))%4 == g((x-y+z)%4), 'rational_affine_covariance')

join_data = []
# Each C4 is S0*S0. Thus m copies have 2m antipodal pairs; a simplex
# contains at most one element from each pair, proving the crosspolytope
# boundary identification for every m, not just the values enumerated here.
for m in range(1,5):
    counts = Counter()
    for choices in it.product((-1,0,1), repeat=2*m):
        k = sum(c != 0 for c in choices)
        if k:
            counts[k-1] += 1
    f = [counts[d] for d in range(2*m)]
    expected = [2**(d+1) * math.comb(2*m,d+1) for d in range(2*m)]
    check(f == expected, 'join_crosspolytope_face_census')
    check(sum((-1)**d*f[d] for d in range(len(f))) == 0, 'odd_sphere_euler')
    join_data.append({'circle_factors':m,'sphere_dimension':2*m-1,
                      'f_vector':f,'quotient_under_circle':'CP^'+str(m-1)})

# Exact complex arithmetic and unit sphere examples in C^(n+1).
C = tuple[F,F]
def cmul(a:C,b:C)->C: return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def conj(a:C)->C: return a[0],-a[1]
def norm(a:C)->F: return a[0]*a[0]+a[1]*a[1]
def csum(xs)->C:
    xs=list(xs); return sum((x[0] for x in xs),F(0)),sum((x[1] for x in xs),F(0))
def projector(z:tuple[C,...]): return tuple(tuple(cmul(a,conj(b)) for b in z) for a in z)
phases=((F(1),F(0)),(F(0),F(1)),(F(3,5),F(4,5)),(F(-5,13),F(12,13)))
for n in range(1,5):
    for seed in range(1,4):
        u = [F((j+seed)%7+1, j+seed+2) for j in range(2*n+1)]
        uu=sum((v*v for v in u),F(0)); den=1+uu
        real=[(1-uu)/den]+[2*v/den for v in u]
        z=tuple((real[2*j],real[2*j+1]) for j in range(n+1))
        check(sum((norm(v) for v in z),F(0)) == 1, 'join_sphere_coordinates')
        M=projector(z)
        check(sum((M[i][i][0] for i in range(n+1)),F(0)) == 1, 'projector_trace')
        for i,j in it.product(range(n+1),repeat=2):
            check(csum(cmul(M[i][k],M[k][j]) for k in range(n+1)) == M[i][j],
                  'projector_idempotence')
        for a in phases:
            check(projector(tuple(cmul(a,v) for v in z)) == M,'phase_quotient_invariance')
        Z=z+((F(0),F(0)),)
        big=projector(Z)
        check(tuple(row[:-1] for row in big[:-1]) == M, 'tower_inclusion_compatibility')

result={'status':'pass','total_exact_checks':sum(COUNTS.values()),
        'counts':dict(sorted(COUNTS.items())), 'automorphisms':[list(p) for p in AUT],
        'rotation_subgroup':[list(p) for p in ROT],
        'abelian_heaps_on_four_labels':len(heaps),
        'D4_equivariant_heaps':len(equivariant),
        'circle_extendable_equivariant_heaps':len(continuous_candidates),
        'xor_orientation_reversing_translation':list(xor_translation),
        'join_levels':join_data,
        'theorem_inputs_not_verified_by_this_program':[
            'standard equal-edge topological realization of the cycle',
            'connected topological circle translations preserve orientation',
            'S^(2n+1)/U(1) is CP^n with its tautological principal bundle',
            'Milnor infinite-join universal-bundle theorem',
            'Hopf invariant and projective-space cohomology'],
        'not_claimed':['native Marici derivation','Agda or Lean compilation',
                       'original tetrahedral A4 action recovered on a single quotient sphere',
                       'selection of all physics or of SU(2)/SU(3)']}
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output',type=Path)
args=parser.parse_args()
text=json.dumps(result,indent=2)
if args.output:
    args.output.write_text(text+'\n',encoding='utf-8')
print(text)
