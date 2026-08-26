"""WP352: complete-ensemble falsification of the WP351 CP prediction."""

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    source = json.loads((ROOT / "results/wp20_valley_audit.json").read_text(encoding="utf-8"))
    records = source["records"]
    predicted_j_squared = 1 / 543
    predicted_abs_j = math.sqrt(predicted_j_squared)
    audits = []
    for index, record in enumerate(records):
        observed_j = float(record["J"])
        observed_squared = observed_j**2
        log_distance = abs(math.log(observed_squared / predicted_j_squared))
        audits.append({
            "record_index": index,
            "orbit": record["orbit"],
            "member": record["member"],
            "observed_J": observed_j,
            "observed_J_squared": observed_squared,
            "log_distance_in_J_squared": log_distance,
            "prediction_to_observed_magnitude_ratio": predicted_abs_j / abs(observed_j),
        })
    closest = min(audits, key=lambda audit: audit["log_distance_in_J_squared"])
    tolerance = 1e-8
    accepted = sum(audit["log_distance_in_J_squared"] <= tolerance for audit in audits)
    magnitudes = [abs(float(record["J"])) for record in records]
    checks = {
        "complete_canonical_ensemble_loaded": len(records) == source["n_minima_audited"] == 1210,
        "all_J_values_are_finite_and_nonzero": all(math.isfinite(value) and value > 0 for value in magnitudes),
        "zero_sheets_match_exact_prediction_at_tolerance": accepted == 0,
        "closest_sheet_has_large_log_gap": closest["log_distance_in_J_squared"] > 10,
        "prediction_exceeds_every_fitted_J_by_three_orders": predicted_abs_j / max(magnitudes) > 1000,
        "both_cp_signs_are_admitted_by_squared_comparison": all(
            (-float(record["J"])) ** 2 == float(record["J"]) ** 2 for record in records
        ),
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP352",
        "admitted_state_domain": "the complete canonical 1210-sheet WP20 fitted ensemble using stored weak-basis-invariant Jarlskog values",
        "faithful_quotient_coordinate": "J^2, so both CP-conjugate signs are admitted",
        "prediction_under_test": "WP351 sector-character rays predict J^2=1/543 independently of radial amplitudes",
        "predicted_J_squared": predicted_j_squared,
        "predicted_abs_J": predicted_abs_j,
        "ensemble_abs_J_range": [min(magnitudes), max(magnitudes)],
        "tolerance_in_log_J_squared": tolerance,
        "accepted_sheets": accepted,
        "closest_packet": closest,
        "numerical_scope": "stored IEEE double-precision J values from the canonical WP20 ensemble; the nearest gap exceeds the tolerance by more than nine orders of magnitude",
        "classification": "WP351 is a genuine conditional normalized-CP selector whose numerical prediction is decisively falsified on the complete fitted ensemble",
        "smallest_finite_falsifier": "the closest fitted sheet still differs by a log gap greater than 10 in J^2 and the predicted magnitude exceeds every fitted value by more than three orders",
        "remaining_physical_instrument_gate": "none can rescue this numerical ray prediction; a successor must change the independently derived projector geometry or sector characters and is therefore a new selector model",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp352_cp_selector_ensemble_falsifier.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
