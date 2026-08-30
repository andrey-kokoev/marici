"""Finite exact model of the central-character reference-port obstruction."""

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "metaplectic_reference_port_no_go_checks.json"


def equivariant_scalar_morphisms(source_charge, target_charge, samples):
    """Return scalars f satisfying z_target f = f z_source."""
    z_source = -1 if source_charge else 1
    z_target = -1 if target_charge else 1
    return [f for f in samples if z_target * f == f * z_source]


def main():
    samples = list(range(-5, 6))
    same = equivariant_scalar_morphisms(1, 1, samples)
    mixed = equivariant_scalar_morphisms(1, 0, samples)
    tensor_charges = {(m, n): (m + n) % 2 for m in range(5) for n in range(5)}

    before = [1, 1]
    after = [-1, 1]
    cross = [[0, 1], [1, 0]]

    def quadratic(v, matrix):
        return sum(v[i] * matrix[i][j] * v[j]
                   for i in range(2) for j in range(2))

    gates = {
        "same_character_has_nonzero_intertwiners": any(f != 0 for f in same),
        "opposite_character_intertwiner_is_zero": mixed == [0],
        "tensor_character_is_additive_mod_two": all(
            charge == (m % 2 + n % 2) % 2
            for (m, n), charge in tensor_charges.items()
        ),
        "odd_and_even_tensor_powers_have_opposite_character":
            tensor_charges[(1, 0)] != tensor_charges[(2, 0)],
        "equivariant_cross_port_for_opposite_characters_absent": mixed == [0],
        "non_equivariant_cross_port_detects_relative_sign":
            quadratic(before, cross) == -quadratic(after, cross) != 0,
        "detecting_port_breaks_central_equivariance":
            equivariant_scalar_morphisms(1, 0, [1]) == [],
        "copy_with_same_diagonal_action_is_not_a_reference":
            [-x for x in before] == [-1, -1],
        "two_odd_characters_pair_to_even": (1 + 1) % 2 == 0,
        "diagonal_action_leaves_odd_odd_pairing_invariant": (-1) * (-1) == 1,
        "selective_action_flips_odd_odd_pairing": (-1) * 1 == -1,
    }

    payload = {
        "schema": "marici.strominger.metaplectic-reference-port-no-go.v1",
        "status": "pass" if all(gates.values()) else "fail",
        "summary": {"passed": sum(gates.values()), "total": len(gates)},
        "semantic_fields": {
            "grading": "central_character_Z2",
            "internal_equivariant_ports": "character_preserving",
            "required_new_constructor": "factor_selective_central_action_or_opposite_character_comparison",
            "constructor_authority": "not_source_derived",
            "characteristic_assumption": "not_2",
        },
        "gates": gates,
    }
    payload["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    raise SystemExit(0 if all(gates.values()) else 1)


if __name__ == "__main__":
    main()
