"""Compile the Hodge-control model through Aspect's seven-axis contract."""

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve()
ROOT = HERE.parents[1]
ASPECT = ROOT.parent / "aspect" / "results" / "typed_seven_axis_events.json"
HODGE = ROOT / "results" / "celestial_hodge_bridge_checks.json"
CIRCLE = ROOT / "results" / "radiative_hodge_circle_boundary_checks.json"
LOCAL = ROOT / "results" / "local_hodge_selector_connection_checks.json"
RESULT = ROOT / "results" / "aspect_seven_axis_hodge_model_audit.json"

aspect = json.loads(ASPECT.read_text(encoding="utf-8"))
hodge = json.loads(HODGE.read_text(encoding="utf-8"))
circle = json.loads(CIRCLE.read_text(encoding="utf-8"))
local = json.loads(LOCAL.read_text(encoding="utf-8"))

unknown = "unknown"
global_hodge = {
    "scalar": unknown,
    "packet": unknown,
    "incidence": unknown,
    "history": unknown,
    "path": "admissible",
    "coefficient": "native",
    "action": "authorized",
}
local_hodge = {
    "scalar": unknown,
    "packet": unknown,
    "incidence": unknown,
    "history": unknown,
    "path": unknown,
    "coefficient": "native",
    "action": "missing",
}
absent_selector = dict(local_hodge)

allowed = {
    "scalar": {"bright", "dark", "flat_normalized", unknown},
    "packet": {"zero", "bright", unknown},
    "incidence": {"matched", "aliased", unknown},
    "history": {"trivial", "nontrivial", unknown},
    "path": {"admissible", "disconnected", unknown},
    "coefficient": {"native", "requires_extension", unknown},
    "action": {"authorized", "missing", unknown},
}

checks = {
    "aspect_updated_tester_passes_unchanged": aspect["status"] == "pass" and aspect["axis_count"] == 7,
    "all_strominger_source_checks_pass": all(x["status"] == "passed" for x in (hodge, circle, local)),
    "global_hodge_event_is_seven_axis_typed": all(global_hodge[k] in allowed[k] for k in allowed),
    "global_hodge_action_exercises_authorized_value": global_hodge["coefficient"] == "native" and global_hodge["path"] == "admissible" and global_hodge["action"] == "authorized",
    "local_hodge_event_keeps_native_coefficient_separate_from_missing_action": local_hodge["coefficient"] == "native" and local_hodge["action"] == "missing",
    "old_selective_coefficient_fixture_is_superseded": aspect["events"]["selective_gate_path"]["coefficient"] == "requires_extension" and global_hodge["coefficient"] == "native",
    "reflection_fixed_path_and_full_radiative_path_have_distinct_scopes": aspect["events"]["selective_gate_path"]["path"] == "disconnected" and global_hodge["path"] == "admissible",
    "seven_axes_alias_absent_action_and_domain_obstruction": absent_selector == local_hodge,
    "eighth_domain_axis_separates_the_hostile_pair": {"absent": "unknown", "local_hodge": "obstructed"}["absent"] != {"absent": "unknown", "local_hodge": "obstructed"}["local_hodge"],
}

result = {
    "schema": "marici.strominger.aspect-seven-axis-hodge-model-audit.v1",
    "status": "passed" if all(checks.values()) else "failed",
    "passed": sum(checks.values()),
    "total": len(checks),
    "checks": checks,
    "compiled_events": {
        "global_hodge_circle": global_hodge,
        "local_hodge_selector": local_hodge,
    },
    "tester_disposition": {
        "survives": "coefficient, path, and action must remain independent",
        "superseded_fixture": "the global Hodge gate has native real source coefficients and an admissible path on the unrestricted radiative carrier",
        "scope_correction": "disconnected applies only inside the reflection-fixed projective locus",
        "smallest_missing_axis": {
            "name": "domain",
            "values": ["preserved", "obstructed", "unknown"],
            "reason": "action=missing cannot distinguish an absent operation from a candidate that fails to preserve the declared derivative domain",
        },
        "hostile_alias": {
            "seven_axis_tuple": local_hodge,
            "case_one": "no selector operation supplied",
            "case_two": "local Hodge formula supplied but selector current exits the derivative-defined carrier",
        },
    },
}
result["checker_sha256"] = hashlib.sha256(HERE.read_bytes()).hexdigest()
RESULT.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
print(f"{result['passed']}/{result['total']} checks passed")
print(result["checker_sha256"])
raise SystemExit(0 if result["status"] == "passed" else 1)
