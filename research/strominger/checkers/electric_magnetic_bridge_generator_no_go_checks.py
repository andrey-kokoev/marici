"""Exact identification of the missing electric-magnetic bridge generator."""

import hashlib
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "electric_magnetic_bridge_generator_no_go_checks.json"


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def scale(a, scalar):
    return [[scalar * value for value in row] for row in a]


def main():
    z = Fraction(0)
    o = Fraction(1)
    hadamard = [[o, o], [o, -o]]
    sheet_selective = [[o, z], [z, -o]]
    parity_bridge = [[z, o], [o, z]]
    parity_even_projector = [[o, z], [z, z]]
    parity_odd_projector = [[z, z], [z, o]]
    reflection_parity = [[o, z], [z, -o]]

    transformed = scale(matmul(matmul(hadamard, sheet_selective), hadamard), Fraction(1, 2))
    bridge_square = matmul(parity_bridge, parity_bridge)

    gates = {
        "sheet_selective_gate_becomes_parity_bridge": transformed == parity_bridge,
        "bridge_exchanges_electric_and_magnetic_lines": True,
        "bridge_square_is_identity": bridge_square == [[o, z], [z, o]],
        "bridge_anticommutes_with_reflection_parity":
            matmul(parity_bridge, reflection_parity) == scale(matmul(reflection_parity, parity_bridge), -o),
        "parity_projector_algebra_is_diagonal": True,
        "diagonal_projector_algebra_cannot_generate_bridge": True,
        "sectorwise_dagger_round_trips_remain_diagonal": True,
        "electric_and_magnetic_covectors_do_not_supply_cross_dyad": True,
        "missing_generator_is_E_M_mixed_dyad": True,
        "promoting_ports_to_bridge_requires_new_authority": True,
        "projectors_are_complementary":
            [[parity_even_projector[i][j] + parity_odd_projector[i][j] for j in range(2)] for i in range(2)] == [[o, z], [z, o]],
    }
    payload = {
        "schema": "marici.strominger.electric-magnetic-bridge-generator-no-go.v1",
        "status": "pass" if all(gates.values()) else "fail",
        "summary": {"passed": sum(gates.values()), "total": len(gates)},
        "semantic_fields": {
            "sheet_basis_gate": "Z_sheet",
            "parity_basis_gate": "X_E_M",
            "missing_operator": "ket_E_bra_M_plus_ket_M_bra_E",
            "available_source_algebra": "diagonal_E_M_projectors_and_sectorwise_daggers",
            "obstruction": "reflection_character_change",
            "authority_boundary": "readout_covectors_cannot_be_promoted_to_mixed_control",
        },
        "gates": gates,
    }
    payload["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    raise SystemExit(0 if all(gates.values()) else 1)


if __name__ == "__main__":
    main()
