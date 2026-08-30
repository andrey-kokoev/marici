from fractions import Fraction as F
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "reset_drift_confounder.json"


def spread(values):
    return max(values) - min(values)


def main():
    true_response = F(1, 5)
    drift = [F(0), F(1, 10), F(2, 10), F(3, 10)]
    grouped_reset = [true_response] * 4
    grouped_control = [true_response + value for value in drift]
    # In a complete-block schedule, every cell samples every drift level equally.
    common_block_mean = true_response + sum(drift) / 4
    blocked_reset = [common_block_mean] * 4
    blocked_control = [common_block_mean] * 4
    assert spread(grouped_reset) == 0
    assert spread(grouped_control) == F(3, 10)
    assert spread(blocked_reset) == spread(blocked_control) == 0
    out = {
        "schema": "marici.aspect.reset-drift-confounder.v1", "status": "pass",
        "true_predecessor_memory": "0",
        "grouped_reset_predecessor_spread": str(spread(grouped_reset)),
        "grouped_control_false_predecessor_spread": str(spread(grouped_control)),
        "naive_qualification_would_accept": True,
        "complete_block_reset_predecessor_spread": str(spread(blocked_reset)),
        "complete_block_control_predecessor_spread": str(spread(blocked_control)),
        "complete_block_qualification_accepts": False,
        "reason_for_correct_rejection": "the no-reset arm does not demonstrate memory sensitivity after drift balance",
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
