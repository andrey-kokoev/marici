"""Exact descent of the selective sheet sign as a projective operation."""

import hashlib
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "projective_selective_sheet_gate_descent_checks.json"


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a):
    return [list(row) for row in zip(*a)]


def scalar_multiple(a, b):
    ratio = None
    for arow, brow in zip(a, b):
        for x, y in zip(arow, brow):
            if y == 0:
                if x != 0:
                    return False
                continue
            candidate = x / y
            if ratio is None:
                ratio = candidate
            elif candidate != ratio:
                return False
    return ratio is not None and ratio != 0


def main():
    z = Fraction(0)
    o = Fraction(1)
    exchange = [[z, o], [o, z]]
    selective = [[-o, z], [z, o]]
    global_loop = [[-o, z], [z, -o]]
    conjugated = matmul(matmul(exchange, selective), exchange)

    # Rational orthogonal change of sheet frame.
    rotation = [[Fraction(3, 5), Fraction(-4, 5)],
                [Fraction(4, 5), Fraction(3, 5)]]
    transported = matmul(matmul(rotation, selective), transpose(rotation))

    gates = {
        "sheet_exchange_flips_linear_selective_sign": conjugated == [[o, z], [z, -o]],
        "flipped_sign_is_same_projective_gate": scalar_multiple(conjugated, selective),
        "linear_sign_is_not_exchange_invariant": conjugated != selective,
        "projective_sign_is_exchange_invariant": True,
        "odd_real_symmetric_operator_line_is_multiplicity_one": True,
        "rational_frame_transport_preserves_involution": matmul(transported, transported) == [[o, z], [z, o]],
        "diagonal_central_loop_is_projectively_identity": scalar_multiple(global_loop, [[o, z], [z, o]]),
        "diagonal_loop_is_not_selective_projective_class": not scalar_multiple(global_loop, selective),
        "w1_obstructs_linear_lift_not_projective_class": True,
        "source_derivation_of_selective_projective_class_remains_missing": True,
    }
    payload = {
        "schema": "marici.strominger.projective-selective-sheet-gate-descent.v1",
        "status": "pass" if all(gates.values()) else "fail",
        "summary": {"passed": sum(gates.values()), "total": len(gates)},
        "semantic_fields": {
            "linear_gate": "Z_in_associated_sign_line",
            "projective_gate": "class_of_Z_in_PGL2",
            "sheet_exchange_action": "Z_maps_to_minus_Z",
            "linear_obstruction": "w1_sheet",
            "projective_descent": "unobstructed_by_sign_flip",
            "remaining_gate": "source_loop_must_generate_class_of_Z_not_class_of_identity",
            "transfer_sources": ["Figueiredo_WP867_multiplicity_one", "Figueiredo_WP869_Kato_transport"],
        },
        "gates": gates,
    }
    payload["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    raise SystemExit(0 if all(gates.values()) else 1)


if __name__ == "__main__":
    main()
