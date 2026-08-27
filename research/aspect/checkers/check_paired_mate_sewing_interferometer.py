from fractions import Fraction as F
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "contracts" / "paired-mate-sewing-interferometer.v1.json"
RESULT = ROOT / "results" / "paired_mate_sewing_interferometer.json"


def law(gamma, cosine):
    x = gamma * cosine
    return {"00": (1 + x) / 4, "11": (1 + x) / 4,
            "01": (1 - x) / 4, "10": (1 - x) / 4}


def assess(fixture, contract):
    cells = fixture["cells"]
    full = all(set(cell["joint"]) == {"00", "01", "10", "11"} for cell in cells)
    normalized = all(sum(cell["joint"].values(), F(0)) == 1 for cell in cells)
    marginals = all(
        cell["joint"]["00"] + cell["joint"]["01"] == F(1, 2)
        and cell["joint"]["00"] + cell["joint"]["10"] == F(1, 2)
        for cell in cells
    )
    exact = all(cell["joint"] == law(cell["gamma"], cell["cosine"]) for cell in cells)
    even_odd = all(
        cell["joint"]["00"] + cell["joint"]["11"] == (1 + cell["gamma"] * cell["cosine"]) / 2
        and cell["joint"]["01"] + cell["joint"]["10"] == (1 - cell["gamma"] * cell["cosine"]) / 2
        for cell in cells
    )
    zero_flat = all(
        cell["gamma"] != 0 or all(p == F(1, 4) for p in cell["joint"].values())
        for cell in cells
    )
    records = set(contract["required_records"]) <= set(fixture["records"])
    epochs = len(set(fixture["epochs"])) == 1
    order = fixture["local_mates_close_before_sewing"]
    nonfactor = fixture["joint_analyzer"] == "coherent_even_odd_sewing"
    counts = fixture["minimum_trials"] >= contract["minimum_effective_trials_per_primary_proportion"]
    gates = {
        "complete_pair_record": full and records,
        "same_epoch_three_surface_calibration": epochs,
        "both_local_marginals_flat": marginals,
        "joint_law_normalized": normalized,
        "even_and_odd_character_blocks_observable": even_odd and exact,
        "parity_fibers_totalize": normalized and even_odd,
        "zero_coherence_is_globally_flat": zero_flat,
        "local_mates_close_before_sewing": order,
        "joint_analyzer_is_nonfactorizing": nonfactor,
        "minimum_counts_and_error_budget": counts,
    }
    return gates, all(gates.values())


def fixture(contract):
    cells = []
    for g in (F(1), F(3, 5), F(0)):
        for c in (F(1), F(0), F(-1), F(0)):
            cells.append({"gamma": g, "cosine": c, "joint": law(g, c)})
    return {
        "cells": cells, "records": contract["required_records"],
        "epochs": ["epoch-17"] * 3, "local_mates_close_before_sewing": True,
        "joint_analyzer": "coherent_even_odd_sewing", "minimum_trials": 750000,
    }


def main():
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    good = fixture(contract)
    gates, accepted = assess(good, contract)

    factorized = fixture(contract)
    for cell in factorized["cells"]:
        cell["joint"] = {k: F(1, 4) for k in ("00", "01", "10", "11")}

    postselected = fixture(contract)
    postselected["records"] = [r for r in postselected["records"] if "full_outcome" not in r]

    stale = fixture(contract)
    stale["epochs"] = ["epoch-17", "epoch-18", "epoch-17"]

    local_leak = fixture(contract)
    local_leak["cells"][0]["joint"] = {"00": F(1, 2), "01": F(1, 4), "10": F(0), "11": F(1, 4)}

    classical = fixture(contract)
    classical["joint_analyzer"] = "classical_record_comparison"

    primary = 3 * 4 * 6
    n = contract["minimum_effective_trials_per_primary_proportion"]
    epsilon = F(1, 20)
    bound = F(primary, 4 * n) / (epsilon * epsilon)
    assert primary == contract["primary_proportions"]
    assert bound == F(6, 625) and bound < F(1, 100)
    assert accepted

    failures = {
        "factorized_local_mates_rejected": not assess(factorized, contract)[1],
        "coincidence_postselection_rejected": not assess(postselected, contract)[1],
        "stale_cross_surface_calibration_rejected": not assess(stale, contract)[1],
        "local_fringe_leakage_rejected": not assess(local_leak, contract)[1],
        "classical_comparison_rejected": not assess(classical, contract)[1],
    }
    assert all(failures.values())
    out = {
        "schema": "marici.aspect.paired-mate-sewing-interferometer-check.v1",
        "status": "pass", "architecture": contract["architecture"],
        "positive_fixture_accepted": accepted, "positive_gates": gates,
        "deliberate_failures": failures, "primary_proportion_count": primary,
        "minimum_effective_trials_per_primary_proportion": n,
        "familywise_error_upper_bound": f"{bound.numerator}/{bound.denominator}",
        "decisive_signature": "both local marginals flat while joint parity retains the declared phase fringe",
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
