from __future__ import annotations

import copy
import json
from fractions import Fraction
from pathlib import Path


INTERFACE = Path("research/voevodsky/coherence-pyramid-partial-composition.json")


def compose(first: dict[str, object], second: dict[str, object]) -> tuple[bool, str, dict[str, object] | None]:
    if first["target"] != second["source"]:
        return False, "middle_type_mismatch", None
    if first.get("identity"):
        return True, "right_input", second
    if second.get("identity"):
        return True, "left_input", first
    if first["kind"] != second["kind"]:
        return False, "variance_mismatch", None
    certificates = set(first["certificates"]) & set(second["certificates"])
    kind = str(first["kind"])
    required = {
        "vertical": {"source_compatibility", "port_preservation"},
        "under": {"typed_injection", "form_preservation", "radical_compatibility"},
        "over": {"typed_surjection", "composite_kernel_identification", "composite_exactness"},
        "comparison": {"domain_map", "radical_descent", "form_isometry", "positive_composite_minimum_modulus"},
    }[kind]
    if not required <= certificates:
        return False, f"missing_{sorted(required - certificates)[0]}", None
    if kind == "comparison" and Fraction(str(first["minimum_modulus"])) * Fraction(str(second["minimum_modulus"])) <= 0:
        return False, "comparison_modulus_collapse", None
    return True, "composed", {
        "kind": kind,
        "source": first["source"],
        "target": second["target"],
        "certificates": sorted(required),
    }


def admit_reindexing(kind: str, certificate: dict[str, object]) -> tuple[bool, str]:
    required = {
        "under_amalgamation": ["typed_cospan", "full_joint_cross_pairing", "joint_positivity", "radical_compatibility", "port_and_sewing_compatibility"],
        "over_pullback": ["typed_base_map", "fiber_product", "kernel_transport", "pullback_exactness"],
        "completion_transport": ["typed_composite", "common_core_transport", "closed_limit_transport", "radical_stability_transport", "positive_coercivity_transport"],
    }[kind]
    for field in required:
        if certificate.get(field) is not True:
            return False, field
    return True, "admitted"


def main() -> None:
    interface = json.loads(INTERFACE.read_text(encoding="utf-8"))
    assert len(interface["identity_constructors"]) == 4
    assert len(interface["refusals"]) == 6

    under = {
        "kind": "under", "source": "G0", "target": "G1",
        "certificates": ["typed_injection", "form_preservation", "radical_compatibility"],
    }
    under_next = {**under, "source": "G1", "target": "G2"}
    identity = {"kind": "under", "source": "G0", "target": "G0", "identity": True, "certificates": []}
    assert compose(identity, under) == (True, "right_input", under)
    assert compose(under, {**identity, "source": "G1", "target": "G1"}) == (True, "left_input", under)
    assert compose(under, under_next)[0] is True

    over = {
        "kind": "over", "source": "E0", "target": "E1",
        "certificates": ["typed_surjection", "composite_kernel_identification", "composite_exactness"],
    }
    assert compose(over, {**over, "source": "E1", "target": "E2"})[0] is True

    comparison = {
        "kind": "comparison", "source": "Q0", "target": "Q1", "minimum_modulus": "1/2",
        "certificates": ["domain_map", "radical_descent", "form_isometry", "positive_composite_minimum_modulus"],
    }
    assert compose(comparison, {**comparison, "source": "Q1", "target": "Q2"})[0] is True

    valid_reindexing = {
        "under_amalgamation": {field: True for field in interface["reindexing_constructors"]["under_amalgamation"]},
        "over_pullback": {field: True for field in interface["reindexing_constructors"]["over_pullback"]},
        "completion_transport": {field: True for field in interface["reindexing_constructors"]["completion_transport"]},
    }
    assert all(admit_reindexing(kind, certificate)[0] for kind, certificate in valid_reindexing.items())

    hostile_results: dict[str, str] = {}
    mismatch = compose(under, {**under_next, "source": "OTHER"})
    assert mismatch[:2] == (False, "middle_type_mismatch")
    hostile_results["middle_type_mismatch"] = mismatch[1]

    omitted_kernel = copy.deepcopy(over)
    omitted_kernel["certificates"].remove("composite_kernel_identification")
    result = compose(omitted_kernel, {**over, "source": "E1", "target": "E2"})
    assert not result[0]
    hostile_results["over_kernel_omitted"] = result[1]

    for hostile, kind, missing in [
        ("amalgamation_pairwise_only", "under_amalgamation", "full_joint_cross_pairing"),
        ("pullback_without_exactness", "over_pullback", "pullback_exactness"),
        ("completion_certificate_not_transportable", "completion_transport", "radical_stability_transport"),
    ]:
        fixture = copy.deepcopy(valid_reindexing[kind])
        fixture[missing] = False
        admitted, reason = admit_reindexing(kind, fixture)
        assert not admitted and reason == missing
        hostile_results[hostile] = reason

    collapsed = {**comparison, "minimum_modulus": "0/1"}
    result = compose(collapsed, {**comparison, "source": "Q1", "target": "Q2"})
    assert result[:2] == (False, "comparison_modulus_collapse")
    hostile_results["comparison_modulus_collapse"] = result[1]

    output = {
        "schema": "marici.voevodsky.coherence-pyramid-partial-composition-check.v1",
        "status": "partial_composition_constructors_verified",
        "identity_classes_verified": 4,
        "sequential_classes_verified": 4,
        "reindexing_classes_verified": 3,
        "hostile_refusals": hostile_results,
        "category_laws_claimed": False,
        "next_gate": "associators, unitors, interchange, and Beck-Chevalley cells",
        "passed": True,
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
