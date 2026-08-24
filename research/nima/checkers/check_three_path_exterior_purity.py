"""Exact rank-three exterior-purity and Bargmann-phase audit."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
OUTPUT = ROOT / "research/nima/results/three-path-exterior-purity.json"

r = sp.Rational(1, 3)

# Same diagonal and same magnitudes for all pairwise overlaps, but different
# gauge-invariant triple phase.
gram_real = sp.Matrix([[1, r, r], [r, 1, r], [r, r, 1]])
gram_phase = sp.Matrix([[1, r, r], [r, 1, sp.I * r], [r, -sp.I * r, 1]])


def principal_minors(matrix: sp.Matrix) -> list[sp.Expr]:
    minors: list[sp.Expr] = []
    for size in range(1, matrix.rows + 1):
        for indices in __import__("itertools").combinations(range(matrix.rows), size):
            minors.append(sp.simplify(matrix.extract(indices, indices).det()))
    return minors


def exterior_two_weight(matrix: sp.Matrix) -> sp.Expr:
    return sp.simplify(
        sum(
            matrix.extract(indices, indices).det()
            for indices in ((0, 1), (0, 2), (1, 2))
        )
    )


def triple_bargmann(matrix: sp.Matrix) -> sp.Expr:
    return sp.simplify(matrix[0, 1] * matrix[1, 2] * matrix[2, 0])


real_det = sp.simplify(gram_real.det())
phase_det = sp.simplify(gram_phase.det())
real_e2 = exterior_two_weight(gram_real)
phase_e2 = exterior_two_weight(gram_phase)
real_bargmann = triple_bargmann(gram_real)
phase_bargmann = triple_bargmann(gram_phase)

# General Hermitian three-record determinant identity.
a, b, c = sp.symbols("a b c")
abar, bbar, cbar = sp.symbols("abar bbar cbar")
general = sp.Matrix([[1, a, b], [abar, 1, c], [bbar, cbar, 1]])
general_det = sp.expand(general.det())
expected_det = sp.expand(
    1 - a * abar - b * bbar - c * cbar + a * c * bbar + abar * cbar * b
)

gates = {
    "both_grams_are_strictly_positive": all(
        minor > 0
        for matrix in (gram_real, gram_phase)
        for minor in principal_minors(matrix)
    ),
    "pairwise_overlap_magnitudes_are_identical": all(
        sp.simplify(abs(gram_real[i, j]) - abs(gram_phase[i, j])) == 0
        for i in range(3)
        for j in range(i + 1, 3)
    ),
    "exterior_two_weights_are_identical": real_e2 == phase_e2,
    "triple_exterior_weights_differ": real_det != phase_det,
    "bargmann_phases_differ": sp.arg(real_bargmann) != sp.arg(phase_bargmann),
    "full_oriented_pairs_determine_triple_port": sp.simplify(
        general_det - expected_det
    ) == 0,
}
assert all(gates.values()), gates

result = {
    "schema": "marici.nima.three-path-exterior-purity.v1",
    "pairwise_overlap_magnitude": str(r),
    "real_packet": {
        "bargmann_product": str(real_bargmann),
        "exterior_two_weight": str(real_e2),
        "exterior_three_weight": str(real_det),
    },
    "phase_packet": {
        "bargmann_product": str(phase_bargmann),
        "exterior_two_weight": str(phase_e2),
        "exterior_three_weight": str(phase_det),
    },
    "general_determinant": str(general_det),
    "gates": gates,
    "conclusion": (
        "Pairwise magnitudes and all grade-two exterior weights do not fix "
        "the grade-three port. The missing datum is the gauge-invariant "
        "Bargmann phase. Full oriented pairwise coherences do fix the port, "
        "so no independent grade-three cell is required in the amplitude Gram."
    ),
}

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"passed": sum(gates.values()), "total": len(gates)}))

