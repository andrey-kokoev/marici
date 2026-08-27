from fractions import Fraction as F
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "three_wing_associator_prediction.json"


def main():
    gamma = F(3, 5)
    cosines = (F(1), F(0), F(-1), F(0))
    sines = (F(0), F(1), F(0), F(-1))

    direct = [gamma * c for c in cosines]
    left_bracket = list(direct)
    right_bracket_standard = list(direct)
    associator_standard = [a - b for a, b in zip(left_bracket, right_bracket_standard)]

    # Deliberate higher-phase hostile: right bracketing acquires omega=pi/2.
    right_bracket_quarter_turn = [-gamma * s for s in sines]
    associator_hostile = [a - b for a, b in zip(left_bracket, right_bracket_quarter_turn)]

    assert direct == [F(3, 5), F(0), F(-3, 5), F(0)]
    assert associator_standard == [F(0)] * 4
    assert right_bracket_quarter_turn == [F(0), F(-3, 5), F(0), F(3, 5)]
    assert associator_hostile == [F(3, 5), F(3, 5), F(-3, 5), F(-3, 5)]

    # GHZ coherence changes only the 000<->111 off-diagonal. Tracing out any
    # nonempty wing kills it, so every proper phase-sensitive marginal is zero.
    proper_phase_marginals = {
        "A": [F(0)] * 4, "B": [F(0)] * 4, "C": [F(0)] * 4,
        "AB": [F(0)] * 4, "AC": [F(0)] * 4, "BC": [F(0)] * 4,
    }
    assert all(all(x == 0 for x in curve) for curve in proper_phase_marginals.values())

    out = {
        "schema": "marici.aspect.three-wing-associator-prediction.v1",
        "status": "pass", "gamma": str(gamma),
        "proper_phase_sensitive_marginals": {
            key: [str(x) for x in curve] for key, curve in proper_phase_marginals.items()
        },
        "direct_ternary_curve": [str(x) for x in direct],
        "left_bracket_curve": [str(x) for x in left_bracket],
        "right_bracket_standard_curve": [str(x) for x in right_bracket_standard],
        "standard_associator_residual": [str(x) for x in associator_standard],
        "quarter_turn_higher_phase_fixture": {
            "right_curve": [str(x) for x in right_bracket_quarter_turn],
            "associator_residual": [str(x) for x in associator_hostile],
        },
        "prediction": "ordinary coherent composition gives zero bracketing residual while direct ternary visibility is 3/5 and all proper phase marginals are zero",
        "discovery_channel": "a reproducible nonzero left-minus-right curve after matched transfer-matrix, loss, phase, and timing calibration",
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
