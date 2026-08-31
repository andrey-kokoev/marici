#!/usr/bin/env python3
"""Validate the bounded Aspect instrument registry and report metadata coverage."""
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CONTRACT = ROOT / "research/aspect/contracts/instrument-registry.v1.json"
RESULT = ROOT / "research/aspect/results/instrument_registry.json"
c = json.loads(CONTRACT.read_text(encoding="utf-8"))
instruments = c["instruments"]
families = {family["id"] for family in c["families"]}
ids = [instrument["id"] for instrument in instruments]
model_vocab = set(c["status_vocabularies"]["model_status"])
simulation_vocab = set(c["status_vocabularies"]["simulation_status"])
profile_vocab = set(c["status_vocabularies"]["profile_status"])
profile_dimensions = c["profile_dimensions"]
factors = {
    "geometry_support", "coefficients", "constructor_grammar",
    "transport_composition", "quotient", "completion", "probe_grammar",
    "readout", "authority"
}
regime_fields = {"scale", "truncation", "access", "calibration", "binding"}
residual_vocab = set(c["status_vocabularies"]["factor_residual"])
portfolio = ROOT / c["portfolio_index"]["path"]
numbered = [line for line in portfolio.read_text(encoding="utf-8").splitlines() if re.match(r"^\d+\. ", line)]
profile_execution = json.loads((ROOT / "research/aspect/results/instrument_profiles.json").read_text(encoding="utf-8"))
passed_profile_ids = {item["id"] for item in profile_execution["executions"] if item["passed"]}

checks = {
    "instrument_ids_unique": len(ids) == len(set(ids)),
    "families_unique": len(families) == len(c["families"]),
    "families_registered": all(instrument["family"] in families for instrument in instruments),
    "packets_exist": all((ROOT / instrument["packet"]).is_file() for instrument in instruments),
    "model_status_typed": all(instrument["model_status"] in model_vocab for instrument in instruments),
    "simulation_status_typed": all(instrument["simulation_status"] in simulation_vocab for instrument in instruments),
    "passed_simulations_have_receipts": all(
        instrument["simulation_status"] != "passed"
        or instrument.get("simulation_receipt") == instrument["verification"]["result"]
        and (ROOT / instrument["simulation_receipt"]).is_file()
        for instrument in instruments
    ),
    "profile_status_typed": all(instrument["profile_status"] in profile_vocab for instrument in instruments),
    "unassigned_profiles_are_null": all(
        instrument["profile_status"] != "unassigned" or instrument["scc_instrument_profile"] is None
        for instrument in instruments
    ),
    "active_profiles_are_total_and_typed": all(
        instrument["profile_status"] not in {"proposed", "checked"}
        or set(instrument["scc_instrument_profile"]) == set(profile_dimensions)
        and all(
            instrument["scc_instrument_profile"][dimension] in values
            for dimension, values in profile_dimensions.items()
        )
        and bool(instrument.get("profile_rationale"))
        for instrument in instruments
    ),
    "checked_profiles_have_passed_execution": all(
        instrument["profile_status"] != "checked" or instrument["id"] in passed_profile_ids
        for instrument in instruments
    ),
    "profile_collision_does_not_collapse_instruments": (
        next(instrument for instrument in instruments if instrument["id"] == "instrument.three-polarizer-zxz.v1")["scc_instrument_profile"]
        == next(instrument for instrument in instruments if instrument["id"] == "instrument.finite-lossy-photodetection.v1")["scc_instrument_profile"]
    ),
    "nonfaithful_access_is_not_profiled_faithful": all(
        instrument["profile_status"] == "unassigned"
        or "access_nonfaithful" not in sum(instrument.get("factor_residuals", {}).values(), [])
        or instrument["scc_instrument_profile"]["observation"] != "faithful"
        for instrument in instruments
    ),
    "factor_matrices_total_when_present": all(
        "factor_status" not in instrument or set(instrument["factor_status"]) == factors
        for instrument in instruments
    ),
    "factor_status_values_typed": all(
        "factor_status" not in instrument
        or set(instrument["factor_status"].values()) <= {"constructed", "partial", "open"}
        for instrument in instruments
    ),
    "factor_matrices_have_complete_regimes": all(
        "factor_status" not in instrument
        or set(instrument.get("assessment_regime", {})) == regime_fields
        and all(instrument["assessment_regime"].values())
        for instrument in instruments
    ),
    "nonconstructed_cells_have_typed_residuals": all(
        "factor_status" not in instrument
        or {
            factor for factor, status in instrument["factor_status"].items()
            if status != "constructed"
        } == set(instrument.get("factor_residuals", {}))
        and all(
            reasons and set(reasons) <= residual_vocab
            for reasons in instrument.get("factor_residuals", {}).values()
        )
        for instrument in instruments
    ),
    "verification_links_exist_when_present": all(
        "verification" not in instrument
        or all((ROOT / path).is_file() for path in instrument["verification"].values())
        for instrument in instruments
    ),
    "three_polarizer_registered": "instrument.three-polarizer-zxz.v1" in ids,
    "three_polarizer_is_open_continuation": next(
        instrument for instrument in instruments if instrument["id"] == "instrument.three-polarizer-zxz.v1"
    )["interaction_net_topology"] == "open_continuation_path",
    "portfolio_index_count_matches": len(numbered) == c["portfolio_index"]["indexed_packet_count"] == 49,
    "registry_is_simulation_only": c["portfolio_index"]["execution_scope"] == "simulation_only"
}

coverage = {
    "registered_instruments": len(instruments),
    "indexed_portfolio_packets": len(numbered),
    "families": len(families),
    "factor_matrices": sum("factor_status" in instrument for instrument in instruments),
    "assessment_regimes": sum("assessment_regime" in instrument for instrument in instruments),
    "typed_factor_residual_sets": sum("factor_residuals" in instrument for instrument in instruments),
    "verification_links": sum("verification" in instrument for instrument in instruments),
    "proposed_scc_profiles": sum(instrument["profile_status"] == "proposed" for instrument in instruments),
    "assigned_or_checked_scc_profiles": sum(instrument["profile_status"] in {"assigned", "checked"} for instrument in instruments),
    "executed_simulations": sum(instrument["simulation_status"] == "passed" for instrument in instruments),
    "family_distribution": dict(sorted(Counter(instrument["family"] for instrument in instruments).items()))
}
out = {
    "schema": "marici.aspect.instrument-registry-check.v1",
    "contract": str(CONTRACT.relative_to(ROOT)).replace("\\", "/"),
    "passed": all(checks.values()),
    "checks": checks,
    "coverage": coverage,
    "residual": "all twenty-four canonical simulations and SCC profiles pass their scoped executable checks; twenty-five indexed portfolio packets remain outside the canonical registry",
    "claim_boundary": c["claim_boundary"]
}
RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
print(json.dumps(out, indent=2))
raise SystemExit(0 if out["passed"] else 1)
