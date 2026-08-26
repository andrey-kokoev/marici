"""WP313: complete-ensemble falsification of the WP312 equal-spectrum prediction."""

import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "checkers"))
import wp7_ensemble as wp7


def rebuild(record):
    member = record["member"]
    phase_sector, phase_row, phase_column = record["phase_edge"]
    parameters = np.array(record["log_mags"] + [record["phi_raw"]], dtype=float)
    return wp7.build_texture(member[0], member[1], phase_sector, (phase_row, phase_column), parameters)


def ordered_singular_values(matrix):
    eigenvalues = np.linalg.eigvalsh(matrix @ matrix.conj().T)
    return np.sqrt(np.maximum(eigenvalues, 0.0))


def main():
    source = json.loads((ROOT / "results/wp20_valley_audit.json").read_text(encoding="utf-8"))
    records = source["records"]
    audits = []
    for index, record in enumerate(records):
        yukawa_up, yukawa_down = rebuild(record)
        up = ordered_singular_values(yukawa_up)
        down = ordered_singular_values(yukawa_down)
        spectral_log_distance = float(np.max(np.abs(np.log(up) - np.log(down))))
        hierarchy_ratio = float((up[-1] / up[0]) / (down[-1] / down[0]))
        hierarchy_log_distance = float(abs(np.log(hierarchy_ratio)))
        audits.append(
            {
                "record_index": index,
                "orbit": record["orbit"],
                "member": record["member"],
                "up_singular_values": up.tolist(),
                "down_singular_values": down.tolist(),
                "spectral_log_distance": spectral_log_distance,
                "hierarchy_ratio": hierarchy_ratio,
                "hierarchy_log_distance": hierarchy_log_distance,
            }
        )

    closest_spectrum = min(audits, key=lambda audit: audit["spectral_log_distance"])
    closest_hierarchy = min(audits, key=lambda audit: audit["hierarchy_log_distance"])
    equality_tolerance = 1e-8
    spectrum_passes = sum(audit["spectral_log_distance"] <= equality_tolerance for audit in audits)
    hierarchy_passes = sum(audit["hierarchy_log_distance"] <= equality_tolerance for audit in audits)

    checks = {
        "canonical_wp20_count_is_1210": source["n_minima_audited"] == len(records) == 1210,
        "all_records_rebuilt": len(audits) == 1210,
        "zero_sheets_have_equal_spectra": spectrum_passes == 0,
        "zero_sheets_have_equal_hierarchy_ratios": hierarchy_passes == 0,
        "closest_spectrum_still_has_large_invariant_gap": closest_spectrum["spectral_log_distance"] > 1,
        "closest_hierarchy_still_exceeds_numerical_tolerance": closest_hierarchy["hierarchy_log_distance"] > 1e-3,
        "all_singular_values_are_positive": all(min(audit["up_singular_values"] + audit["down_singular_values"]) > 0 for audit in audits),
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP313",
        "admitted_state_domain": "complete canonical WP20 stored viable ensemble rebuilt into weak-basis-invariant ordered Yukawa singular spectra",
        "ensemble_size": len(audits),
        "prediction_under_test": "WP312 symmetric matching requires M_u=M_d and therefore identical ordered spectra and hierarchy ratio 1",
        "tolerance": equality_tolerance,
        "numerical_scope": "IEEE double-precision reconstruction using the canonical WP20 builder; closest invariant gaps exceed the equality tolerance by more than eight orders of magnitude",
        "accepted_equal_spectra": spectrum_passes,
        "accepted_equal_hierarchy_ratios": hierarchy_passes,
        "closest_spectrum_packet": closest_spectrum,
        "closest_hierarchy_packet": closest_hierarchy,
        "classification": "WP312 is a genuine source-derived ratio selector but its numerical equal-spectrum and equal-hierarchy prediction is falsified on the complete fitted physical ensemble",
        "smallest_exact_falsifier": f"exact equality requires zero ordered log-spectrum gap; record {closest_spectrum['record_index']} is closest yet has reconstructed gap {closest_spectrum['spectral_log_distance']:.12g}",
        "remaining_physical_instrument_gate": "a successor must introduce independently derived exchange breaking that yields unequal spectra while retaining a non-fitted, ensemble-stable proper physical16 prediction",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp313_symmetric_selector_ensemble_falsifier.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
