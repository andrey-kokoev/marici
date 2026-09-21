#!/usr/bin/env python3
"""Exact rational/complex-rational regression for matrix and extension realizations.

Run with: uv run --with sympy python research/nima/checkers/check_coherent_matrix_and_extension_realization.py
"""
import itertools
import json
from pathlib import Path
import sympy as s

ROOT = Path(__file__).resolve().parents[3]
G = list(itertools.permutations(range(3)))
identity = (0, 1, 2)


def mul(g, h):
    return tuple(g[h[j]] for j in range(3))


def inv(g):
    return tuple(g.index(j) for j in range(3))


def permutation(g):
    P = s.zeros(3)
    for j in range(3):
        P[g[j], j] = 1
    return P


B = s.Matrix([[1, 0], [0, 1], [-1, -1]])
H = B.T * B
reps = [
    {g: s.Matrix([[1]]) for g in G},
    {g: s.Matrix([[permutation(g).det()]]) for g in G},
    {g: (permutation(g)*B)[:2, :] for g in G},
]
grams = [s.eye(1), s.eye(1), H]
dims = [1, 1, 2]


def F(f):
    return [sum((f[g]*rep[g] for g in G), s.zeros(d))
            for rep, d in zip(reps, dims)]


def recover(blocks, g):
    return s.expand(sum(d*s.trace(rep[inv(g)]*A)
                        for rep, d, A in zip(reps, dims, blocks))/len(G))


def conv(f, h):
    out = dict.fromkeys(G, s.Integer(0))
    for a in G:
        for b in G:
            out[mul(a, b)] += f[a]*h[b]
    return {g: s.expand(v) for g, v in out.items()}


f = {g: s.Integer(j+1)+s.I*(j % 3-1) for j, g in enumerate(G)}
h = {g: s.Integer(2-j)+s.I*(j % 2) for j, g in enumerate(G)}
Ff, Fh = F(f), F(h)
Fconv = F(conv(f, h))
star_f = {g: s.conjugate(f[inv(g)]) for g in G}
Fstar = F(star_f)


def dagger(A, gram):
    return gram.inv()*A.conjugate().T*gram


def zero_matrix(A):
    return all(s.expand(x) == 0 for x in A)


lhs = sum(f[g]*s.conjugate(h[g]) for g in G)
rhs = sum(d*s.trace(A*dagger(C, gram))
          for d, A, C, gram in zip(dims, Ff, Fh, grams))/len(G)

s3_checks = {
    'all_representation_products': all(rep[mul(g, h)] == rep[g]*rep[h]
                                      for rep in reps for g in G for h in G),
    'dimension_sum': sum(d*d for d in dims) == len(G),
    'positive_invariant_gram': H[0, 0] > 0 and H.det() > 0 and
        all(rep[g].T*gram*rep[g] == gram for rep, gram in zip(reps, grams) for g in G),
    'full_basis_inversion': all(recover([rep[h] for rep in reps], g) == (1 if g == h else 0)
                               for g in G for h in G),
    'sample_complex_inversion': all(s.expand(recover(Ff, g)-f[g]) == 0 for g in G),
    'ordered_convolution': all(zero_matrix(C-A*B1) for C, A, B1 in zip(Fconv, Ff, Fh)),
    'star_compatibility': all(zero_matrix(C-dagger(A, gram))
                              for C, A, gram in zip(Fstar, Ff, grams)),
    'polarized_plancherel': s.expand(lhs-rhs) == 0,
    'noncommuting_frequency_block': any(reps[2][g]*reps[2][h] != reps[2][h]*reps[2][g]
                                       for g in G for h in G),
}

# The lower triangular incidence algebra.
e0 = s.Matrix([[1, 0], [0, 0]])
e1 = s.Matrix([[0, 0], [0, 1]])
u = s.Matrix([[0, 0], [1, 0]])
a, b, c, d, e, f0 = s.symbols('a b c d e f')
A = a*e0+b*e1+c*u
C = d*e0+e*e1+f0*u
product = a*d*e0+b*e*e1+(c*d+b*f0)*u
center_equations = list(A*e0-e0*A)+list(A*u-u*A)
center = s.linsolve(center_equations, (a, b, c))


def hom_ext(T, W):
    """T: V0->V1; W: W0->W1. Compute ker/coker of D(f0,f1)=W f0-f1 T."""
    v1, v0 = T.shape
    w1, w0 = W.shape
    columns = []
    for i in range(w0):
        for j in range(v0):
            E = s.zeros(w0, v0)
            E[i, j] = 1
            columns.append(s.Matrix(w1*v0, 1, list(W*E)))
    for i in range(w1):
        for j in range(v1):
            E = s.zeros(w1, v1)
            E[i, j] = 1
            columns.append(s.Matrix(w1*v0, 1, list(-E*T)))
    D = s.Matrix.hstack(*columns) if columns else s.zeros(w1*v0, 0)
    rank = D.rank()
    return {'hom': D.cols-rank, 'ext1': D.rows-rank}


S0 = s.zeros(0, 1)
S1 = s.zeros(1, 0)
P0 = s.eye(1)
E0, E1 = s.zeros(1), s.eye(1)
arrow_dimensions = {
    'S0_to_S1': hom_ext(S0, S1),
    'S1_to_S0': hom_ext(S1, S0),
    'P0_to_S1': hom_ext(P0, S1),
    'P1_to_S1': hom_ext(S1, S1),
    'E0_to_E0': hom_ext(E0, E0),
    'E1_to_E1': hom_ext(E1, E1),
}
# Faithful and split realizations have equal traces on every algebra element.
rho_split = s.diag(a, b)
rho_nonsplit = A
triangular_checks = {
    'incidence_convolution_formula': A*C == product,
    'square_zero_radical': u != s.zeros(2) and u*u == s.zeros(2),
    'scalar_observer_kernel': (u[0, 0], u[1, 1]) == (0, 0),
    'center_only_scalars': center == s.FiniteSet((b, b, 0)),
    'vertices_are_not_central': e0*u != u*e0 and e1*u != u*e1,
    'same_trace_for_split_and_nonsplit': s.trace(rho_split) == s.trace(rho_nonsplit),
    'one_extension_between_simples': arrow_dimensions['S0_to_S1'] == {'hom': 0, 'ext1': 1},
    'reverse_extension_vanishes': arrow_dimensions['S1_to_S0'] == {'hom': 0, 'ext1': 0},
    'projective_resolution_hom': arrow_dimensions['P0_to_S1'] == {'hom': 0, 'ext1': 0}
        and arrow_dimensions['P1_to_S1'] == {'hom': 1, 'ext1': 0},
    'split_endomorphisms': arrow_dimensions['E0_to_E0'] == {'hom': 2, 'ext1': 1},
    'nonsplit_endomorphisms': arrow_dimensions['E1_to_E1'] == {'hom': 1, 'ext1': 0},
    'adjoint_adjoins_reverse_arrow': u.T not in [e0, e1, u] and u*u.T == e1 and u.T*u == e0,
}
# Diamond resolution, evaluated at each vertex: P3 -> P1+P2 -> P0 -> S0.
diamond_rows = []
for vertex in range(4):
    active = ([False, False] if vertex == 0 else
              [True, False] if vertex == 1 else
              [False, True] if vertex == 2 else [True, True])
    middle_dim = sum(active)
    d2 = s.Matrix([1, -1]) if vertex == 3 else s.zeros(middle_dim, 0)
    d1 = s.ones(1, middle_dim)
    augmentation = s.eye(1) if vertex == 0 else s.zeros(0, 1)
    diamond_rows.append({
        'vertex': vertex,
        'chain': d1*d2 == s.zeros(1, d2.cols) and augmentation*d1 == s.zeros(augmentation.rows, middle_dim),
        'exact_middle': d2.rank()+d1.rank() == middle_dim,
        'exact_P0': d1.rank()+augmentation.rank() == 1,
        'left_injective': d2.rank() == d2.cols,
        'right_surjective': augmentation.rank() == augmentation.rows,
    })
# Hom(Pi,S3)=S3(i). Applying Hom to the resolution gives 0 -> 0 -> C.
simple_top = [0, 0, 0, 1]
hom_dims = [simple_top[0], simple_top[1]+simple_top[2], simple_top[3]]
coboundaries = [s.zeros(hom_dims[1], hom_dims[0]),
                s.zeros(hom_dims[2], hom_dims[1]), s.zeros(0, hom_dims[2])]
cohom_dims = [hom_dims[i]-coboundaries[i].rank()
              -(coboundaries[i-1].rank() if i else 0) for i in range(3)]
diamond_checks = {
    'projective_resolution_exact_at_all_vertices': all(
        all(v for k, v in row.items() if k != 'vertex') for row in diamond_rows),
    'ext1_bottom_to_top_zero': cohom_dims[1] == 0,
    'ext2_bottom_to_top_one': cohom_dims[2] == 1,
}

# Convert SymPy boolean values to ordinary JSON booleans.
s3_checks = {k: bool(v) for k, v in s3_checks.items()}
triangular_checks = {k: bool(v) for k, v in triangular_checks.items()}
out = {
    'schema': 'marici.nima.coherent-matrix-and-extension-realization.v1',
    'arithmetic': 'Exact rational and complex-rational SymPy arithmetic',
    'S3': {'irreducible_dimensions': dims, 'standard_gram': [list(H.row(i)) for i in range(2)],
           'checks': s3_checks},
    'two_stage_incidence': {'mapping_dimensions': arrow_dimensions, 'checks': triangular_checks},
    'diamond': {'vertexwise_resolution': diamond_rows, 'checks': diamond_checks},
    'passed': all(s3_checks.values()) and all(triangular_checks.values()) and all(diamond_checks.values()),
    'proof': 'research/nima/coherent-spectral-realization-matrix-blocks-and-extension-gluing.md',
}
out['S3']['standard_gram'] = [[int(v) for v in row] for row in out['S3']['standard_gram']]
path = ROOT/'research/nima/results/coherent-matrix-and-extension-realization.json'
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps(out, indent=2))
raise SystemExit(0 if out['passed'] else 1)
