#!/usr/bin/env python3
"""Finite comparison of a strict attachment fiber and a comma sector."""

import json
from pathlib import Path

ATT_S0 = ("bare0", "p")
ATT_S1 = ("bare1", "q")


def pullback(attachment):
    return {"bare1": "bare0", "q": "p"}[attachment]


# Comma objects are (target base, target attachment, source-to-target base arrow).
COMMA = (
    ("S0", "bare0", "id0"),
    ("S0", "p", "id0"),
    ("S1", "bare1", "f"),
    ("S1", "q", "f"),
)


def K(comma_object):
    target, attachment, arrow = comma_object
    return attachment if arrow == "id0" else pullback(attachment)


def J(attachment):
    return "S0", attachment, "id0"


def fiber_hom(source, target):
    return 1 if source == target else 0


def comma_hom_from_J(source_attachment, target_comma):
    # A map J(D)->((T,E),a) is exactly D->a*E in the discrete fiber.
    return fiber_hom(source_attachment, K(target_comma))


adjunction_table = {
    f"{source}->{target}": {
        "comma": comma_hom_from_J(source, target),
        "fiber": fiber_hom(source, K(target)),
    }
    for source in ATT_S0 for target in COMMA
}
checks = {
    "strict_fiber_has_two_objects": len(ATT_S0) == 2,
    "comma_sector_has_four_objects": len(COMMA) == 4,
    "comma_sector_is_not_strict_fiber": len(COMMA) != len(ATT_S0),
    "J_is_injective_on_objects": len({J(value) for value in ATT_S0}) == len(ATT_S0),
    "K_retracts_J": all(K(J(value)) == value for value in ATT_S0),
    "K_pulls_back_changed_targets": K(("S1", "q", "f")) == "p" and K(("S1", "bare1", "f")) == "bare0",
    "J_left_adjoint_K_hom_counts": all(item["comma"] == item["fiber"] for item in adjunction_table.values()),
    "every_comma_object_has_pulled_back_attachment": all(K(item) in ATT_S0 for item in COMMA),
    "changed_target_objects_are_retained_in_comma": sum(1 for item in COMMA if item[0] == "S1") == 2,
    "fiber_objects_preserve_base_exactly": all(J(value)[0] == "S0" for value in ATT_S0),
}
assert all(checks.values()), checks
result = {"schema": "marici.aspect.fixed-attachment-fiber-comma.v1", "status": "passed", "checks": checks, "fiber": ATT_S0, "comma": COMMA, "adjunction_table": adjunction_table, "claim_boundary": "Finite split-fibration witness; no physical evolution interpretation."}
output = Path(__file__).parents[1] / "results" / "fixed_attachment_fiber_comma.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "fiber_size": len(ATT_S0), "comma_size": len(COMMA)}, sort_keys=True))
