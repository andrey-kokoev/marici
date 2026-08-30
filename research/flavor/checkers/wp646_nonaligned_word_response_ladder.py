"""Exact WP646 weak-basis-invariant response-rank ladder."""
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
wp450 = json.loads((ROOT / "results" / "wp450_messenger_word_grammar.json").read_text())
I = sp.I
J = [
    sp.Matrix([[0, 1, 0], [1, 0, 1], [0, 1, 0]]) / sp.sqrt(2),
    sp.Matrix([[0, -I, 0], [I, 0, -I], [0, I, 0]]) / sp.sqrt(2),
    sp.diag(1, 0, -1),
]
linear_words = [sp.eye(3)] + J
matrix_units = []
for row in range(3):
    for col in range(3):
        unit = sp.zeros(3)
        unit[row, col] = 1
        matrix_units.append(unit)

c12, s12 = sp.Rational(3, 5), sp.Rational(4, 5)
c23, s23 = sp.Rational(5, 13), sp.Rational(12, 13)
c13, s13 = sp.Rational(8, 17), sp.Rational(15, 17)
V = sp.Matrix([
    [c12*c13, s12*c13, -I*s13],
    [-s12*c23-I*c12*s23*s13, c12*c23-I*s12*s23*s13, s23*c13],
    [s12*s23-I*c12*c23*s13, -c12*s23-I*s12*c23*s13, c23*c13],
])
Yu, Yd = sp.diag(1, 2, 4), V * sp.diag(3, 5, 7)
Hu, Hd = Yu * Yu.H, Yd * Yd.H
C = Hu * Hd - Hd * Hu


def invariant_column(dyu, dyd):
    dhu = dyu * Yu.H + Yu * dyu.H
    dhd = dyd * Yd.H + Yd * dyd.H
    values = [k * sp.trace(Hu**(k-1) * dhu) for k in (1, 2, 3)]
    values += [k * sp.trace(Hd**(k-1) * dhd) for k in (1, 2, 3)]
    values += [
        sp.trace(dhu*Hd + Hu*dhd),
        sp.trace((dhu*Hu + Hu*dhu)*Hd + Hu**2*dhd),
        sp.trace(dhu*Hd**2 + Hu*(dhd*Hd + Hd*dhd)),
    ]
    dc = dhu*Hd + Hu*dhd - dhd*Hu - Hd*dhu
    values.append(sp.im(3 * sp.trace(C**2 * dc)))
    return sp.Matrix([sp.simplify(sp.expand_complex(value)) for value in values])


def response(words):
    columns = []
    for sector in ("up", "down"):
        for phase in (1, I):
            for word in words:
                zero = sp.zeros(3)
                columns.append(invariant_column(
                    phase*word if sector == "up" else zero,
                    phase*word if sector == "down" else zero))
    return sp.Matrix.hstack(*columns)


linear_response = response(linear_words)
full_response = response(matrix_units)
checks = {
    "wp450_linear_word_rank_is_four": wp450["linear_span_dimension"] == 4,
    "wp450_degree_two_word_rank_is_nine": wp450["degree_two_span_dimension"] == 9,
    "exact_ckm_witness_is_unitary": sp.simplify(V*V.H-sp.eye(3)) == sp.zeros(3),
    "linear_response_shape_is_ten_by_sixteen": linear_response.shape == (10, 16),
    "linear_word_intrinsic_response_rank_is_nine": linear_response.rank() == 9,
    "full_response_shape_is_ten_by_thirty_six": full_response.shape == (10, 36),
    "degree_two_complete_grammar_has_full_intrinsic_rank": full_response.rank() == 10,
    "aligned_rank_is_strictly_smaller_than_linear_rank": 2 < linear_response.rank(),
    "linear_rank_is_strictly_smaller_than_complete_rank": (
        linear_response.rank() < full_response.rank()),
}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP646", "status": "PASS", "checks": checks,
    "intrinsic_quotient_dimension": 10,
    "rank_ladder": {"aligned_charged_loop": 2, "identity_plus_linear_words": 9,
                    "degree_two_complete_words": 10},
    "linear_word_classification": "conditional codimension-one tangent capacity; coefficients lack source selection authority",
    "degree_two_classification": "universal local carrier capacity; not selector",
    "smallest_authority_falsifier": "arbitrary linear-word coefficients can be varied without a source law",
    "next_gate": "derive linear-word coefficients independently and test rank-nine relation on all 1210 sheets",
}
(ROOT / "results" / "wp646_nonaligned_word_response_ladder.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
