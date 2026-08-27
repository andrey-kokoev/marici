from fractions import Fraction as F
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "within_block_position_confounder.json"


def spread(values):
    return max(values) - min(values)


def main():
    true_response = F(1, 5)
    position_effect = [F(i, 10) for i in range(4)]
    # Fixed positions alias predecessor labels to warm-up position.
    fixed_reset = [true_response] * 4
    fixed_control = [true_response + effect for effect in position_effect]
    # Four cyclic rotations give every predecessor every position once.
    balanced_value = true_response + sum(position_effect) / 4
    rotated_reset = [balanced_value] * 4
    rotated_control = [balanced_value] * 4
    assert spread(fixed_reset) == 0
    assert spread(fixed_control) == F(3, 10)
    assert spread(rotated_reset) == spread(rotated_control) == 0
    out = {
        "schema": "marici.aspect.within-block-position-confounder.v1", "status": "pass",
        "true_predecessor_memory": "0",
        "fixed_order_reset_spread": "0",
        "fixed_order_control_false_spread": "3/10",
        "fixed_complete_blocks_would_accept": True,
        "position_balanced_reset_spread": "0",
        "position_balanced_control_spread": "0",
        "position_balanced_qualification_accepts": False,
        "repair": "cycle the 32-cell permutation so every cell occupies every within-block position equally often",
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
