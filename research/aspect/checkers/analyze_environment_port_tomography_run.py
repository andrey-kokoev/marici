import argparse
import csv
from collections import Counter, defaultdict
from fractions import Fraction as F
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "contracts" / "environment-port-tomography-acquisition.v1.json"
PROBES = ("H", "V", "D", "R")
BASES = ("X", "Y", "Z")


def required_cells():
    science = {("science", p, s, e) for p in PROBES for s in BASES for e in BASES}
    controls = {(mode, "D", basis, basis) for mode in ("identical_marker", "orthogonal_marker")
                for basis in ("X", "Z")}
    return science | controls


def assess(rows, minimum_count):
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    required = set(contract["required_columns"])
    expected = required_cells()
    counts, sys_sums, env_sums, corr_sums = Counter(), Counter(), Counter(), Counter()
    keys, epochs, ports, phases, schedules = set(), set(), set(), set(), set()
    block_cells, positions, cell_positions = defaultdict(Counter), defaultdict(set), defaultdict(Counter)
    complete = True
    for row in rows:
        complete &= required <= set(row) and all(row[name] != "" for name in required)
        if row["trial_key"] in keys:
            complete = False
        keys.add(row["trial_key"])
        cell = row["mode"], row["input_probe"], row["system_basis"], row["environment_basis"]
        if cell not in expected:
            complete = False
            continue
        try:
            s, e = int(row["system_outcome"]), int(row["environment_outcome"])
            pos = int(row["within_block_position"])
            assert s in (-1, 1) and e in (-1, 1)
        except (ValueError, AssertionError):
            complete = False
            continue
        block = row["acquisition_block"]
        block_cells[block][cell] += 1; positions[block].add(pos); cell_positions[cell][pos] += 1
        counts[cell] += 1; sys_sums[cell] += s; env_sums[cell] += e; corr_sums[cell] += s * e
        epochs.add(row["acquisition_epoch"]); ports.add(row["environment_port_manifest"])
        phases.add(row["phase_reference_key"]); schedules.add(row["sealed_schedule_key"])
    all_cells = set(counts) == expected
    blocks = bool(block_cells) and all(set(v) == expected and set(v.values()) == {1} and
                                       positions[k] == set(range(40)) for k, v in block_cells.items())
    balanced = all_cells and all(set(v) == set(range(40)) and len(set(v.values())) == 1
                                 for v in cell_positions.values())
    enough = all_cells and all(counts[c] >= minimum_count for c in expected)
    mean = lambda table, c: F(table[c], counts[c])
    ix = ("identical_marker", "D", "X", "X")
    ox = ("orthogonal_marker", "D", "X", "X")
    iz = ("identical_marker", "D", "Z", "Z")
    oz = ("orthogonal_marker", "D", "Z", "Z")
    env_separation = abs(mean(corr_sums, ix) - mean(corr_sums, ox)) if all_cells else None
    population_difference = abs(mean(sys_sums, iz) - mean(sys_sums, oz)) if all_cells else None
    gates = {
        "raw_joint_records_complete_and_unique": complete,
        "one_acquisition_epoch_port_phase_and_schedule": len(epochs) == len(ports) == len(phases) == len(schedules) == 1,
        "all_forty_tomography_and_control_cells_present": all_cells,
        "every_block_is_complete_forty_cell_permutation": blocks,
        "every_cell_is_uniform_over_block_position": balanced,
        "minimum_attempted_counts_pass": enough,
        "system_population_control_is_blind": population_difference is not None and population_difference <= F(1, 20),
        "environment_port_control_separates_markers": env_separation is not None and env_separation >= F(1, 2),
    }
    return {"accepted": all(gates.values()), "gates": gates,
            "attempted_trial_count": sum(counts.values()),
            "environment_control_separation": str(env_separation) if env_separation is not None else None,
            "system_population_control_difference": str(population_difference) if population_difference is not None else None}


def main():
    parser = argparse.ArgumentParser(); parser.add_argument("input_csv", type=Path)
    parser.add_argument("--output", type=Path, required=True); args = parser.parse_args()
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    with args.input_csv.open(newline="", encoding="utf-8") as handle:
        result = assess(csv.DictReader(handle), contract["minimum_attempted_trials_per_cell"])
    result["schema"] = "marici.aspect.environment-port-tomography-run-analysis.v1"
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True)); raise SystemExit(0 if result["accepted"] else 1)


if __name__ == "__main__": main()
