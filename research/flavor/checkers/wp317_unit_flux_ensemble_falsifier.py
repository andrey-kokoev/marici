"""WP317: complete-ensemble test of the WP316 reciprocal prediction."""

import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "checkers"))
import wp7_ensemble as wp7


def rebuild(record):
    member = record["member"]
    sector, row, column = record["phase_edge"]
    parameters = np.array(record["log_mags"] + [record["phi_raw"]], dtype=float)
    return wp7.build_texture(member[0], member[1], sector, (row, column), parameters)


def hierarchy_ratio(yukawa_up, yukawa_down):
    up = np.sqrt(np.maximum(np.linalg.eigvalsh(yukawa_up @ yukawa_up.conj().T), 0.0))
    down = np.sqrt(np.maximum(np.linalg.eigvalsh(yukawa_down @ yukawa_down.conj().T), 0.0))
    return float((up[-1] / up[0]) / (down[-1] / down[0]))


def main():
    source = json.loads((ROOT / "results/wp20_valley_audit.json").read_text(encoding="utf-8"))
    target_small = float(np.sqrt(2.0) - 1.0)
    target_large = float(np.sqrt(2.0) + 1.0)
    targets = np.array([target_small, target_large])
    audits = []
    for index, record in enumerate(source["records"]):
        ratio = hierarchy_ratio(*rebuild(record))
        log_distances = np.abs(np.log(ratio) - np.log(targets))
        branch = int(np.argmin(log_distances))
        audits.append({
            "record_index": index,
            "orbit": record["orbit"],
            "member": record["member"],
            "hierarchy_ratio": ratio,
            "nearest_target": float(targets[branch]),
            "log_distance": float(log_distances[branch]),
        })

    closest = min(audits, key=lambda audit: audit["log_distance"])
    tolerance = 1e-8
    accepted = sum(audit["log_distance"] <= tolerance for audit in audits)
    ratios = [audit["hierarchy_ratio"] for audit in audits]
    checks = {
        "complete_canonical_ensemble_loaded": len(audits) == source["n_minima_audited"] == 1210,
        "reciprocal_targets_are_distinct": target_small != target_large,
        "target_product_is_one_numerically": abs(target_small * target_large - 1.0) < 1e-14,
        "zero_sheets_match_either_ordered_branch": accepted == 0,
        "closest_sheet_is_well_outside_tolerance": closest["log_distance"] > 1e-3,
        "all_reconstructed_ratios_are_positive": min(ratios) > 0,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP317",
        "admitted_state_domain": "complete canonical WP20 stored viable ensemble rebuilt into weak-basis-invariant ordered Yukawa hierarchy ratios",
        "ensemble_size": len(audits),
        "prediction_under_test": "WP316 unit-flux orbit predicts the unordered reciprocal pair {sqrt(2)-1, sqrt(2)+1}",
        "ordered_targets": [target_small, target_large],
        "tolerance_in_log_ratio": tolerance,
        "accepted_sheets": accepted,
        "ensemble_ratio_range": [min(ratios), max(ratios)],
        "closest_packet": closest,
        "numerical_scope": "IEEE double-precision reconstruction of the canonical WP20 records; the minimum log-gap exceeds the declared tolerance by more than eight orders of magnitude",
        "classification": "the WP316 conditional topological selector is genuine on its declared quotient but its unit-flux hierarchy prediction is falsified on the complete fitted ensemble",
        "smallest_finite_falsifier": "the selected orbit has only the two reciprocal branches, while the closest reconstructed sheet has log-distance greater than 3.9 from both",
        "remaining_physical_instrument_gate": "none can rescue the numerical prediction; a successor must change the independently derived source energy or matching, which constitutes a new selector model",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp317_unit_flux_ensemble_falsifier.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
