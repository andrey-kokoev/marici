from fractions import Fraction as F
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "reset_depth_law_falsifier.json"


def main():
    r = F(16, 25)
    extra = F(1, 2)
    amplitude = F(9, 25)
    two_state = [amplitude * r ** k for k in range(11)]
    two_mode = [amplitude * (r ** k + extra ** k) / 2 for k in range(11)]
    two_state_ratios = [two_state[k + 1] / two_state[k] for k in range(10)]
    two_mode_ratios = [two_mode[k + 1] / two_mode[k] for k in range(10)]
    assert set(two_state_ratios) == {r}
    assert any(value != r for value in two_mode_ratios)
    residuals = [two_mode[k + 1] - r * two_mode[k] for k in range(10)]
    assert any(residual != 0 for residual in residuals)
    out = {
        "schema": "marici.aspect.reset-depth-law-falsifier.v1", "status": "pass",
        "depths": list(range(11)),
        "two_state_spreads": [str(x) for x in two_state],
        "two_state_ratios": [str(x) for x in two_state_ratios],
        "hostile_two_mode_spreads": [str(x) for x in two_mode],
        "hostile_two_mode_ratios": [str(x) for x in two_mode_ratios],
        "geometric_residuals": [str(x) for x in residuals],
        "frozen_ratio": "16/25",
        "extra_memory_mode_detected": True,
        "required_gate": "all depth-0-through-10 recurrence residuals are null within frozen simultaneous bounds",
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
