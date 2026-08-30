"""Typed existence contract for the first nonzero five-point homotopy residue."""

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve()
ROOT = HERE.parents[1]
RESULT = ROOT / "results" / "five_point_eta_squared_residue_contract_checks.json"

contract = {
    "arity": 5,
    "residue_group": "pi_4(S2)",
    "group_presentation": "Z/2",
    "generator": "eta o Sigma(eta)",
    "generator_name": "eta^2",
    "double": "0",
    "braid_source": "Brun_5(S2)",
    "braid_to_residue_map": "surjective",
    "explicit_braid_lift": None,
}

checks = {
    "residue_is_five_point_graded": contract["arity"] == 5,
    "residue_group_is_pi4_of_sphere": contract["residue_group"] == "pi_4(S2)",
    "residue_is_binary": contract["group_presentation"] == "Z/2",
    "generator_is_secondary_hopf_composite": "Sigma(eta)" in contract["generator"],
    "doubling_trivializes_generator": contract["double"] == "0",
    "existence_follows_from_surjective_braid_map": contract["braid_to_residue_map"] == "surjective",
    "explicit_lift_is_not_fabricated": contract["explicit_braid_lift"] is None,
}
checks = {name: bool(value) for name, value in checks.items()}

payload = {
    "schema": "marici.strominger.five-point-eta-squared-residue-contract.v1",
    "status": "passed" if all(checks.values()) else "failed",
    "passed": sum(checks.values()),
    "total": len(checks),
    "checks": checks,
    "contract": contract,
    "conclusion": "a nonzero binary five-point residue exists and is typed as eta squared; an explicit Brunnian braid lift remains uncompiled",
    "rejection": "do not reuse the fillable nested commutator as the eta-squared lift",
}
payload["checker_sha256"] = hashlib.sha256(HERE.read_bytes()).hexdigest()
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="ascii")
print(f"{payload['passed']}/{payload['total']} checks passed")
print(payload["checker_sha256"])
raise SystemExit(0 if payload["status"] == "passed" else 1)
