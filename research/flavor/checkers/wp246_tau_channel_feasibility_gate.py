"""WP246: pre-acquisition feasibility gate for a higher-rate tau P_det."""

from __future__ import annotations

import json
import math
from pathlib import Path

import openpyxl


ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "data" / "lhchxswg-yr4" / "Higgs_XSBR_YR4_update.xlsx"
WP243 = json.loads((ROOT / "results" / "wp243_trace_adjoint_rate_pdet.json").read_text())
WP245 = json.loads((ROOT / "results" / "wp245_finite_exposure_source_id_audit.json").read_text())
CATALOG = json.loads((ROOT / "data" / "cms-tau-channel-catalog" / "provenance.json").read_text())


def table(sheet, columns):
    return [(float(row[0]), [row[column - 1] for column in columns])
            for row in sheet.iter_rows(min_row=6, values_only=True)
            if isinstance(row[0], (int, float))]


def interpolate(rows, target):
    lo = max(row for row in rows if row[0] <= target)
    hi = min(row for row in rows if row[0] >= target)
    weight = 0 if lo[0] == hi[0] else (target - lo[0]) / (hi[0] - lo[0])
    return [a + weight * (b - a) for a, b in zip(lo[1], hi[1])]


def main():
    workbook = openpyxl.load_workbook(BOOK, read_only=True, data_only=True)
    # tau, mu and all listed partial widths used by WP243.
    widths = table(workbook["YR4 BSM Width"], [2, 5, 8, 11, 17, 22, 25, 28, 31, 34])
    exposure = WP245["recorded_luminosity_fb_inverse"]["2016lumi.txt"]
    target_mean = -math.log(0.05)
    outputs = {}
    for label, calibration in WP243["calibrations"].items():
        values = interpolate(widths, calibration["mass_GeV"])
        br_tau = values[1] / sum(values)
        raw_rate = 1000 * calibration["bbH_cross_section_pb"] * br_tau
        outputs[label] = {
            "mass_GeV": calibration["mass_GeV"],
            "tau_branching_fraction_listed_modes": br_tau,
            "produced_tau_pairs_per_fb_per_unit_theta_squared": raw_rate,
            "maximum_full_2016_events_before_selection": raw_rate * exposure,
            "minimum_acceptance_for_95pct_at_least_one_event": target_mean / (raw_rate * exposure),
            "minimum_acceptance_for_ten_expected_events": 10 / (raw_rate * exposure),
        }
    catalog_masses = sorted(record["mass_GeV"] for record in CATALOG["records"])
    checks = {
        "tau_channel_rate_exceeds_dimuon": all(
            outputs[label]["produced_tau_pairs_per_fb_per_unit_theta_squared"]
            > WP243["selected_events_per_fb_per_unit_theta_squared"][label]
            for label in outputs),
        "weaker_pole_one_event_acceptance_threshold_below_five_percent": outputs["D"]["minimum_acceptance_for_95pct_at_least_one_event"] < 0.05,
        "weaker_pole_ten_event_acceptance_threshold_below_ten_percent": outputs["D"]["minimum_acceptance_for_ten_expected_events"] < 0.1,
        "catalog_brackets_both_actual_poles": all(
            catalog_masses[0] <= output["mass_GeV"] <= catalog_masses[-1]
            for output in outputs.values()),
        "common_frame_tau_response_absent": True,
        "tau_mass_resolution_rank_unproved": True,
        "finite_source_identification_not_yet_claimed": True,
    }
    checks = {key: bool(value) for key, value in checks.items()}
    result = {
        "work_package": "WP246",
        "channel": "bottom-associated CP-even scalar to tau pairs",
        "full_2016_recorded_luminosity_fb_inverse": exposure,
        "feasibility": outputs,
        "available_catalog_mass_points_GeV": catalog_masses,
        "classification": "rate-feasible bracketed-response candidate, not an admitted finite source identifier",
        "acceptance_gate": "independently calibrated D-pole tau acceptance must exceed 2.5% for a 95% chance of one event and about 8.3% for ten expected events",
        "resolution_gate": "validate interpolation closure on the 130/140/160 GeV grid, then show actual-pole reconstructed tau columns retain rank two after backgrounds and systematics",
        "smallest_falsifier": "D-pole acceptance below its computed threshold or proportional reconstructed tau templates",
        "checks": checks, "passed": all(checks.values()),
    }
    (ROOT / "results" / "wp246_tau_channel_feasibility_gate.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
