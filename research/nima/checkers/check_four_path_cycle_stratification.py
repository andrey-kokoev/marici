"""Exact four-path cycle reconstruction and chord-deletion audit."""

from __future__ import annotations

import itertools
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
OUTPUT = ROOT / "research/nima/results/four-path-cycle-stratification.json"


def principal_minors(matrix: sp.Matrix) -> list[sp.Expr]:
    return [
        sp.simplify(matrix.extract(indices, indices).det())
        for size in range(1, matrix.rows + 1)
        for indices in itertools.combinations(range(matrix.rows), size)
    ]


# On the open nonzero-chord locus, the four-cycle is reconstructed from two
# triangle Bargmann monomials after multiplying by the chord norm.
g12, g23, g34, g41, g13, g31 = sp.symbols(
    "g12 g23 g34 g41 g13 g31", nonzero=True
)
b123 = g12 * g23 * g31
b134 = g13 * g34 * g41
c1234 = g12 * g23 * g34 * g41
open_locus_relation = sp.expand(b123 * b134 - (g13 * g31) * c1234)

# The cycle-space dimension of connected K4 is E-V+1=3.  The oriented
# incidence matrix verifies this without choosing phases or a gauge.
incidence = sp.Matrix(
    [
        [-1, -1, -1, 0, 0, 0],
        [1, 0, 0, -1, -1, 0],
        [0, 1, 0, 1, 0, -1],
        [0, 0, 1, 0, 1, 1],
    ]
)
cycle_rank = len(incidence.nullspace())

# Hostile chord-deletion boundary.  All proper principal minors and all
# triangle Bargmann products agree, but the grade-four determinant changes
# with the surviving chordless cycle phase.
r = sp.Rational(1, 4)
gram_real = sp.Matrix(
    [
        [1, r, 0, r],
        [r, 1, r, 0],
        [0, r, 1, r],
        [r, 0, r, 1],
    ]
)
gram_phase = sp.Matrix(
    [
        [1, r, 0, sp.I * r],
        [r, 1, r, 0],
        [0, r, 1, r],
        [-sp.I * r, 0, r, 1],
    ]
)


def proper_principal_minors(matrix: sp.Matrix) -> list[sp.Expr]:
    return [
        sp.simplify(matrix.extract(indices, indices).det())
        for size in range(1, matrix.rows)
        for indices in itertools.combinations(range(matrix.rows), size)
    ]


def triangle_products(matrix: sp.Matrix) -> list[sp.Expr]:
    return [
        sp.simplify(matrix[i, j] * matrix[j, k] * matrix[k, i])
        for i, j, k in itertools.combinations(range(4), 3)
    ]


def four_cycle(matrix: sp.Matrix) -> sp.Expr:
    return sp.simplify(matrix[0, 1] * matrix[1, 2] * matrix[2, 3] * matrix[3, 0])


proper_real = proper_principal_minors(gram_real)
proper_phase = proper_principal_minors(gram_phase)
triangles_real = triangle_products(gram_real)
triangles_phase = triangle_products(gram_phase)
cycle_real = four_cycle(gram_real)
cycle_phase = four_cycle(gram_phase)
det_real = sp.simplify(gram_real.det())
det_phase = sp.simplify(gram_phase.det())

gates = {
    "k4_cycle_space_has_rank_three": cycle_rank == 3,
    "open_locus_four_cycle_is_triangle_composite": open_locus_relation == 0,
    "hostile_packets_are_strictly_positive": all(
        minor > 0
        for matrix in (gram_real, gram_phase)
        for minor in principal_minors(matrix)
    ),
    "proper_principal_data_agree": proper_real == proper_phase,
    "all_triangle_products_agree_and_vanish": (
        triangles_real == triangles_phase
        and all(value == 0 for value in triangles_real)
    ),
    "four_cycle_survives_and_changes": cycle_real != 0 and cycle_real != cycle_phase,
    "grade_four_port_distinguishes_packets": det_real != det_phase,
}
assert all(gates.values()), gates

result = {
    "schema": "marici.nima.four-path-cycle-stratification.v1",
    "cycle_space_rank": cycle_rank,
    "open_locus_relation": "B123*B134 = |g13|^2*C1234",
    "chord_deletion_boundary": {
        "deleted_chords": ["g13", "g24"],
        "proper_principal_minors": [str(value) for value in proper_real],
        "triangle_products": [str(value) for value in triangles_real],
        "real_cycle": str(cycle_real),
        "phase_cycle": str(cycle_phase),
        "real_grade_four_port": str(det_real),
        "phase_grade_four_port": str(det_phase),
    },
    "gates": gates,
    "conclusion": (
        "A four-cycle is composite from triangle Bargmann data on the "
        "nonzero-chord locus.  On the chord-deletion boundary the triangle "
        "probes vanish while a chordless four-cycle survives and changes the "
        "grade-four exterior port.  New arity-four information is therefore "
        "support-stratified, not generic."
    ),
}

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"passed": sum(gates.values()), "total": len(gates)}))
