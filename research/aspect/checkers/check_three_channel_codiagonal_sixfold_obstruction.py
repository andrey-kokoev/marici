import json

import sympy as sp


C, U, V = sp.symbols("C U V")
M = sp.Matrix([[1, 1, 1], [0, 1, -1], [2, -1, -1]])
packet = sp.Matrix([C, U, V])
ports = M * packet
gram = M * M.T
inverse = M.inv()

M2 = M.applyfunc(lambda x: int(x) % 2)
M3 = M.applyfunc(lambda x: int(x) % 3)


def rank_mod(matrix, prime):
    rows = [[int(x) % prime for x in matrix.row(i)] for i in range(matrix.rows)]
    rank = 0
    col = 0
    while rank < len(rows) and col < len(rows[0]):
        pivot = next((i for i in range(rank, len(rows)) if rows[i][col]), None)
        if pivot is None:
            col += 1
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inv = pow(rows[rank][col], -1, prime)
        rows[rank] = [(inv * x) % prime for x in rows[rank]]
        for i in range(len(rows)):
            if i != rank and rows[i][col]:
                factor = rows[i][col]
                rows[i] = [
                    (x - factor * y) % prime
                    for x, y in zip(rows[i], rows[rank])
                ]
        rank += 1
        col += 1
    return rank


zero_substitution = {C: sp.Rational(1, 2), V: -sp.Rational(1, 2) - U}

checks = {
    "rows_are_orthogonal": gram == sp.diag(3, 2, 6),
    "determinant_is_minus_six": M.det() == -6,
    "inverse_reconstructs_packet": sp.simplify(inverse * ports - packet)
    == sp.zeros(3, 1),
    "rank_drops_mod_two": rank_mod(M2, 2) == 2,
    "rank_drops_mod_three": rank_mod(M3, 3) == 2,
    "integral_cokernel_order_is_six": abs(int(M.det())) == 6,
    "zero_fiber_control_is_three_halves": sp.simplify(
        ports[2].subs(zero_substitution) - sp.Rational(3, 2)
    )
    == 0,
    "zero_fiber_antisymmetric_survives": sp.simplify(
        ports[1].subs(zero_substitution) - (2 * U + sp.Rational(1, 2))
    )
    == 0,
}

result = {
    "schema": "marici.aspect.three-channel-codiagonal-sixfold.v1",
    "status": "pass" if all(checks.values()) else "fail",
    "checks": checks,
    "readout_matrix": str(M),
    "row_gram": str(gram),
    "inverse_matrix": str(inverse),
    "interpretation": (
        "The theta three-port analyzer is orthogonal after normalization but "
        "has index six over the integral source lattice."
    ),
}

print(json.dumps(result, indent=2))
