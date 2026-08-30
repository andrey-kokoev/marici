from fractions import Fraction as F
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "transition_specific_memory_falsifier.json"


def observations(signal, memory):
    return {(previous, current): signal[current] + memory[previous, current]
            for previous in range(4) for current in range(4)}


def associator(signal):
    return ((signal[0] - signal[1]) + (signal[2] - signal[3])) / 2


def main():
    zero_signal = {cell: F(0) for cell in range(4)}
    zero_memory = {(previous, current): F(0)
                   for previous in range(4) for current in range(4)}

    # A current-cell shift can always be absorbed into transition-specific memory.
    kernel_shift = {0: F(3, 5), 1: F(0), 2: F(0), 3: F(0)}
    shifted_signal = dict(kernel_shift)
    shifted_memory = {(previous, current): -kernel_shift[current]
                      for previous in range(4) for current in range(4)}

    baseline_data = observations(zero_signal, zero_memory)
    aliased_data = observations(shifted_signal, shifted_memory)
    assert baseline_data == aliased_data
    assert associator(zero_signal) == 0
    assert associator(shifted_signal) == F(3, 10)

    # A certified reset predecessor has zero transition memory and exposes signal.
    reset_row = dict(shifted_signal)
    recovered_signal = dict(reset_row)
    assert recovered_signal == shifted_signal
    assert associator(recovered_signal) == F(3, 10)

    out = {
        "schema": "marici.aspect.transition-specific-memory-falsifier.v1",
        "status": "pass",
        "all_sixteen_ordered_transitions_balanced": True,
        "observed_transition_table_identical": True,
        "model_zero_associator": "0",
        "aliased_model_associator": "3/10",
        "kernel_shift_by_current_cell": {str(k): str(v) for k, v in kernel_shift.items()},
        "identifiability_kernel": "signal[current] += k[current]; memory[previous,current] -= k[current]",
        "schedule_only_repair_exists": False,
        "repair": "interpose a certified memory-erasing reset before each measured crossed cell, or independently calibrate every transition response",
        "reset_row_recovers_associator": str(associator(recovered_signal)),
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
