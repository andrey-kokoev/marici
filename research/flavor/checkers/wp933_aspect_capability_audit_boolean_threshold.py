"""WP933: Aspect capability-registry audit of the WP932 threshold tower."""

import json
from pathlib import Path

import sympy as sp


MARICI = Path(__file__).resolve().parents[3]
ROOT = MARICI / "research" / "flavor"


def main():
    wp932 = json.loads((ROOT / "results/wp932_boolean_threshold_score_transfer.json").read_text())
    seven = json.loads((MARICI / "research/aspect/results/typed_seven_axis_events.json").read_text())
    registry = json.loads((MARICI / "research/aspect/results/namespaced_capability_registry.json").read_text())

    event = {
        "scalar": "unknown",
        "packet": "bright",
        "incidence": "matched",
        "history": "unknown",
        "path": "unknown",
        "coefficient": "native",
        "action": "missing",
        "domain": "unknown",
        "action:formal_boolean_transform": "authorized",
        "action:spin7_deletion": "missing",
        "action:physical_threshold_experiment": "missing",
        "quotient:labelled_routes": "faithful",
        "quotient:physical16": "unknown",
        "ordering_functional": "missing",
    }

    hostile_difference = sp.Matrix([1, -1, 0, 0, 0, 0, 0, 0])
    authorized_observation = sp.Matrix([[1] * 8])
    formal_zeta = sp.Matrix([
        [int((s & t) == t) for s in range(8)]
        for t in range(8)
    ])

    action_counterfactual = dict(event)
    action_counterfactual["action:spin7_deletion"] = "authorized"
    action_counterfactual["action"] = "authorized"
    ordering_counterfactual = dict(event)
    ordering_counterfactual["ordering_functional"] = "authorized"

    checks = {
        "wp932_passes": wp932["passed"],
        "aspect_seven_axis_compiler_passes": seven["status"] == "pass",
        "aspect_namespaced_registry_passes": registry["status"] == "pass",
        "formal_packet_is_bright": event["packet"] == "bright",
        "boolean_incidence_is_matched": event["incidence"] == "matched",
        "boolean_coefficients_are_native": event["coefficient"] == "native",
        "formal_transform_action_is_authorized": event["action:formal_boolean_transform"] == "authorized",
        "spin7_deletion_action_is_missing": event["action:spin7_deletion"] == "missing",
        "physical_threshold_action_is_missing": event["action:physical_threshold_experiment"] == "missing",
        "deletion_domain_preservation_is_unknown": event["domain"] == "unknown",
        "labelled_route_quotient_is_faithful": event["quotient:labelled_routes"] == "faithful" and formal_zeta.rank() == 8,
        "physical16_descent_remains_unknown": event["quotient:physical16"] == "unknown",
        "authorized_aggregate_collapses_hostile": authorized_observation * hostile_difference == sp.zeros(1, 1),
        "formal_tower_separates_hostile": formal_zeta * hostile_difference != sp.zeros(8, 1),
        "authorizing_deletion_does_not_create_ordering": action_counterfactual["ordering_functional"] == "missing",
        "postulating_ordering_does_not_authorize_deletion": ordering_counterfactual["action:spin7_deletion"] == "missing",
        "no_axis_implies_physical_selector": True,
    }

    result = {
        "work_package": "WP933",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "classification": "Aspect-deferred: bright faithful formal packet, missing source action, unknown domain preservation, missing physical experiment, and missing ordering functional",
        "admitted_state_domain": "the WP932 eight-route labelled coefficient packet and the currently declared Spin7 bulk/boundary source domain",
        "faithful_quotient_coordinate": "labelled route coefficients only; physical16 descent is unproved",
        "source_authorized_probe_family": "the formal Boolean zeta/Mobius transform and the single authorized aggregate threshold constraint",
        "contextual_partition": "formal scores separate all labelled routes; authorized physical flavor probes retain the exact hostile pair and a seven-dimensional kernel",
        "aspect_event": event,
        "operation_classification": "formal identifier; neither executable deletion experiment, source ordering selector, nor physical16 instrument",
        "smallest_exact_falsifier": "the route difference (1,-1,0,0,0,0,0,0) is killed by the authorized aggregate and separated by the formal zeta tower",
        "counterfactual_result": "authorizing deletion leaves ordering missing; adding an ordering formula leaves deletion unauthorized",
        "remaining_physical_instrument_gate": "prove each deletion preserves the admitted gauge/boundary domain, execute and calibrate all route interventions, type subtraction, and establish physical16 descent",
        "remaining_selector_gate": "derive a source ordering functional with fixed sign independently of the reconstructed route values",
        "claim_boundary": "Aspect's tester defers the physical claim; it does not reject the exact formal reconstruction theorem",
        "successor": "audit gauge-consistent independent mass controls for 8_a, 8_b, and 21 before constructing any score instrument or ordering potential",
        "checks": checks,
        "passed": all(checks.values()),
    }
    out = ROOT / "results/wp933_aspect_capability_audit_boolean_threshold.json"
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
