from copy import deepcopy
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "checkers" / "analyze_reset_qualification_run.py"
RESULT = ROOT / "results" / "reset_qualification_run_analyzer.json"
spec = importlib.util.spec_from_file_location("reset_analyzer", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def rows(n=32):
    out = []
    cell_index = 0
    for arm in module.ARMS:
        for p_index, predecessor in enumerate(module.TREATMENTS):
            for t_index, target in enumerate(module.TREATMENTS):
                base_hits = 4 + t_index * 2
                hits = base_hits if arm == "five_empty_bin_reset" else base_hits + p_index * 2
                for i in range(n):
                    out.append({
                        "trial_key": f"{arm}-{predecessor}-{target}-{i}",
                        "qualification_epoch": "reset-q-17", "arm": arm,
                        "predecessor": predecessor, "target": target,
                        "reset_setting": "empty,empty,empty,empty,empty" if arm == "five_empty_bin_reset" else "none",
                        "reset_monitor_outcome": "0", "target_outcome": str(int(i < hits)),
                        "reset_failure": str(int(i == 0 and predecessor == "L1" and target == "L1")),
                        "detector_assignment": "crossed-A", "source_setting": "probe-1",
                        "acquisition_block": f"block-{i}",
                        "within_block_position": str((cell_index + i) % 32),
                        "sealed_schedule_key": "schedule-17",
                    })
                cell_index += 1
    return out


def main():
    good = rows()
    accepted = module.assess(good, 20)
    assert accepted["accepted"]
    missing = good[:-20]
    duplicate = deepcopy(good); duplicate[1]["trial_key"] = duplicate[0]["trial_key"]
    wrong_reset = deepcopy(good); wrong_reset[0]["reset_setting"] = "empty,empty,empty,empty"
    grouped_drift = deepcopy(good)
    for row in grouped_drift:
        row["acquisition_block"] = f"{row['arm']}-{row['predecessor']}"
    fixed_position = deepcopy(good)
    for row in fixed_position:
        arm_index = module.ARMS.index(row["arm"])
        p_index = module.TREATMENTS.index(row["predecessor"])
        t_index = module.TREATMENTS.index(row["target"])
        row["within_block_position"] = str(arm_index * 16 + p_index * 4 + t_index)
    memory_survives = deepcopy(good)
    for row in memory_survives:
        if row["arm"] == "five_empty_bin_reset" and row["predecessor"] == "R1" and row["target"] == "L1":
            row["target_outcome"] = "1" if int(row["trial_key"].rsplit("-", 1)[1]) < 8 else "0"
    blind_control = deepcopy(good)
    for row in blind_control:
        if row["arm"] == "no_reset_control":
            i = int(row["trial_key"].rsplit("-", 1)[1]); t = module.TREATMENTS.index(row["target"])
            row["target_outcome"] = str(int(i < 4 + t * 2))
    hostiles = {
        "missing_cell_rejected": not module.assess(missing, 32)["accepted"],
        "duplicate_trial_key_rejected": not module.assess(duplicate, 32)["accepted"],
        "four_bin_substitution_rejected": not module.assess(wrong_reset, 32)["accepted"],
        "grouped_drift_confounder_rejected": not module.assess(grouped_drift, 32)["accepted"],
        "fixed_within_block_position_confounder_rejected": not module.assess(fixed_position, 32)["accepted"],
        "surviving_target_memory_rejected": not module.assess(memory_survives, 32)["accepted"],
        "memory_blind_control_rejected": not module.assess(blind_control, 32)["accepted"],
    }
    assert all(hostiles.values())
    out = {"schema": "marici.aspect.reset-qualification-run-analyzer-check.v1", "status": "pass",
           "positive_fixture": accepted, "deliberate_failures": hostiles}
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
