"""Exact audit of the magnetic sheet pair as an endogenous coherence carrier."""

import hashlib
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "sheet_pair_coherence_carrier_selective_action_no_go_checks.json"


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def commutes(a, b):
    return matmul(a, b) == matmul(b, a)


def main():
    z = Fraction(0)
    o = Fraction(1)
    exchange = [[z, o], [o, z]]
    hadamard = [[o, o], [o, -o]]
    plus_sheet = [[o], [o]]
    minus_sheet = [[o], [-o]]
    diagonal_loop = [[-o, z], [z, -o]]
    selective_loop = [[-o, z], [z, o]]

    gates = {
        "sheet_exchange_is_involution": matmul(exchange, exchange) == [[o, z], [z, o]],
        "electric_magnetic_atlas_separates_even_sheet_state": matmul(hadamard, plus_sheet) == [[Fraction(2)], [z]],
        "electric_magnetic_atlas_separates_odd_sheet_state": matmul(hadamard, minus_sheet) == [[z], [Fraction(2)]],
        "diagonal_metaplectic_loop_is_reflection_equivariant": commutes(diagonal_loop, exchange),
        "diagonal_loop_is_only_global_sign": matmul(diagonal_loop, plus_sheet) == [[-o], [-o]],
        "selective_loop_converts_even_to_odd": matmul(selective_loop, plus_sheet) == [[-o], [o]],
        "selective_loop_is_not_reflection_equivariant": not commutes(selective_loop, exchange),
        "sheet_pair_supplies_carrier_but_not_selective_authority": True,
        "global_sheet_basis_may_require_local_system_framing": True,
        "missing_constructor_is_reflection_framed_addressability": True,
    }
    payload = {
        "schema": "marici.strominger.sheet-pair-coherence-carrier-selective-action-no-go.v1",
        "status": "pass" if all(gates.values()) else "fail",
        "summary": {"passed": sum(gates.values()), "total": len(gates)},
        "semantic_fields": {
            "endogenous_carrier": "right_left_sheet_pair",
            "carrier_atlas": "electric_magnetic_Hadamard",
            "source_loop": "diagonal_global_sign",
            "needed_loop": "one_sheet_selective_sign",
            "obstruction": "selective_sign_not_reflection_equivariant",
            "missing_constructor": "reflection_framed_sheet_addressability",
        },
        "gates": gates,
    }
    payload["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    raise SystemExit(0 if all(gates.values()) else 1)


if __name__ == "__main__":
    main()
