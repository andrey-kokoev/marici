"""WP318: test whether higher integer flux predicts or merely indexes the ensemble."""

import json
import sys
from pathlib import Path

import numpy as np
import sympy as sp

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


def high_branch(charge):
    return sp.sqrt(charge**2 + 1) + charge


def main():
    source = json.loads((ROOT / "results/wp20_valley_audit.json").read_text(encoding="utf-8"))
    ratios = [hierarchy_ratio(*rebuild(record)) for record in source["records"]]
    low, high = min(ratios), max(ratios)
    charges = list(range(1, 101))
    lattice = {charge: float(high_branch(charge)) for charge in charges}
    charges_in_range = [charge for charge, value in lattice.items() if low <= value <= high]

    audits = []
    for index, ratio in enumerate(ratios):
        charge = min(charges, key=lambda candidate: abs(np.log(ratio) - np.log(lattice[candidate])))
        audits.append({
            "record_index": index,
            "hierarchy_ratio": ratio,
            "nearest_charge": charge,
            "nearest_lattice_ratio": lattice[charge],
            "log_distance": float(abs(np.log(ratio) - np.log(lattice[charge]))),
        })
    closest = min(audits, key=lambda audit: audit["log_distance"])
    tolerance = 1e-8
    exact_symbolic = {
        "charge_63": str(high_branch(63)),
        "charge_64": str(high_branch(64)),
        "charge_65": str(high_branch(65)),
    }
    checks = {
        "complete_canonical_ensemble_loaded": len(ratios) == source["n_minima_audited"] == 1210,
        "high_branch_is_strictly_increasing_on_test_domain": all(lattice[n] < lattice[n + 1] for n in charges[:-1]),
        "only_charge_64_lies_in_ensemble_range": charges_in_range == [64],
        "charge_63_is_below_ensemble": lattice[63] < low,
        "charge_65_is_above_ensemble": lattice[65] > high,
        "zero_sheets_equal_the_charge_64_value_at_tolerance": sum(a["log_distance"] <= tolerance for a in audits) == 0,
        "nearest_charge_is_inferred_from_readout": closest["nearest_charge"] == 64,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP318",
        "admitted_state_domain": "integer charge magnitudes 1 through 100 and the complete canonical 1210-sheet fitted hierarchy-ratio ensemble",
        "faithful_quotient_coordinate": "weak-basis-invariant ordered hierarchy ratio, with reciprocal orientation treated separately",
        "source_authorized_probe_family": "the quantized WP314 ratio lattice t_m=sqrt(m^2+1)+m; no source energy selecting m=64 is admitted",
        "ensemble_ratio_range": [low, high],
        "charges_with_prediction_in_range": charges_in_range,
        "symbolic_neighboring_predictions": exact_symbolic,
        "numeric_neighboring_predictions": {str(n): lattice[n] for n in (63, 64, 65)},
        "closest_packet": closest,
        "contextual_partition": "each charge magnitude labels one reciprocal exchange orbit; the fitted range intersects only the magnitude-64 orbit",
        "classification": "higher flux supplies a discrete lookup family, not a selector; choosing magnitude 64 from the fitted readout is target-coded",
        "smallest_exact_falsifier": "the source rule E=n^2 on the nonzero domain selects magnitude 1, not magnitude 64",
        "remaining_physical_instrument_gate": "an independently derived source topology or action must select magnitude 64 before flavor data are read; detector precision cannot create that upstream authority",
        "tolerance_in_log_ratio": tolerance,
        "numerical_scope": "IEEE double-precision reconstruction of the canonical ensemble; symbolic lattice values are retained separately",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp318_high_flux_discrete_lookup.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
