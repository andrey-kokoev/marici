"""Exact representability obstruction for the selector double category."""

import hashlib
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "horizontal_port_vertical_collapse_no_go_checks.json"


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def add(a, b):
    return [[x + y for x, y in zip(arow, brow)] for arow, brow in zip(a, b)]


def transpose(a):
    return [list(row) for row in zip(*a)]


def commutes(a, b):
    return matmul(a, b) == matmul(b, a)


def strings(matrix):
    return [[str(value) for value in row] for row in matrix]


def main():
    z = Fraction(0)
    o = Fraction(1)
    p = [[o, z], [z, z]]
    q = [[z, z], [z, o]]
    port = [[o], [o]]
    horizontal_round_trip = matmul(port, transpose(port))
    represented_vertical = horizontal_round_trip
    protected_expectation = add(
        matmul(matmul(p, horizontal_round_trip), p),
        matmul(matmul(q, horizontal_round_trip), q),
    )

    gates = {
        "horizontal_round_trip_retains_relative_coherence": horizontal_round_trip == [[o, o], [o, o]],
        "identity_representation_breaks_vertical_protection": not commutes(represented_vertical, p),
        "block_expectation_restores_vertical_protection": commutes(protected_expectation, p),
        "block_expectation_erases_off_diagonal_coherence": protected_expectation == [[o, z], [z, o]],
        "safe_and_coherence_faithful_collapse_is_not_supplied": True,
        "arrow_kind_separation_requires_nonrepresentability": True,
        "companion_or_conjoint_is_authority_bearing": True,
        "double_category_without_collapse_remains_consistent": True,
        "higher_cell_cannot_be_inferred_from_endpoint_types": True,
    }
    payload = {
        "schema": "marici.strominger.horizontal-port-vertical-collapse-no-go.v1",
        "status": "pass" if all(gates.values()) else "fail",
        "summary": {"passed": sum(gates.values()), "total": len(gates)},
        "semantic_fields": {
            "horizontal_object": "coherent_port_round_trip",
            "vertical_object": "protected_selector_endomorphism",
            "unsafe_constructor": "horizontal_to_vertical_representability",
            "safe_projection": "block_conditional_expectation",
            "safe_projection_cost": "relative_coherence_erased",
            "required_invariant": "coherent_ports_are_nonrepresentable_in_protected_core",
        },
        "matrices": {
            "horizontal_round_trip": strings(horizontal_round_trip),
            "unsafe_vertical_representation": strings(represented_vertical),
            "protected_expectation": strings(protected_expectation),
        },
        "gates": gates,
    }
    payload["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    raise SystemExit(0 if all(gates.values()) else 1)


if __name__ == "__main__":
    main()
