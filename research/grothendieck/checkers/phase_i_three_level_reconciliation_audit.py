"""Exact reconciliation audit for Carrier, pi_0, and D4-abelianized levels."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
INPUTS = {
    "carrier_closure": ROOT / "research/grothendieck/results/phase-i-operation-inventory-closure.json",
    "additive_completion": ROOT / "research/grothendieck/results/phase-i-monoidal-additive-completion.json",
    "endomorphism_semiring": ROOT / "research/nima/results/phase-i-endomorphism-semiring.json",
    "intrinsic_primes": ROOT / "research/nima/results/phase-i-intrinsic-primes.json",
    "unit_automorphism": ROOT / "research/nima/results/phase-i-unit-automorphism-obstruction.json",
    "abelianized_rig": ROOT / "research/nima/results/phase-i-abelianized-rig-groupoid.json",
    "m2_sector": ROOT / "research/nima/results/phase-i-m2-ward-d4-factorization.json",
    "flavor_comparison": ROOT / "research/nima/results/phase-i-flavor-lens-readout-abelianization.json",
}
OUT = ROOT / "research/grothendieck/results/phase-i-three-level-reconciliation-audit.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


for path in INPUTS.values():
    assert path.is_file(), path

data = {
    name: json.loads(path.read_text(encoding="utf-8"))
    for name, path in INPUTS.items()
}

closure = data["carrier_closure"]
additive = data["additive_completion"]
semiring = data["endomorphism_semiring"]
primes = data["intrinsic_primes"]
unit_obstruction = data["unit_automorphism"]
rig = data["abelianized_rig"]
m2 = data["m2_sector"]
flavor = data["flavor_comparison"]

# Level 1: the admitted full-Carrier inventory stays closed.
assert closure["passing_multiplication_candidates"] == []
assert closure["verdict"]["carrier_tensor_and_unit_derived"] is False
assert closure["verdict"]["phase_i_passed"] is False
assert closure["obstruction_vector"] == {
    "face_join_support_excess": 130,
    "surface_coproduct_injection_leg_deficit": 2,
    "unmarked_sewing_fixed_point_deficit": 1,
    "four_point_Carrier_unit_arity_residual": 2,
}

# Level 2: after the explicit monoidal relaxation, additive freeness really
# does classify a canonical multiplication on pi_0.  This corrects only the
# old decategorified verdict, never the Carrier-level one.
assert additive["compatibility_preflight"]["adopted_for_project"] is False
assert additive["verdict"]["conditional_additive_N_derived"] is True
assert semiring["verdict"]["conditional_initial_semiring_on_pi0_derived"] is True
assert semiring["verdict"]["surface_level_distributive_tensor_derived"] is False
assert primes["verdict"]["conditional_intrinsic_prime_elements_derived"] is True
assert primes["verdict"]["closed_points_of_spec_z_derived"] is False
assert primes["verdict"]["arithmetic_frobenius_derived"] is False
assert primes["verdict"]["euler_product_derived"] is False

# Level 3: noncommuting unit automorphisms forbid a full lift.  Abelianization
# is the maximal algebraic unit-compatible quotient, but it is neither a
# physical realization nor a full-information Carrier quotient.
assert unit_obstruction["finite_certificate"]["commute"] is False
assert unit_obstruction["verdict"]["lift_with_U_as_unit_on_full_D4_groupoid_exists"] is False
assert rig["unit_automorphisms"]["commutator_subgroup_order"] == 2
assert rig["unit_automorphisms"]["quotient_order"] == 4
assert rig["verdict"]["abelianized_rig_groupoid_exists"] is True
assert rig["verdict"]["quotient_is_physical_realization"] is False
assert rig["verdict"]["full_D4_information_retained"] is False

# The rank-one m=2 line factors, but is not hostile: every one-dimensional
# group representation kills the commutator.  The flavor comparison already
# falsifies the stronger universal-coefficient reading and leaves only a
# physical-readout shadow as a live possibility.
assert m2["representation"]["dimension"] == 1
assert m2["representation"]["factors_through_D4_ab"] is True
assert m2["verdict"]["all_sector_factorization_proved"] is False
assert flavor["coefficient_lens"]["factors_through_S3_abelianization"] is False
assert flavor["physical_readout"]["all_exact_weak_basis_invariants_preserved"] is True
assert flavor["verdict"]["abelianized_rig_is_universal_coefficient_object"] is False

out = {
    "schema": "marici.grothendieck.phase_i_three_level_reconciliation_audit.v1",
    "status": "typed_reconciliation_with_exact_controls",
    "inputs": {
        str(path.relative_to(ROOT)).replace("\\", "/"): digest(path)
        for path in INPUTS.values()
    },
    "levels": {
        "admitted_full_carrier": {
            "multiplication": "not derived",
            "phase_i_status": "closed over the admitted inventory",
            "obstruction_vector": [130, 2, 1, 2],
        },
        "conditional_pi0": {
            "hypothesis": "symmetric-monoidal disjoint-union relaxation",
            "initial_semiring": "derived by additive-endomorphism classification",
            "intrinsic_primes_and_ufd": "derived conditionally",
            "surface_tensor": "not derived",
        },
        "d4_abelianized_rig": {
            "algebraic_candidate": "derived as maximal unit-compatible automorphism quotient",
            "physical_authorization": "not derived",
            "universal_coefficient_status": "falsified by the flavor lens/readout separation",
            "remaining_status": "candidate physical-readout shadow",
        },
    },
    "correction": {
        "prior_sentence_too_broad": "initial semiring and intrinsic primes: not derived",
        "replacement": (
            "no initial semiring or primes are derived at full Carrier level; "
            "under the explicit monoidal relaxation, the pointed free additive pi_0 "
            "canonically derives the initial semiring and intrinsic primes"
        ),
    },
    "deliberate_failures": {
        "carrier_product_candidate_deficit": 1,
        "noncommuting_unit_pair_count_lower_bound": 1,
        "d4_information_killed_by_abelianization": True,
        "universal_coefficient_factorization": False,
    },
    "next_gate": (
        "Test a source-established physical invariant carrying a genuinely "
        "higher-dimensional nonabelian source action; rank-one characters "
        "cannot detect the commutator, and raw coefficient-lens factorization "
        "is already too strong"
    ),
    "verdict": {
        "nima_three_level_reconciliation_accepted": True,
        "grothendieck_full_carrier_closure_preserved": True,
        "conditional_pi0_verdict_corrected": True,
        "d4ab_rig_physically_authorized": False,
        "phase_ii_burnside_witt_authorized": False,
        "spec_z_frobenius_euler_product_derived": False,
    },
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
print(json.dumps(out))
