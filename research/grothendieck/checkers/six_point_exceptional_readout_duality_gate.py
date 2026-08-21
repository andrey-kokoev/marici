"""Exact underdetermination test for the six-point exceptional readout pairing."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from sympy import Matrix, eye, zeros


ROOT = Path(__file__).resolve().parents[3]
INPUTS = {
    "physical_congruence": ROOT / "research/grothendieck/results/physical-readout-congruence.json",
    "reflection": ROOT / "research/benincasa/string-six-point-shift-coherence.json",
    "cyclic_atlas": ROOT / "research/benincasa/string-six-point-shift-cyclic-atlas.json",
    "disk_all_arity": ROOT / "research/nima/results/string-disk-readout-dihedral-all-arity.json",
}
OUT = ROOT / "research/grothendieck/results/six-point-exceptional-readout-duality-gate.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


for path in INPUTS.values():
    assert path.is_file(), path

data = {
    name: json.loads(path.read_text(encoding="utf-8"))
    for name, path in INPUTS.items()
}

assert data["physical_congruence"]["sector_controls"]["string_six_point_exceptional_module"][
    "commutator_descent_status"
] == "untyped"
assert data["reflection"]["source_row_covariant"] is True
assert data["reflection"]["reflection_labels_disambiguated"] is True
assert data["cyclic_atlas"]["global_symbol_shift_rank"] == 8
assert data["cyclic_atlas"]["cyclic_shift_holonomy"] == "identity"
assert data["cyclic_atlas"]["source_row_return_after_three"] is True
assert data["disk_all_arity"]["passed"] is True


def permutation_matrix(permutation: tuple[int, ...]) -> Matrix:
    matrix = zeros(len(permutation), len(permutation))
    for source, target in enumerate(permutation):
        matrix[target, source] = 1
    return matrix


# An exact rank-eight dihedral control with the same abstract covariance type:
# two 3-cycles and two fixed directions. It is not asserted to be the physical
# six-point module; it isolates what coefficient covariance can and cannot
# logically force about a partner representation.
rotation_perm = (1, 2, 0, 4, 5, 3, 6, 7)
reflection_perm = (0, 2, 1, 3, 5, 4, 6, 7)
rotation = permutation_matrix(rotation_perm)
reflection = permutation_matrix(reflection_perm)
identity = eye(8)

assert rotation**3 == identity
assert reflection**2 == identity
assert reflection * rotation * reflection == rotation**2

# Formal dual model. For a permutation representation the contragredient
# matrices equal the original matrices. Evaluation P=I is strictly invariant.
formal_dual_rotation = rotation.inv().T
formal_dual_reflection = reflection.inv().T
formal_pairing = identity
formal_defects = {
    "rotation": rotation.T * formal_pairing * formal_dual_rotation - formal_pairing,
    "reflection": reflection.T * formal_pairing * formal_dual_reflection - formal_pairing,
}
assert all(defect == zeros(8, 8) for defect in formal_defects.values())
assert formal_pairing.det() == 1

# Equally compatible coefficient-only input can be paired with a trivial
# partner action. Covariance then forces each column of P into the invariant
# subspace of the coefficient representation. That subspace has dimension 4,
# so every such P is singular and no perfect physical pairing exists.
stacked_constraints = (rotation.T - identity).col_join(reflection.T - identity)
invariant_covectors = stacked_constraints.nullspace()
invariant_dimension = len(invariant_covectors)
assert invariant_dimension == 4

trivial_partner_example = Matrix.hstack(*invariant_covectors, *([zeros(8, 1)] * 4))
assert trivial_partner_example.rank() == invariant_dimension
assert trivial_partner_example.det() == 0
assert rotation.T * trivial_partner_example == trivial_partner_example
assert reflection.T * trivial_partner_example == trivial_partner_example

# A deliberately chosen non-invariant full-rank candidate exposes the exact
# defect matrices that the future source-derived pairing must annihilate.
naive_pairing = identity
naive_defects = {
    "rotation": rotation.T * naive_pairing - naive_pairing,
    "reflection": reflection.T * naive_pairing - naive_pairing,
}
assert any(defect != zeros(8, 8) for defect in naive_defects.values())

out = {
    "schema": "marici.grothendieck.six_point_exceptional_readout_duality_gate.v1",
    "status": "exact_underdetermination_theorem",
    "inputs": {
        str(path.relative_to(ROOT)).replace("\\", "/"): digest(path)
        for path in INPUTS.values()
    },
    "frozen_evidence": {
        "coefficient_module_rank": 8,
        "reflection_covariant": True,
        "cyclic_holonomy": "identity",
        "ordinary_disk_period_D6_abelianization": "C2 x C2",
        "exceptional_global_physical_cycle_constructed": False,
    },
    "two_exact_completions": {
        "formal_dual": {
            "partner_action": "contragredient coefficient action",
            "pairing": "evaluation matrix I_8",
            "covariant": True,
            "nondegenerate": True,
            "source_or_physical_authorization": False,
        },
        "trivial_partner": {
            "partner_action": "trivial rank-eight action",
            "maximum_covariant_pairing_rank": invariant_dimension,
            "perfect_pairing_exists": False,
        },
    },
    "logical_conclusion": (
        "The same frozen coefficient covariance admits a tautological formal-dual "
        "completion and a trivial-partner completion with no perfect pairing. "
        "Therefore coefficient covariance alone cannot determine the physical readout."
    ),
    "missing_source_data": [
        "a source-derived global cycle module Gamma_source",
        "its action matrices for the same cyclic and reflection generators",
        "a source-normalized pairing matrix P",
        "a physical nonzero or nondegeneracy criterion",
    ],
    "future_exact_test": {
        "covariance_defect": "D_g = R_N(g)^T P R_Gamma(g) - P",
        "pass_condition": "all D_g vanish on a generating set and P meets the physical rank criterion",
        "commutator_test": "evaluate the induced physical observable representation on source commutator generators",
    },
    "deliberate_failure": {
        "naive_claim": "rank-eight coefficient covariance canonically supplies the six-point physical pairing",
        "claim_holds": False,
        "formal_dual_is_tautological": True,
        "trivial_partner_maximum_rank": invariant_dimension,
        "required_perfect_rank": 8,
        "pairing_rank_deficit": 8 - invariant_dimension,
    },
    "verdict": {
        "formal_invariant_dual_pairing_exists": True,
        "formal_pairing_is_physical_evidence": False,
        "source_derived_exceptional_pairing_exists": False,
        "coefficient_covariance_forces_physical_descent": False,
        "six_point_exceptional_commutator_descent_remains_untyped": True,
        "ordinary_disk_all_arity_result_affected": False,
    },
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
print(json.dumps(out))
