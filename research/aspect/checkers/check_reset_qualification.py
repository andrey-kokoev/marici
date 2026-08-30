from copy import deepcopy
from fractions import Fraction as F
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "contracts" / "reset-qualification.v1.json"
RESULT = ROOT / "results" / "reset_qualification.json"

TREATMENTS = ("L1", "R2", "L2", "R1")


def spread(values):
    return max(values) - min(values)


def fixture():
    target_signal = {"L1": F(3, 5), "R2": F(1, 5), "L2": F(-1, 5), "R1": F(-3, 5)}
    cells = {}
    no_reset = {}
    for p_index, predecessor in enumerate(TREATMENTS):
        for target in TREATMENTS:
            cells[predecessor, target] = {
                "target_response": target_signal[target],
                "reset_monitor": F(0),
                "reset_failure_recorded": True,
            }
            no_reset[predecessor, target] = target_signal[target] + F(p_index, 10)
    return {
        "cells": cells,
        "no_reset": no_reset,
        "qualification_epoch": "reset-q-17",
        "science_epoch": "science-23",
        "full_records": True,
    }


def assess(data):
    expected = {(p, t) for p in TREATMENTS for t in TREATMENTS}
    complete = set(data["cells"]) == expected
    response_invariant = complete and all(
        spread([data["cells"][p, t]["target_response"] for p in TREATMENTS]) <= F(1, 20)
        for t in TREATMENTS
    )
    monitor_invariant = complete and all(
        spread([data["cells"][p, t]["reset_monitor"] for p in TREATMENTS]) <= F(1, 20)
        for t in TREATMENTS
    )
    negative_control = set(data["no_reset"]) == expected and all(
        spread([data["no_reset"][p, t] for p in TREATMENTS]) >= F(1, 10)
        for t in TREATMENTS
    )
    epoch_disjoint = data["qualification_epoch"] != data["science_epoch"]
    full_records = data["full_records"] and all(
        cell["reset_failure_recorded"] for cell in data["cells"].values()
    )
    gates = {
        "all_sixteen_predecessor_target_cells_present": complete,
        "reset_target_response_is_predecessor_invariant": response_invariant,
        "reset_monitor_is_predecessor_invariant": monitor_invariant,
        "no_reset_control_detects_injected_memory": negative_control,
        "qualification_epoch_is_disjoint_from_science_epoch": epoch_disjoint,
        "all_reset_failures_remain_in_full_outcome_record": full_records,
    }
    return gates, all(gates.values())


def main():
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    good = fixture()
    gates, accepted = assess(good)
    assert accepted

    quiet_but_not_erasing = deepcopy(good)
    quiet_but_not_erasing["cells"]["R1", "L1"]["target_response"] += F(1, 5)
    missing_cell = deepcopy(good)
    del missing_cell["cells"]["L2", "R1"]
    blind_control = deepcopy(good)
    blind_control["no_reset"] = {(p, t): F(0) for p in TREATMENTS for t in TREATMENTS}
    reused_epoch = deepcopy(good)
    reused_epoch["science_epoch"] = reused_epoch["qualification_epoch"]
    discarded_failure = deepcopy(good)
    discarded_failure["cells"]["L1", "L1"]["reset_failure_recorded"] = False

    hostiles = {
        "quiet_monitor_but_residual_target_memory_rejected": not assess(quiet_but_not_erasing)[1],
        "missing_predecessor_target_cell_rejected": not assess(missing_cell)[1],
        "memory_blind_negative_control_rejected": not assess(blind_control)[1],
        "qualification_on_science_epoch_rejected": not assess(reused_epoch)[1],
        "discarded_reset_failure_rejected": not assess(discarded_failure)[1],
    }
    assert all(hostiles.values())
    out = {
        "schema": "marici.aspect.reset-qualification-check.v1",
        "status": "pass",
        "positive_fixture_accepted": accepted,
        "positive_gates": gates,
        "deliberate_failures": hostiles,
        "cell_count": len(good["cells"]),
        "trials_per_cell": contract["minimum_effective_trials_per_predecessor_target_cell"],
        "decision": "candidate reset is qualified only for the tested settings and memory sensitivity witnessed by the no-reset control",
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
