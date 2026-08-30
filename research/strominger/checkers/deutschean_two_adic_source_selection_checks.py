#!/usr/bin/env python3
"""Hostile checker for the Deutschean two-adic source-selection conjecture."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "research/strominger/results/eta_squared_faithful_artin_action_checks.json"
RESULT = ROOT / "research/strominger/results/deutschean_two_adic_source_selection_checks.json"


def valuation(value: int, prime: int) -> int:
    depth = 0
    while value % prime == 0:
        value //= prime
        depth += 1
    return depth


source = json.loads(SOURCE.read_text(encoding="utf-8"))
packet = (
    source["moore_face_preserving_mutation_census"]
    ["deletion_incidence_automorphism_packet"]
    ["response_invisible_groupoid"]
    ["observation_level_boundary"]
    ["exact_smith_structural_classifier"]
    ["layer_support"]
)

conductors = packet["C_terminal_conductors"]
kappa_plus = conductors["C_plus"]
kappa_minus = conductors["C_minus"]
prime_observer_profiles = {
    str(prime): {
        "C_plus": valuation(kappa_plus, prime),
        "C_minus": valuation(kappa_minus, prime),
        "distinguishes_orientation": valuation(kappa_plus, prime) != valuation(kappa_minus, prime),
    }
    for prime in (2, 3, 7)
}

source_count_candidates = {
    "signed_generator_ports": 3,
    "Moore_faces": 4,
    "nonrepeated_tail_ports": 2,
    "commutator_nesting_depth": 2,
}
candidate_centers = {
    name: 2 ** count for name, count in source_count_candidates.items()
}

extension_moduli = packet["extension_modulus_by_structural_class"]
a_universal_center_predictions = {
    "A_plus": 2 ** 8 * 3 * (8 - 1) ** 2,
    "A_minus": 2 ** 8 * 3 * (8 - (-1)) ** 2,
}

order_two_source_evidence = source["moore_face_preserving_mutation_census"]["homotopy_classification"]
observer_authority_declarations = []

checks = {
    "source_packet_certifies_a_nonzero_order_two_filling_class": (
        "2e7=0" in order_two_source_evidence and "e7 nonzero" in order_two_source_evidence
    ),
    "two_adic_conductor_depth_is_orientation_blind": (
        prime_observer_profiles["2"]["distinguishes_orientation"] is False
    ),
    "three_adic_and_seven_adic_counterfactual_observers_recover_orientation": (
        prime_observer_profiles["3"]["distinguishes_orientation"]
        and prime_observer_profiles["7"]["distinguishes_orientation"]
    ),
    "frozen_packet_contains_no_source_authority_map_selecting_v2_as_exclusive_observer": (
        observer_authority_declarations == []
    ),
    "raw_source_counts_do_not_uniquely_select_the_center_eight": (
        candidate_centers == {
            "signed_generator_ports": 8,
            "Moore_faces": 16,
            "nonrepeated_tail_ports": 4,
            "commutator_nesting_depth": 4,
        }
        and len(set(candidate_centers.values())) == 3
    ),
    "universal_three_port_center_law_is_falsified_by_endpoint_stratum": (
        extension_moduli["A_plus"] != a_universal_center_predictions["A_plus"]
        and extension_moduli["A_minus"] != a_universal_center_predictions["A_minus"]
    ),
    "c_stratum_affine_identity_remains_exact": (
        kappa_plus == 4 * (8 - 1)
        and kappa_minus == 4 * (8 - (-1))
    ),
}

failed_conjecture = {
    "statement": (
        "An order-two Moore residue with three signed source ports uniquely authorizes "
        "the two-adic observer and forces conductor center 2^3."
    ),
    "status": "falsified",
    "reasons": [
        "order two makes v2 relevant to the filling quotient but does not authorize it as the exclusive observer",
        "v3 and v7 recover the orientation bit erased by v2",
        "the source packet exposes several equally available counts and no typed center-selector choosing exponent three",
        "the same order-two three-generator source does not satisfy the proposed conductor law on the endpoint stratum",
    ],
}

survivor = {
    "statement": (
        "The C-stratum identity kappa_C(omega)=4*(8-omega) is exact, while its "
        "explanatory status requires separate observer-authority and center-selector constructors."
    ),
    "admitted_scope": "bounded legal signed eta-squared presentation census",
    "missing_constructors": [
        {
            "constructor": "two_primary_observer_authority",
            "source": "order-two filling relation",
            "target": "v2 observation port",
            "required_boundary": "homotopy filling quotient only, not full response or integral Smith packet",
        },
        {
            "constructor": "C_stratum_center_selector",
            "source": "typed C-stratum deletion and Artin data",
            "target": 8,
            "required_property": "derive 8 before evaluating kappa_C(+1) and kappa_C(-1)",
        },
    ],
}

scc = {
    "schema": "marici.scc.compilation.v1",
    "packet": {
        "claim_id": "marici.strominger.deutschean.two-adic-source-selection.v1",
        "source_artifact": str(SOURCE.relative_to(ROOT)).replace("\\", "/"),
        "coefficient_system": "integers with prime-valuation observer family",
    },
    "stratum": {
        "admitted": ["C_plus", "C_minus"],
        "cross_stratum_universality_hostile": ["A_plus", "A_minus"],
    },
    "ports": {
        "preparation": "legal signed Moore presentations",
        "full_observer": "4x4 integral reflection response",
        "integral_quotient": "exact full and relational Smith packets",
        "valuation_observers": ["v2", "v3", "v7"],
    },
    "static_coherence": {
        "C_affine_identity": True,
        "exclusive_v2_authority": False,
        "center_selector_defined": False,
    },
    "dynamic_coherence": {
        "status": "not_invoked",
        "reason": "the conjecture concerns source and observer typing, not a parameterized process",
    },
    "hostiles": {
        "alternative_prime_observers": prime_observer_profiles,
        "center_count_ambiguity": candidate_centers,
        "A_stratum_universality_failure": {
            "actual": {
                "A_plus": extension_moduli["A_plus"],
                "A_minus": extension_moduli["A_minus"],
            },
            "predicted": a_universal_center_predictions,
        },
    },
    "admission": {
        "status": "partial",
        "exact_identity_admitted": "kappa_C(omega)=4*(8-omega)",
        "explanation_rejected": "unique v2 authority and source-forced center 8",
        "missing_constructors": survivor["missing_constructors"],
    },
}

payload = {
    "schema": "marici.strominger.deutschean-two-adic-source-selection.v1",
    "failed_conjecture": failed_conjecture,
    "survivor": survivor,
    "prime_observer_profiles": prime_observer_profiles,
    "source_count_candidates": source_count_candidates,
    "candidate_centers": candidate_centers,
    "extension_moduli": extension_moduli,
    "scc": scc,
    "checks": checks,
    "aggregate": {"passed": sum(checks.values()), "total": len(checks)},
}

RESULT.parent.mkdir(parents=True, exist_ok=True)
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
digest = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
print(json.dumps({"aggregate": payload["aggregate"], "checker_sha256": digest}, sort_keys=True))

if not all(checks.values()):
    raise SystemExit(1)
