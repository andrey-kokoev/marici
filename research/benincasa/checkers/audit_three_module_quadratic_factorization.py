#!/usr/bin/env python3
"""Exact universal factorization of the A2 quadratic scalar through Sym^2(A2)."""

from fractions import Fraction as F


def rank(a):
    a = [[F(x) for x in row] for row in a]
    r = 0
    for c in range(len(a[0]) if a else 0):
        p = next((i for i in range(r, len(a)) if a[i][c]), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        z = a[r][c]
        a[r] = [x / z for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c]:
                z = a[i][c]
                a[i] = [x - z * y for x, y in zip(a[i], a[r])]
        r += 1
    return r


def mv(a, x):
    return [sum(a[i][j] * x[j] for j in range(len(x))) for i in range(len(a))]


def veronese(x):
    # Symmetric tensor coordinates (x^2, xy, y^2).
    return [x[0] * x[0], x[0] * x[1], x[1] * x[1]]


R = [[F(0), F(-1)], [F(1), F(-1)]]

# Induced cyclic action on Sym^2 in the basis (x^2,xy,y^2), obtained by
# transporting three basis tensors.
S = [
    [F(0), F(0), F(1)],
    [F(0), F(-1), F(1)],
    [F(1), F(-2), F(1)],
]

samples = [[F(1), F(0)], [F(0), F(1)], [F(1), F(1)], [F(2), F(-3)]]

# Cartan norm q(x,y)=2x^2-2xy+2y^2 is a linear readout after Veronese.
q_row = [F(2), F(-2), F(2)]

# Invariant rows l satisfy lS=l.
invariant_constraints = [[S[j][i] - (F(1) if i == j else F(0))
                          for j in range(3)] for i in range(3)]
invariant_readout_dimension = 3 - rank(invariant_constraints)

# The universal quadratic images span all of Sym^2(A2).
universal_span_rank = rank([veronese(x) for x in samples[:3]])

# Direct linear scalar contradiction, using e1,e2,e1+e2.
q_values = [sum(q_row[i] * veronese(x)[i] for i in range(3)) for x in samples]
direct_linear_defect = q_values[2] - q_values[0] - q_values[1]

checks = {
    "veronese_is_cyclic_equivariant": all(veronese(mv(R, x)) == mv(S, veronese(x)) for x in samples),
    "quadratic_images_span_full_symmetric_square": universal_span_rank == 3,
    "unique_cyclic_scalar_readout_after_intervention": invariant_readout_dimension == 1,
    "cartan_readout_is_invariant": all(sum(q_row[i] * S[i][j] for i in range(3)) == q_row[j] for j in range(3)),
    "factorization_recovers_cartan_norm": q_values == [2, 2, 2, 38],
    "direct_linear_factorization_is_impossible": direct_linear_defect == -2,
}

assert all(checks.values()), checks
print(f"PASS {sum(checks.values())}/{len(checks)}")
print(f"universal middle rank: {universal_span_rank}")
print(f"invariant readout dimension: {invariant_readout_dimension}")
print(f"direct linear defect: {direct_linear_defect}")
