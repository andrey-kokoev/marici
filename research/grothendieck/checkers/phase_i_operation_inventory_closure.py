"""Typed closure audit of every admitted Phase-I operation candidate."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from sympy import Integer


ROOT = Path(__file__).resolve().parents[3]
ENTRY_27 = (
    ROOT
    / "src/ledger/20260813-27 Regional Core-Filtered Scalar-QTDS Theorem.md"
)
ENTRY_46 = (
    ROOT
    / "src/ledger/20260813-46 Closed-Circuit Resolution and the Modular "
    "Counit Target.md"
)
ENTRY_47 = (
    ROOT
    / "src/ledger/20260813-47 Derived Modular-Envelope Lift and the Physical "
    "Descent Obstruction.md"
)
ENTRY_542 = (
    ROOT
    / "src/ledger/20260818-542 Even-Arity Framed Cut Descent Follows by "
    "Quadrangulation Induction.md"
)
RESULT_DIR = ROOT / "research/grothendieck/results"
RESULTS = {
    "lens": RESULT_DIR / "arithmetic-lens-resolution-falsifier.json",
    "assembly": RESULT_DIR / "phase-i-unmarked-assembly-obstruction.json",
    "face": RESULT_DIR / "phase-i-face-coproduct-idempotence.json",
    "surface": RESULT_DIR / "phase-i-surface-disjoint-union-typing.json",
    "additive": RESULT_DIR / "phase-i-monoidal-additive-completion.json",
    "unit": RESULT_DIR / "phase-i-connected-sewing-unit-obstruction.json",
}
OUT = RESULT_DIR / "phase-i-operation-inventory-closure.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


inputs = [ENTRY_27, ENTRY_46, ENTRY_47, ENTRY_542, *RESULTS.values()]
for path in inputs:
    assert path.is_file()

evidence = {
    name: json.loads(path.read_text(encoding="utf-8"))
    for name, path in RESULTS.items()
}

# Recheck every imported verdict before composing the closure matrix.
assert evidence["lens"]["verdict"]["arithmetic_derived"] is False
assert (
    evidence["assembly"]["verdict"]
    ["unmarked_connected_binary_assembly_derived"]
    is False
)
assert evidence["face"]["verdict"]["incidence_poset_coproduct_exists"] is True
assert (
    evidence["face"]["verdict"]
    ["incidence_poset_coproduct_is_disjoint_union"]
    is False
)
assert evidence["surface"]["verdict"]["surface_disjoint_union_monoidal"] is True
assert (
    evidence["surface"]["verdict"]
    ["surface_disjoint_union_coproduct_derived"]
    is False
)
assert evidence["additive"]["verdict"]["conditional_additive_N_derived"] is True
assert evidence["additive"]["verdict"]["carrier_multiplication_derived"] is False
assert evidence["unit"]["verdict"]["framed_coefficient_unit_verified"] is True
assert evidence["unit"]["verdict"]["four_point_carrier_tensor_unit"] is False

addition_candidates = [
    {
        "candidate": "closed-face categorical join",
        "carrier_level": True,
        "categorical_coproduct": True,
        "multiplicity_sensitive": False,
        "unit_powers_free": False,
        "group_completion": "zero_group",
        "passes_literal_additive_gate": False,
    },
    {
        "candidate": "geometric surface disjoint union",
        "carrier_level": True,
        "categorical_coproduct": False,
        "multiplicity_sensitive": True,
        "unit_powers_free": True,
        "group_completion": "Z_conditionally_after_monoidal_relaxation",
        "passes_literal_additive_gate": False,
    },
]

multiplication_requirements = (
    "carrier_level",
    "coefficient_neutral",
    "total_unmarked",
    "source_equivariant",
    "unit_object_admitted",
    "distributive_over_geometric_sum",
)

multiplication_candidates = [
    {
        "candidate": "unmarked connected edge sewing",
        "carrier_level": True,
        "coefficient_neutral": True,
        "total_unmarked": False,
        "source_equivariant": False,
        "unit_object_admitted": False,
        "distributive_over_geometric_sum": False,
        "decisive_evidence": [
            "D4_x_D4_fixed_point_deficit_1",
            "stable_unit_arity_residual_2",
        ],
    },
    {
        "candidate": "fixed-core regional Cartesian product",
        "carrier_level": False,
        "coefficient_neutral": False,
        "total_unmarked": False,
        "source_equivariant": True,
        "unit_object_admitted": False,
        "distributive_over_geometric_sum": False,
        "decisive_evidence": [
            "entry_27_calls_it_coefficient_level_transfer",
            "partial_core_and_regions_are_fixed_inputs",
        ],
    },
    {
        "candidate": "framed physical-line external product",
        "carrier_level": False,
        "coefficient_neutral": False,
        "total_unmarked": False,
        "source_equivariant": True,
        "unit_object_admitted": False,
        "distributive_over_geometric_sum": False,
        "decisive_evidence": [
            "all_even_fs_Kato_coherence_passes",
            "primitive_plus_one_is_coefficient_line_generator",
            "four_point_Carrier_arity_residual_2",
        ],
    },
    {
        "candidate": "resolved Brauer-state tensor",
        "carrier_level": False,
        "coefficient_neutral": False,
        "total_unmarked": True,
        "source_equivariant": True,
        "unit_object_admitted": False,
        "distributive_over_geometric_sum": False,
        "decisive_evidence": [
            "state_category_over_Z_of_D",
            "D_to_1_augmentation_precedes_modular_envelope",
        ],
    },
    {
        "candidate": "formal finite-family pairwise tensor",
        "carrier_level": False,
        "coefficient_neutral": True,
        "total_unmarked": True,
        "source_equivariant": True,
        "unit_object_admitted": False,
        "distributive_over_geometric_sum": True,
        "decisive_evidence": [
            "not_admitted_or_source_derived",
            "finite_index_pairing_would_supply_target_multiplicity_law",
        ],
    },
]

for candidate in multiplication_candidates:
    candidate["missing_requirements"] = [
        requirement
        for requirement in multiplication_requirements
        if not candidate[requirement]
    ]
    candidate["passes_phase_i_multiplication_gate"] = not candidate[
        "missing_requirements"
    ]

passing_multiplication_candidates = [
    candidate["candidate"]
    for candidate in multiplication_candidates
    if candidate["passes_phase_i_multiplication_gate"]
]
assert passing_multiplication_candidates == []

obstruction_vector = {
    "face_join_support_excess": evidence["face"]["finite_model"]
    ["join_support_excess"],
    "surface_coproduct_injection_leg_deficit": evidence["surface"]
    ["source_typing"]["required_leg_deficit"],
    "unmarked_sewing_fixed_point_deficit": 1
    - len(
        evidence["assembly"]["finite_model"]["dihedral_fixed_gluing_pairs"]
    ),
    "four_point_Carrier_unit_arity_residual": evidence["unit"]
    ["deliberate_failure"]["observed_arity_residual"],
}
assert obstruction_vector == {
    "face_join_support_excess": 130,
    "surface_coproduct_injection_leg_deficit": 2,
    "unmarked_sewing_fixed_point_deficit": 1,
    "four_point_Carrier_unit_arity_residual": 2,
}

required_passing_candidate_count = Integer(1)
observed_passing_candidate_count = Integer(len(passing_multiplication_candidates))
passing_candidate_deficit = (
    required_passing_candidate_count - observed_passing_candidate_count
)
assert passing_candidate_deficit == 1

packet = {
    "schema": "marici.grothendieck.phase_i_operation_inventory_closure.v1",
    "demonstrated_strength": [
        "typed closure over admitted candidate inventory",
        "composition of six exact prior audits",
    ],
    "compatibility_preflight": {
        "scope": "named Phase-I candidates present in admitted sources",
        "global_impossibility_claimed": False,
        "coefficient_domain": None,
        "input_sha256": {rel(path): sha256(path) for path in inputs},
    },
    "addition_candidates": addition_candidates,
    "multiplication_requirements": list(multiplication_requirements),
    "multiplication_candidates": multiplication_candidates,
    "passing_multiplication_candidates": passing_multiplication_candidates,
    "obstruction_vector": obstruction_vector,
    "realization_invariance": {
        "framed_fs_Kato_tensor_control": True,
        "independent_common_Carrier_tensor_control": False,
        "lens_readout_invariance": False,
        "lens_torsion_orders": evidence["lens"]["smith_invariants"],
    },
    "conditional_branch": {
        "monoidal_additive_N": True,
        "monoidal_group_completion_Z": True,
        "unital_distributive_multiplication": False,
        "initial_semiring": False,
    },
    "deliberate_failure": {
        "naive_claim": (
            "at least one admitted use of tensor or product satisfies every "
            "Phase-I multiplication requirement"
        ),
        "claim_holds": False,
        "required_passing_candidate_count": int(required_passing_candidate_count),
        "observed_passing_candidate_count": int(observed_passing_candidate_count),
        "nonzero_obstruction": {
            "passing_candidate_deficit": int(passing_candidate_deficit)
        },
    },
    "verdict": {
        "literal_finite_coproduct_derived": False,
        "conditional_additive_N_and_Z_derived": True,
        "carrier_tensor_and_unit_derived": False,
        "distributivity_derived": False,
        "initial_semiring_derived": False,
        "intrinsic_multiplication_derived": False,
        "unique_factorization_or_primes_derived": False,
        "phase_i_passed": False,
        "phase_ii_authorized": False,
        "arithmetic_sector_derived": False,
    },
    "precise_next_authority_boundary": [
        "admit a new coefficient-neutral Carrier product and unit",
        "admit component-inclusion morphisms making disjoint union a coproduct",
        "or explicitly revise the finalized Phase-I requirements",
    ],
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet))
