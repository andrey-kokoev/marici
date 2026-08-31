#!/usr/bin/env python3
"""Execute SCC Instrument Profile assignments against scoped registry evidence."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CONTRACT = ROOT / "research/aspect/contracts/instrument-registry.v1.json"
RESULT = ROOT / "research/aspect/results/instrument_profiles.json"
c = json.loads(CONTRACT.read_text(encoding="utf-8"))
instruments = [i for i in c["instruments"] if i["profile_status"] in {"proposed", "checked"}]


def residuals(instrument):
    return {reason for reasons in instrument.get("factor_residuals", {}).values() for reason in reasons}


def execute(instrument):
    profile = instrument["scc_instrument_profile"]
    factors = instrument["factor_status"]
    result_path = ROOT / instrument["verification"]["result"]
    result = json.loads(result_path.read_text(encoding="utf-8"))
    result_pass = result.get("status") == "pass" or result.get("passed") is True
    rs = residuals(instrument)

    scale_pass = profile["scale"] in c["profile_dimensions"]["scale"] and bool(instrument["assessment_regime"]["scale"])
    carrier_pass = {
        "absent": True,
        "split": factors["geometry_support"] != "open",
        "compatible": factors["geometry_support"] != "open" and factors["transport_composition"] != "open",
    }[profile["carrier"]]
    action_pass = {
        "absent": True,
        "typed": factors["constructor_grammar"] != "open",
        "faithful": factors["constructor_grammar"] == "constructed" and "constructor_authority_open" not in rs,
    }[profile["action"]]
    observation_pass = {
        "absent": True,
        "natural": factors["readout"] != "open",
        "faithful": (
            factors["probe_grammar"] == "constructed"
            and factors["readout"] == "constructed"
            and "access_nonfaithful" not in rs
            and "readout_hidden_state" not in rs
        ),
    }[profile["observation"]]
    estimate_pass = {
        "absent": True,
        "bounded": result_pass and factors["readout"] != "open",
        "uniform": result_pass and instrument["model_status"] == "exact_finite_model",
    }[profile["estimate"]]
    dimensions = {
        "scale": scale_pass,
        "carrier": carrier_pass,
        "action": action_pass,
        "observation": observation_pass,
        "estimate": estimate_pass,
    }
    return {
        "id": instrument["id"],
        "profile": profile,
        "verification_result": instrument["verification"]["result"],
        "verification_result_passes": result_pass,
        "dimension_checks": dimensions,
        "passed": result_pass and all(dimensions.values()),
    }


executions = [execute(instrument) for instrument in instruments]
out = {
    "schema": "marici.aspect.instrument-profile-execution.v1",
    "contract": str(CONTRACT.relative_to(ROOT)).replace("\\", "/"),
    "executed_profile_count": len(executions),
    "passed_profile_count": sum(item["passed"] for item in executions),
    "failed_profile_ids": [item["id"] for item in executions if not item["passed"]],
    "executions": executions,
    "passed": bool(executions) and all(item["passed"] for item in executions),
    "claim_boundary": "checks scoped classifier predicates against recorded finite model evidence; it does not establish physical execution or source-type equivalence"
}
RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
print(json.dumps(out, indent=2))
raise SystemExit(0 if out["passed"] else 1)
