from fractions import Fraction as F
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "reset_insertion_associator_falsifier.json"


def main():
    direct_without_reset = [F(3, 5), F(0), F(-3, 5), F(0)]
    # A hidden reset-native three-body phase of pi flips the ternary curve.
    direct_with_reset = [-value for value in direct_without_reset]
    left_with_reset = list(direct_with_reset)
    right_with_reset = list(direct_with_reset)
    destructive_with_reset = [F(0)] * 4
    zero_coherence_with_reset = [F(0)] * 4
    associator = [left - right for left, right in zip(left_with_reset, right_with_reset)]
    assert associator == [F(0)] * 4
    assert destructive_with_reset == zero_coherence_with_reset == [F(0)] * 4
    assert direct_with_reset != direct_without_reset
    out = {
        "schema": "marici.aspect.reset-insertion-associator-falsifier.v1", "status": "pass",
        "direct_without_reset": [str(x) for x in direct_without_reset],
        "direct_with_reset": [str(x) for x in direct_with_reset],
        "left_with_reset": [str(x) for x in left_with_reset],
        "right_with_reset": [str(x) for x in right_with_reset],
        "associator_with_reset": [str(x) for x in associator],
        "destructive_control_with_reset": [str(x) for x in destructive_with_reset],
        "zero_coherence_control_with_reset": [str(x) for x in zero_coherence_with_reset],
        "naive_associator_null_passes": True,
        "reset_insertion_transport_passes": False,
        "required_gate": "direct ternary curve with reset equals the independently calibrated direct ternary curve without reset",
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
