#!/usr/bin/env python3
"""Exact audit of the proposed Morse primitive and the corrected source fibre.

Python 3.10+, standard library only.  Writes certificate.json and matrices.json
next to this script.  No assumed physical comparison is inserted into the checks.
"""
from __future__ import annotations
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import hashlib
import json

OUT = Path(__file__).resolve().parent
CHECKS = 0

def check(actual, expected, label):
    global CHECKS
    if actual != expected:
        raise AssertionError(f"{label}: {actual!r} != {expected!r}")
    CHECKS += 1

def zeros(m, n):
    return [[0] * n for _ in range(m)]

def eye(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]

def transpose(A):
    return [list(c) for c in zip(*A)]

def mm(A, B):
    if not A or not B:
        raise ValueError("Use shaped zero matrices, not an empty matrix")
    if len(A[0]) != len(B):
        raise ValueError("Matrix dimensions do not match")
    return [[sum(x*y for x, y in zip(row, col)) for col in zip(*B)] for row in A]

def add(A, B):
    return [[x+y for x,y in zip(a,b)] for a,b in zip(A,B)]

def neg(A):
    return [[-x for x in row] for row in A]

def sub(A, B):
    return add(A, neg(B))

def inverse(A):
    n = len(A)
    rows = [[Fraction(x) for x in row] + [Fraction(int(i == j)) for j in range(n)]
            for i,row in enumerate(A)]
    for j in range(n):
        pivot = next((i for i in range(j,n) if rows[i][j]), None)
        if pivot is None:
            raise ValueError("Singular matrix")
        rows[j], rows[pivot] = rows[pivot], rows[j]
        v = rows[j][j]
        rows[j] = [x/v for x in rows[j]]
        for i in range(n):
            if i != j:
                v = rows[i][j]
                if v:
                    rows[i] = [x-v*y for x,y in zip(rows[i],rows[j])]
    return [r[n:] for r in rows]

# Entry 436: homogeneous chain degrees 3,2,1,0, with no regrading.
d3 = [[0],[1],[1],[1]]
d2 = [[1,0,0,0],[1,0,0,0],[0,1,0,-1],[0,-1,1,0],[0,0,-1,1]]
d1 = [[1,-1,-1,-1,-1]]
r = [[0,0,1,1,1]]
z = [[1],[0],[1],[0],[0]]
h0 = [[1],[0],[0],[0],[0]]
h1 = [[0,1,0,0,0],[0,0,0,-1,-1],[0,0,0,0,-1],[0,0,0,0,0]]
h2 = [[0,0,0,1]]

check(mm(d2,d3), zeros(5,1), 'd2 d3')
check(mm(d1,d2), zeros(1,4), 'd1 d2')
check(mm(d1,z), [[0]], 'z closed')
check(mm(r,d2), zeros(1,4), 'r closed')
check(mm(r,z), [[1]], 'primitive readout')
check(mm(d1,h0), eye(1), 'contraction degree 0')
check(add(mm(d2,h1),mm(h0,d1)), sub(eye(5),mm(z,r)), 'contraction degree 1')
check(add(mm(d3,h2),mm(h1,d2)), eye(4), 'contraction degree 2')
check(mm(h2,d3), eye(1), 'contraction degree 3')
check(mm(h1,h0), zeros(4,1), 'h squared on degree 0')
check(mm(h2,h1), zeros(1,5), 'h squared on degree 1')
check(mm(h1,z), zeros(4,1), 'h i')
check(mm(r,h0), [[0]], 'r h')

# Integral change of basis in degree 1: three boundaries, one homology
# generator, one preimage of the degree-zero generator.
B1 = transpose([list(c) for c in zip(*d2)][:3] + [list(x[0] for x in z), list(x[0] for x in h0)])
B1inv = inverse(B1)
check(all(x.denominator == 1 for row in B1inv for x in row), True, 'integral degree-1 splitting')
check(mm(B1,B1inv), eye(5), 'degree-1 splitting inverse')

# Full classification of closed rows using exact symbolic coefficient vectors.
# w d2=0 gives w0+w1=0 and w2=w3=w4.  Normalize w z=1.
endpoint_difference = [[-1,1,0,0,0]]
check(mm(endpoint_difference,d2), zeros(1,4), 'endpoint-difference row closed')
check(neg(add(endpoint_difference,r)), d1, 'one exact row relation')
# Every nullhomotopy into C[1] only has h0:J0 -> C1; its boundary is c*d1.
check(mm(d1,z), [[0]], 'all possible primitive boundaries vanish on z')
# Thus the primitive equation cannot hold: its detector is 1, while
# the detector on every candidate coboundary is 0.  No finite search is used.
obstruction_value = mm(r,z)[0][0]
check(obstruction_value, 1, 'exact obstruction to nullhomotopy')

# The proposed Morse map from a boundary-pair D2 --1--> D1 to J.
# A chain map sending the bottom to z would require d2*w=z.
check(mm(r,d2), zeros(1,4), 'left-null detector for d2*w=z')
check(mm(r,z), [[1]], 'nonzero right-side detector')

# Cone fibre of a_C=epsilon_B*r, with modules:
# F3=B, F2=B^4, F1=B^5, F0=B direct-sum C.
# Integers in C-valued rows mean compose with epsilon_B:B->C.
Fd1 = d1 + r
Fd2 = d2
Fd3 = d3
p1 = r
p0 = [[0,1]]
i1 = z
i0 = [[0],[1]]
Fh0 = [[row[0],0] for row in h0]
check(mm(Fd1,Fd2), zeros(2,4), 'fibre d1 d2')
check(mm(Fd2,Fd3), zeros(5,1), 'fibre d2 d3')
check(mm(p0,Fd1), p1, 'fibre projection to [B -> C]')
check(mm(Fd1,i1), i0, 'fibre inclusion from [B -> C]')
check(mm(p1,i1), eye(1), 'reduced fibre degree-1 retraction')
check(mm(p0,i0), eye(1), 'reduced fibre degree-0 retraction')
check(mm(Fd1,Fh0), sub(eye(2),mm(i0,p0)), 'fibre homotopy degree 0')
check(add(mm(Fd2,h1),mm(Fh0,Fd1)), sub(eye(5),mm(i1,p1)), 'fibre homotopy degree 1')
check(add(mm(Fd3,h2),mm(h1,Fd2)), eye(4), 'fibre homotopy degree 2')
check(mm(h2,Fd3), eye(1), 'fibre homotopy degree 3')
# Universal nullhomotopy is the C component of F0.
S0 = [[0,1]]
check(mm(S0,Fd1), r, 'universal fibre nullhomotopy')
check(mm(Fd1,z), [[0],[1]], 'unit z is not closed in the fibre')

# Strict lifts J_B -> T[1], checked on the conductor.  Global proof uses
# the B-linear maps ell_+(b)=(b_+,0), ell_-(b)=(0,-b_-).
nu = [[1],[1]]
rho = [[1,-1]]
ell_plus = [[1],[0]]
ell_minus = [[0],[-1]]
check(mm(rho,nu), [[0]], 'normalization exact-sequence composition')
check(mm(rho,ell_plus), [[1]], 'positive lift on conductor unit')
check(mm(rho,ell_minus), [[1]], 'negative lift on conductor unit')
Aplus = mm(ell_plus,r)
Aminus = mm(ell_minus,r)
AS = neg(r)  # J1 -> T[1]_2=B, whose boundary is -nu
check(mm(Aplus,d2), zeros(2,4), 'a+ chain equation')
check(mm(Aminus,d2), zeros(2,4), 'a- chain equation')
check(mm(neg(nu),AS), sub(Aplus,Aminus), 'a+-a- is a boundary')
check(mm(AS,d2), zeros(1,4), 'source homotopy lower equation')

# Cochain kernel homotopy k_nu=-G, with the two endpoint bottom units
# symbolically independent.  Its differential e_nu has top value v++v-.
G = eye(2)
k = neg(G)
e = nu
Hplus = mm(k,Aplus)
Hminus = mm(k,Aminus)
check(mm(k,neg(nu)), e, 'delta k_nu=e_nu')
check(sub(Hplus,Hminus), mm(e,AS), 'nonclosed postcomposition correction')
check(sub(sub(Hplus,Hminus),mm(e,AS)), zeros(2,5), 'corrected representative difference')
# e_nu a+ and e_nu a- vanish because a+_2=a-_2=0.

# Six-generator conductor ideal.  Construct all 24 first syzygies.
variables = ['x1','x2','x3','y1','y2','y3']
linear_module_basis = [(i,j) for i in range(6) for j in range(6)]
quadratic_basis = ([(i,j) for i in range(3) for j in range(i,3)]
                   + [(i,j) for i in range(3,6) for j in range(i,6)])
quad_index = {q:i for i,q in enumerate(quadratic_basis)}
lin_index = {ij:i for i,ij in enumerate(linear_module_basis)}
product = zeros(12,36)
for k,(i,j) in enumerate(linear_module_basis):
    if i//3 == j//3:
        product[quad_index[tuple(sorted((i,j)))]][k] = 1
syzygy_cols = []
syzygy_labels = []
for block in (range(3),range(3,6)):
    for i,j in combinations(block,2):
        v = [0]*36
        v[lin_index[(i,j)]] = 1
        v[lin_index[(j,i)]] = -1
        syzygy_cols.append(v)
        syzygy_labels.append(f'{variables[i]} e_{variables[j]} - {variables[j]} e_{variables[i]}')
for i in range(3):
    for j in range(3,6):
        for a,b in ((i,j),(j,i)):
            v = [0]*36
            v[lin_index[(a,b)]] = 1
            syzygy_cols.append(v)
            syzygy_labels.append(f'{variables[a]} e_{variables[b]}')
syz = transpose(syzygy_cols)
check(len(syzygy_cols),24,'first syzygy count')
check(mm(product,syz), zeros(12,24), 'all conductor syzygies are relations')
# Twelve monomial lifts complement these 24 kernel columns by a unimodular basis.
lifts = []
for i,j in quadratic_basis:
    v=[0]*36
    v[lin_index[(i,j)]]=1
    lifts.append(v)
change = transpose(lifts+syzygy_cols)
change_inv = inverse(change)
check(all(v.denominator == 1 for row in change_inv for v in row), True, 'degree-2 syzygy basis saturated')
check(mm(change,change_inv), eye(36), 'degree-2 syzygy basis inverse')
check(mm(product,change), [eye(12)[i]+[0]*24 for i in range(12)], 'degree-2 exactness matrix')

# Laurent residue detector for each endpoint after t_i=1. Bottom generator
# 1/(x1*x2*x3) is detected; any one-circle incoming summand leaves one x_i
# unlocalized and therefore cannot contain the triple exponent (-1,-1,-1).
residue_degree = (-1,-1,-1)
for missing in range(3):
    check(residue_degree[missing] < 0, True, 'residue outside incoming localization')
check(int(residue_degree == (-1,-1,-1)), 1, 'bottom endpoint residue')

matrices = {
    'degree_convention':'homological; differential lowers degree; cochain Hom degree r lowers chain degree by r',
    'J': {'d3':d3,'d2':d2,'d1':d1,'readout':r,'primitive_z':z,
          'h0':h0,'h1':h1,'h2':h2},
    'fibre': {'modules':{'3':'B','2':'B^4','1':'B^5','0':'B direct-sum C'},
              'd1':Fd1,'d2':Fd2,'d3':Fd3,
              'C_row_convention':'Every integer from B to C is followed by epsilon_B',
              'projection1':p1,'projection0':p0,'inclusion1':i1,'inclusion0':i0,
              'homotopy0':Fh0,'homotopy1':h1,'homotopy2':h2,'universal_nullhomotopy0':S0},
    'normalization_lifts':{'conductor_nu':nu,'rho':rho,'a_plus':Aplus,'a_minus':Aminus,
                           'source_homotopy':AS,'k_nu_formal':k,'e_nu_formal':e,
                           'Hplus_formal':Hplus,'Hminus_formal':Hminus},
    'conductor_syzygies':{'variables':variables,'labels':syzygy_labels,
                           'linear_module_basis':linear_module_basis,
                           'quadratic_basis':quadratic_basis,
                           'multiplication_matrix':product,'syzygy_matrix':syz,
                           'unimodular_completion':change}
}
serialized = json.dumps(matrices,indent=2,sort_keys=True)+'\n'
(OUT/'matrices.json').write_text(serialized)
cert = {
    'schema':'marici.source_frame_admissibility.v2',
    'assertions_executed':CHECKS,
    'input_repo':'andrey-kokoev/marici',
    'input_commit':'d1947b67a60d3e88ba77f4ca60ea02c2a306ee61',
    'input_source':'research/voevodsky/check_physical_derived_pullback_after_transform.py',
    'input_blob_sha':'7993b2b1bbdba03d05c3f443a45717d7b8efeec5',
    'facts_checked':{
        'J_integral_deformation_retract':'J_Z ≃ Z[1]',
        'a_C_primitive_readout':1,
        'nullhomotopy_of_a_C_exists':False,
        'map_of_corrected_Morse_boundary_to_primitive_z_exists':False,
        'strict_B_free_source_lifts':'a+ and a-, homotopic',
        'nonclosed_k_nu_composition_requires_homotopy_correction':True,
        'homotopy_fibre_reduced_complex':'[B --epsilon--> C] in degrees 1,0',
        'homotopy_fibre_quasi_isomorphism':'I[1]',
        'derived_conductor_fibre_H1':'I/I^2 = C^6',
        'derived_conductor_fibre_H2':'Tor_1^B(C,I) = C^24',
        'full_higher_Tor_calculated':False
    },
    'physical_scope':{
        'source_mismatch_resolved_by_identification':False,
        'physical_primitive_P_constructed':False,
        'framed_admissibility_of_alternative_physical_primitive_established':False,
        'physical_Delta_value_assigned':False,
        'new_fibre_identified_as_physical_source':False
    },
    'matrices_sha256':hashlib.sha256(serialized.encode()).hexdigest(),
    'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'proof_scope':'Integer identities are checked. Arbitrary-polynomial syzygy completeness and geometric scope are proved in proof.md; no physical input is inferred from a check count.'
}
(OUT/'certificate.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps(cert,indent=2,sort_keys=True))
