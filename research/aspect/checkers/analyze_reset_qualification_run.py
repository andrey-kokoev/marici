import argparse
import csv
from collections import Counter, defaultdict
from fractions import Fraction as F
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT_PATH = ROOT / "contracts" / "reset-qualification-acquisition.v1.json"
TREATMENTS = ("L1", "R2", "L2", "R1")
ARMS = ("five_empty_bin_reset", "no_reset_control")


def proportion(total, count):
    return F(total, count) if count else None


def assess(rows, minimum_count):
    required = set(json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))["required_columns"])
    counts, target_sums, monitor_sums = Counter(), Counter(), Counter()
    keys, epochs = set(), set()
    block_cells, block_positions, cell_positions, schedule_keys = defaultdict(Counter), defaultdict(set), defaultdict(Counter), set()
    complete_records = True
    reset_settings = True
    failures_retained = 0
    for row in rows:
        complete_records &= required <= set(row) and all(row[name] != "" for name in required)
        key = row["trial_key"]
        if key in keys:
            complete_records = False
        keys.add(key)
        arm, predecessor, target = row["arm"], row["predecessor"], row["target"]
        if arm not in ARMS or predecessor not in TREATMENTS or target not in TREATMENTS:
            complete_records = False
            continue
        expected_reset = "empty,empty,empty,empty,empty" if arm == ARMS[0] else "none"
        reset_settings &= row["reset_setting"] == expected_reset
        cell = arm, predecessor, target
        block = row["acquisition_block"]
        block_cells[block][cell] += 1
        try:
            position = int(row["within_block_position"])
        except ValueError:
            complete_records = False
            position = -1
        block_positions[block].add(position)
        cell_positions[cell][position] += 1
        schedule_keys.add(row["sealed_schedule_key"])
        counts[cell] += 1
        target_sums[cell] += int(row["target_outcome"])
        monitor_sums[cell] += int(row["reset_monitor_outcome"])
        failures_retained += int(row["reset_failure"])
        epochs.add(row["qualification_epoch"])

    expected_cells = {(a, p, t) for a in ARMS for p in TREATMENTS for t in TREATMENTS}
    complete_cells = set(counts) == expected_cells
    complete_blocks = bool(block_cells) and all(
        set(cell_counts) == expected_cells and set(cell_counts.values()) == {1}
        and block_positions[block] == set(range(32))
        for block, cell_counts in block_cells.items()
    )
    position_balanced = complete_cells and all(
        set(position_counts) == set(range(32)) and len(set(position_counts.values())) == 1
        for position_counts in cell_positions.values()
    )
    enough = complete_cells and all(counts[cell] >= minimum_count for cell in expected_cells)
    means = {cell: proportion(target_sums[cell], counts[cell]) for cell in expected_cells if counts[cell]}
    monitors = {cell: proportion(monitor_sums[cell], counts[cell]) for cell in expected_cells if counts[cell]}

    def max_spread(table, arm):
        return max(max(table[arm, p, t] for p in TREATMENTS) -
                   min(table[arm, p, t] for p in TREATMENTS) for t in TREATMENTS)

    target_spread = max_spread(means, ARMS[0]) if complete_cells else None
    monitor_spread = max_spread(monitors, ARMS[0]) if complete_cells else None
    control_spread = max_spread(means, ARMS[1]) if complete_cells else None
    gates = {
        "raw_records_complete_and_trial_keys_unique": complete_records,
        "one_qualification_epoch": len(epochs) == 1,
        "all_thirty_two_arm_predecessor_target_cells_present": complete_cells,
        "every_acquisition_block_is_a_complete_32_cell_permutation": complete_blocks,
        "every_cell_is_uniformly_balanced_over_32_block_positions": position_balanced,
        "one_sealed_schedule_key": len(schedule_keys) == 1,
        "minimum_attempted_counts_pass": enough,
        "five_empty_bin_sequences_are_literal": reset_settings,
        "reset_target_response_is_predecessor_invariant": target_spread is not None and target_spread <= F(1, 20),
        "reset_monitor_is_predecessor_invariant": monitor_spread is not None and monitor_spread <= F(1, 20),
        "no_reset_control_is_memory_sensitive": control_spread is not None and control_spread >= F(1, 10),
    }
    return {
        "accepted": all(gates.values()), "gates": gates,
        "attempted_trial_count": sum(counts.values()),
        "recorded_reset_failure_count": failures_retained,
        "maximum_reset_target_predecessor_spread": str(target_spread) if target_spread is not None else None,
        "maximum_reset_monitor_predecessor_spread": str(monitor_spread) if monitor_spread is not None else None,
        "maximum_no_reset_target_predecessor_spread": str(control_spread) if control_spread is not None else None,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_csv", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    contract = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))
    with args.input_csv.open(newline="", encoding="utf-8") as handle:
        result = assess(csv.DictReader(handle), contract["minimum_attempted_trials_per_arm_predecessor_target_cell"])
    result["schema"] = "marici.aspect.reset-qualification-run-analysis.v1"
    result["input"] = str(args.input_csv)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))
    raise SystemExit(0 if result["accepted"] else 1)


if __name__ == "__main__":
    main()
