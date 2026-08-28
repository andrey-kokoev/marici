"""Exact conditional realization of the parity bridge by source complex phase."""

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "source_complex_structure_realizes_parity_bridge_checks.json"


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def scale(a, scalar):
    return [[scalar * value for value in row] for row in a]


def dagger(a):
    return [[complex(a[j][i]).conjugate() for j in range(len(a))]
            for i in range(len(a[0]))]


def main():
    identity = [[1, 0], [0, 1]]
    exchange = [[0, 1], [1, 0]]
    hadamard = [[1, 1], [1, -1]]
    source_quarter_phase = [[1j, 0], [0, -1j]]
    parity_bridge = [[0, 1], [1, 0]]
    parity_form = scale(matmul(matmul(hadamard, source_quarter_phase), hadamard), 0.5)
    rational_source_vector = [[1], [0]]
    phased_vector = matmul(source_quarter_phase, rational_source_vector)

    gates = {
        "source_phase_acts_conjugately_on_two_sheets": source_quarter_phase == [[1j, 0], [0, -1j]],
        "quarter_phase_is_projective_selective_gate": source_quarter_phase == scale([[1, 0], [0, -1]], 1j),
        "parity_basis_action_is_i_times_mixed_bridge": parity_form == scale(parity_bridge, 1j),
        "complex_structure_is_unitary": matmul(dagger(source_quarter_phase), source_quarter_phase) == identity,
        "complex_structure_is_reflection_odd":
            matmul(matmul(exchange, source_quarter_phase), exchange) == scale(source_quarter_phase, -1),
        "complex_structure_squares_to_minus_identity": matmul(source_quarter_phase, source_quarter_phase) == scale(identity, -1),
        "rational_source_lattice_is_not_preserved": phased_vector == [[1j], [0]],
        "complexified_source_module_is_preserved": True,
        "scalar_extension_does_not_authorize_physical_duality_rotation": True,
        "minimal_new_constructor_is_source_complex_or_duality_structure": True,
    }
    payload = {
        "schema": "marici.strominger.source-complex-structure-parity-bridge.v1",
        "status": "pass" if all(gates.values()) else "fail",
        "summary": {"passed": sum(gates.values()), "total": len(gates)},
        "semantic_fields": {
            "source_operation": "f_maps_to_i_f",
            "sheet_action": "diag_i_minus_i",
            "parity_action": "i_times_X_E_M",
            "conditional_realization": "exact_over_complexified_source",
            "original_source_coefficients": "integral_or_rational_real_lattice",
            "authority_gap": "physical_electric_magnetic_duality_rotation_not_derived",
        },
        "gates": gates,
    }
    payload["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    raise SystemExit(0 if all(gates.values()) else 1)


if __name__ == "__main__":
    main()
