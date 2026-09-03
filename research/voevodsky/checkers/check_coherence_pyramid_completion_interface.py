from __future__ import annotations

import copy
import json
from fractions import Fraction
from pathlib import Path


INTERFACE = Path("research/voevodsky/coherence-pyramid-completion-interface.json")


def admit(certificate: dict[str, object]) -> tuple[bool, str]:
    ordered_boolean_gates = [
        "finite_forms_source_derived",
        "candidate_form_source_derived",
        "comparison_maps_source_derived",
        "common_core_dense",
        "candidate_form_closable",
        "closure_domain_identified",
        "restriction_core_invariant",
        "mosco_or_strong_resolvent_witness",
        "closed_limit_positive",
        "finite_radicals_declared",
        "limit_radical_declared",
        "radical_stability",
        "comparison_descends_to_quotients",
        "restriction_completion_cells",
    ]
    for gate in ordered_boolean_gates:
        if certificate.get(gate) is not True:
            return False, gate
    if Fraction(str(certificate["positive_quotient_coercivity_bound"])) <= 0:
        return False, "positive_quotient_coercivity_bound"
    if Fraction(str(certificate["positive_reduced_minimum_modulus"])) <= 0:
        return False, "positive_reduced_minimum_modulus"
    return True, "admitted"


def main() -> None:
    interface = json.loads(INTERFACE.read_text(encoding="utf-8"))
    assert interface["partial"] is True
    assert len(interface["refusals"]) == 6

    valid: dict[str, object] = {
        "finite_forms_source_derived": True,
        "candidate_form_source_derived": True,
        "comparison_maps_source_derived": True,
        "common_core_dense": True,
        "candidate_form_closable": True,
        "closure_domain_identified": True,
        "restriction_core_invariant": True,
        "mosco_or_strong_resolvent_witness": True,
        "closed_limit_positive": True,
        "finite_radicals_declared": True,
        "limit_radical_declared": True,
        "radical_stability": True,
        "comparison_descends_to_quotients": True,
        "positive_quotient_coercivity_bound": "1/3",
        "positive_reduced_minimum_modulus": "1/2",
        "restriction_completion_cells": True,
    }
    assert admit(valid) == (True, "admitted")

    mutations: dict[str, tuple[str, object, str]] = {
        "negative_limit": ("closed_limit_positive", False, "closed_limit_positive"),
        "domain_escape": ("candidate_form_closable", False, "candidate_form_closable"),
        "new_radical": ("radical_stability", False, "radical_stability"),
        "quotient_coercivity_loss": ("positive_quotient_coercivity_bound", "0/1", "positive_quotient_coercivity_bound"),
        "minimum_modulus_collapse": ("positive_reduced_minimum_modulus", "0/1", "positive_reduced_minimum_modulus"),
        "circular_comparison": ("comparison_maps_source_derived", False, "comparison_maps_source_derived"),
    }
    refusals: dict[str, str] = {}
    for hostile, (field, value, expected) in mutations.items():
        fixture = copy.deepcopy(valid)
        fixture[field] = value
        admitted, reason = admit(fixture)
        assert not admitted and reason == expected
        refusals[hostile] = reason

    result = {
        "schema": "marici.voevodsky.coherence-pyramid-completion-interface-check.v1",
        "status": "partial_completion_constructor_verified",
        "valid_fixture_admitted": True,
        "hostile_fixture_count": len(refusals),
        "hostile_refusals": refusals,
        "completion_functor_claimed": False,
        "next_gate": "certificate transport under partial composition",
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
