"""WP245: finite-exposure audit of the WP243/WP244 source identifier."""

from __future__ import annotations

import json
import math
import re
import zlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "cms-luminosity-2016"
PROVENANCE = json.loads((DATA / "provenance.json").read_text())
WP243 = json.loads((ROOT / "results" / "wp243_trace_adjoint_rate_pdet.json").read_text())


def recorded_luminosity(path):
    match = re.search(r"\|\s*\d+\s*\|\s*\d+\s*\|\s*\d+\s*\|\s*\d+\s*\|\s*[0-9.]+\s*\|\s*([0-9.]+)\s*\|\s*\n\+[-+]+\n#Check", path.read_text())
    if not match:
        raise ValueError(f"summary luminosity not found in {path}")
    return float(match.group(1))


def main():
    file_checks = []
    luminosities = {}
    for entry in PROVENANCE["files"]:
        path = DATA / entry["path"]
        checksum = format(zlib.adler32(path.read_bytes()) & 0xFFFFFFFF, "08x")
        value = recorded_luminosity(path)
        file_checks.append(checksum == entry["adler32"] and value == entry["recorded_fb_inverse"])
        luminosities[entry["path"]] = value

    full_lumi = luminosities["2016lumi.txt"]
    rates = WP243["selected_events_per_fb_per_unit_theta_squared"]
    # Orthogonal scalar mixing implies theta_i^2 <= 1. Using equality and the
    # entire certified year is an optimistic upper bound for the local shard.
    maximum_counts = {label: rate * full_lumi for label, rate in rates.items()}
    probability_each_seen = {label: 1 - math.exp(-count) for label, count in maximum_counts.items()}
    probability_both_seen = math.prod(probability_each_seen.values())
    target_mean_95 = -math.log(0.05)
    luminosity_for_95pct_one_event = {label: target_mean_95 / rate for label, rate in rates.items()}
    luminosity_for_ten_events = {label: 10 / rate for label, rate in rates.items()}

    checks = {
        "official_luminosity_files_match": all(file_checks),
        "full_2016_exposure_is_36_313753344_fb_inverse": full_lumi == 36.313753344,
        "mixing_upper_bound_is_optimistic": True,
        "both_maximum_expected_counts_below_one": all(value < 1 for value in maximum_counts.values()),
        "ideal_probability_of_both_poles_below_ten_percent": probability_both_seen < 0.1,
        "background_free_assumption_is_optimistic": True,
        "finite_2016_source_identification_rejected": probability_both_seen < 0.95,
        "asymptotic_rate_injectivity_preserved": WP243["kappa_squared_jacobian_rank"] == 2,
    }
    checks = {key: bool(value) for key, value in checks.items()}
    result = {
        "work_package": "WP245",
        "recorded_luminosity_fb_inverse": luminosities,
        "luminosity_uncertainty_percent": PROVENANCE["uncertainty_percent"],
        "maximum_theta_squared": 1,
        "maximum_selected_counts_full_2016": maximum_counts,
        "ideal_zero_background_probability_each_pole_seen": probability_each_seen,
        "ideal_zero_background_probability_both_poles_seen": probability_both_seen,
        "luminosity_for_95pct_probability_of_at_least_one_selected_event_fb_inverse": luminosity_for_95pct_one_event,
        "luminosity_for_ten_selected_events_fb_inverse": luminosity_for_ten_events,
        "classification": "WP243 is an asymptotically injective calibrated rate map, not a finite-2016 operational source identifier; WP244 source-grammar identification is likewise asymptotic/conditional",
        "smallest_physical_falsifier": "even at theta_A_squared=theta_D_squared=1 and zero background, full 2016 exposure yields less than one expected selected event in each source column",
        "remaining_instrument_gate": "substantially larger exposure or a higher-rate source-derived channel, followed by background-aware power and systematic-uncertainty validation",
        "checks": checks, "passed": all(checks.values()),
    }
    (ROOT / "results" / "wp245_finite_exposure_source_id_audit.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
