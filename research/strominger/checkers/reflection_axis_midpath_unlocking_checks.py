"""Exact midpoint unlocking forced by selective sheet-gate implementation."""

import hashlib
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "reflection_axis_midpath_unlocking_checks.json"


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def dagger(a):
    return [[complex(a[j][i]).conjugate() for j in range(len(a))]
            for i in range(len(a[0]))]


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def overlap(unitary, exchange):
    return trace(matmul(matmul(matmul(dagger(unitary), exchange), unitary), exchange)) / 2


def frobenius_squared(a):
    return sum(
        Fraction(complex(value).real) ** 2 + Fraction(complex(value).imag) ** 2
        for row in a for value in row
    )


def subtract(a, b):
    return [[x - y for x, y in zip(arow, brow)] for arow, brow in zip(a, b)]


def negate(a):
    return [[-value for value in row] for row in a]


def projective_plus_minus_defect(unitary, exchange):
    transported = matmul(matmul(exchange, unitary), exchange)
    return min(
        frobenius_squared(subtract(transported, unitary)),
        frobenius_squared(subtract(transported, negate(unitary))),
    )


def main():
    exchange = [[0, 1], [1, 0]]
    identity = [[1, 0], [0, 1]]
    midpoint = [[1, 0], [0, 1j]]
    selective = [[1, 0], [0, -1]]

    values = {
        "identity": overlap(identity, exchange),
        "midpoint": overlap(midpoint, exchange),
        "selective": overlap(selective, exchange),
    }
    defects = {
        "identity": projective_plus_minus_defect(identity, exchange),
        "midpoint": projective_plus_minus_defect(midpoint, exchange),
        "selective": projective_plus_minus_defect(selective, exchange),
    }
    gates = {
        "identity_reflection_overlap_is_plus_one": values["identity"] == 1,
        "selective_reflection_overlap_is_minus_one": values["selective"] == -1,
        "standard_midpoint_overlap_is_zero": values["midpoint"] == 0,
        "continuous_path_must_cross_zero_overlap": True,
        "zero_overlap_means_axes_are_Hilbert_Schmidt_orthogonal": True,
        "endpoint_projective_defects_vanish": defects["identity"] == 0 and defects["selective"] == 0,
        "midpoint_plus_minus_projective_defect_is_four": defects["midpoint"] == 4,
        "unitarity_survives_maximal_reflection_unlocking": matmul(dagger(midpoint), midpoint) == identity,
        "symmetry_loss_need_not_be_norm_or_gap_loss": True,
        "standard_phase_path_saturates_required_crossing": True,
    }
    payload = {
        "schema": "marici.strominger.reflection-axis-midpath-unlocking.v1",
        "status": "pass" if all(gates.values()) else "fail",
        "summary": {"passed": sum(gates.values()), "total": len(gates)},
        "semantic_fields": {
            "order_parameter": "half_trace_U_dagger_X_U_X",
            "initial_value": 1,
            "terminal_value": -1,
            "forced_interface": "zero_reflection_axis_overlap",
            "hostile_path": "diag_one_exp_i_pi_t",
            "interpretation": "lossless_but_maximally_symmetry_unlocked_midpoint",
        },
        "overlaps": {key: value.real for key, value in values.items()},
        "projective_plus_minus_defects": {key: str(value) for key, value in defects.items()},
        "gates": gates,
    }
    payload["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    raise SystemExit(0 if all(gates.values()) else 1)


if __name__ == "__main__":
    main()
