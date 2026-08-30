from copy import deepcopy
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "checkers" / "analyze_environment_port_tomography_run.py"
RESULT = ROOT / "results" / "environment_port_tomography_run_analyzer.json"
spec = importlib.util.spec_from_file_location("env_analyzer", MODULE)
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)


def rows(n=40):
    out = []
    for cell_index, (mode, probe, sb, eb) in enumerate(sorted(m.required_cells())):
        for i in range(n):
            s = 1 if i % 2 == 0 else -1
            if mode == "identical_marker" and sb == "X": e = s
            elif mode == "orthogonal_marker" and sb == "X": e = -s
            else: e = 1 if (i // 2) % 2 == 0 else -1
            out.append({"trial_key": f"{mode}-{probe}-{sb}-{eb}-{i}", "acquisition_epoch": "env-1",
                        "mode": mode, "input_probe": probe, "system_basis": sb, "environment_basis": eb,
                        "system_outcome": str(s), "environment_outcome": str(e),
                        "environment_port_manifest": "port-E-coherent-v1", "phase_reference_key": "comb-17",
                        "detector_assignment": "crossed-A", "acquisition_block": f"block-{i}",
                        "within_block_position": str((cell_index + i) % 40), "sealed_schedule_key": "env-schedule-1",
                        "no_click_flag": "0"})
    return out


def main():
    good = rows(); positive = m.assess(good, 20); assert positive["accepted"]
    missing = good[:-40]
    duplicate = deepcopy(good); duplicate[1]["trial_key"] = duplicate[0]["trial_key"]
    no_environment = deepcopy(good)
    for row in no_environment: row["environment_outcome"] = row["system_outcome"]
    population_cheat = deepcopy(good)
    for row in population_cheat:
        if row["mode"] == "orthogonal_marker" and row["system_basis"] == "Z": row["system_outcome"] = "1"
    grouped = deepcopy(good)
    for row in grouped: row["acquisition_block"] = row["mode"]
    hostiles = {"missing_cell_rejected": not m.assess(missing, 40)["accepted"],
                "duplicate_key_rejected": not m.assess(duplicate, 40)["accepted"],
                "environment_blind_instrument_rejected": not m.assess(no_environment, 40)["accepted"],
                "population_mismatch_rejected": not m.assess(population_cheat, 40)["accepted"],
                "grouped_acquisition_rejected": not m.assess(grouped, 40)["accepted"]}
    assert all(hostiles.values())
    out = {"schema": "marici.aspect.environment-port-tomography-run-analyzer-check.v1", "status": "pass",
           "positive_fixture": positive, "deliberate_failures": hostiles,
           "contract_attempted_trials": 40000000}
    RESULT.parent.mkdir(parents=True, exist_ok=True); RESULT.write_text(json.dumps(out, indent=2)+"\n")
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__": main()
