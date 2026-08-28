from fractions import Fraction
import json
from pathlib import Path


def transpose(matrix):
    return [list(column) for column in zip(*matrix)]


def matvec(matrix, vector):
    return [
        sum((entry * value for entry, value in zip(row, vector)), Fraction(0))
        for row in matrix
    ]


cutoffs = []
for n in range(1, 13):
    # A deterministic full-rank synthesis fixture with nontrivial off-diagonal
    # entries. Rows are analytic samples; columns are arithmetic labels.
    synthesis = [
        [Fraction(1 if i == j else i + j + 1, n + i + j + 2) for j in range(n)]
        for i in range(n)
    ]
    synthesis_t = transpose(synthesis)
    endpoint_probe = [Fraction(1)] + [Fraction(0) for _ in range(n - 1)]
    endpoint_row = matvec(synthesis_t, endpoint_probe)
    assert endpoint_row == synthesis[0]

    for length in range(1, n + 1):
        seam_probe = [
            Fraction(1 if i < length else 0) for i in range(n)
        ]
        seam_row = matvec(synthesis_t, seam_probe)
        expected = [
            sum((synthesis[i][j] for i in range(length)), Fraction(0))
            for j in range(n)
        ]
        assert seam_row == expected

        probe_norm_squared = sum(value * value for value in seam_probe)
        assert probe_norm_squared == length

    constant_unit = [Fraction(1, n) for _ in range(n)]
    # Its squared l2 norm is 1/n and its seam value is 1. After unit
    # normalization the seam value squared is n.
    norm_squared = sum(value * value for value in constant_unit)
    seam_value = sum(constant_unit)
    hostile_ratio_squared = seam_value * seam_value / norm_squared
    assert hostile_ratio_squared == n

    cutoffs.append(
        {
            "cutoff": n,
            "endpoint_transpose_identity": True,
            "all_fixed_seam_transpose_identities": True,
            "largest_fixed_seam_dual_cost_squared": n,
            "moving_seam_hostile_ratio_squared": int(hostile_ratio_squared),
        }
    )

result = {
    "schema": "marici.nima.endpoint-fixed-seam-transpose-provenance.v1",
    "cutoffs": cutoffs,
    "endpoint_has_uniform_representative": True,
    "each_fixed_seam_has_representative": True,
    "unrestricted_moving_seam_has_uniform_bound": False,
    "primitive_and_square_rows_resolved": False,
    "verdict": "endpoint and fixed seams descend explicitly; moving seams still need uniform source control",
}

out = (
    Path(__file__).parents[1]
    / "results"
    / "endpoint-fixed-seam-transpose-provenance.json"
)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
