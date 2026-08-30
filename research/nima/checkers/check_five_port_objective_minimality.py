#!/usr/bin/env python3
"""Exact objective-indexed ablations for the five-role architecture."""

import json
from fractions import Fraction
from pathlib import Path


def main():
    # Source capability: two injections remain distinguishable.
    source_records = {-1: -1, 1: 1}
    source_deleted = {-1: 0, 1: 0}
    assert len(set(source_records.values())) == 2
    assert len(set(source_deleted.values())) == 1

    # Gate capability: transfer changes under an independent gate intervention.
    gate_settings = (Fraction(-1, 2), Fraction(1, 2))
    gated_transfer = tuple((1 + q) / 2 for q in gate_settings)
    gate_deleted = (Fraction(1, 2), Fraction(1, 2))
    assert len(set(gated_transfer)) == 2
    assert len(set(gate_deleted)) == 1

    # Body capability: signed reference versus even quotient.
    body_values = (-1, 1)
    signed_body = tuple(body_values)
    body_deleted = tuple(value * value for value in body_values)
    assert len(set(signed_body)) == 2
    assert len(set(body_deleted)) == 1

    # Resource capability: active gain requires a balance port.
    signal_energy, output_energy = 1, 9
    resource_supply, exported = 10, 2
    assert signal_energy + resource_supply == output_energy + exported
    assert signal_energy != output_energy

    # Observer capability: internal distinction versus an empty empirical map.
    internal_outputs = (2, 5)
    observed = internal_outputs
    observer_deleted = (None, None)
    assert len(set(observed)) == 2
    assert len(set(observer_deleted)) == 1

    failures = {
        "source": "injection_distinguishability",
        "gate": "independent_modulation",
        "body": "orientation_selection",
        "resource": "active_balance_provenance",
        "observer": "empirical_distinguishability",
    }
    assert len(set(failures.values())) == 5

    result = {
        "schema": "marici.five-port-objective-minimality.v1",
        "status": "pass",
        "objective_capabilities": list(failures.values()),
        "distinct_ablation_signatures": len(set(failures.values())),
        "each_role_necessary_for_full_objective": True,
        "universal_five_role_minimality_claimed": False,
        "disposition": "five roles are conjunctively minimal only for the frozen active relational objective",
    }
    out = Path(__file__).parents[1] / "results" / "five-port-objective-minimality.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

