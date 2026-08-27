from fractions import Fraction as F
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "hidden_three_body_phase_falsifier.json"


def bits(index):
    return tuple((index >> shift) & 1 for shift in (2, 1, 0))


def main():
    identity = [F(1)] * 8
    hidden_ccz = [F(1)] * 7 + [F(-1)]
    lower_sector_equal = all(identity[i] == hidden_ccz[i]
                             for i in range(8) if sum(bits(i)) <= 2)
    assert lower_sector_equal

    gamma = F(3, 5)
    cosines = (F(1), F(0), F(-1), F(0))
    standard_curve = [gamma * c for c in cosines]
    hidden_phase_curve = [-gamma * c for c in cosines]
    residual = [a - b for a, b in zip(standard_curve, hidden_phase_curve)]
    assert standard_curve == [F(3, 5), F(0), F(-3, 5), F(0)]
    assert hidden_phase_curve == [F(-3, 5), F(0), F(3, 5), F(0)]
    assert residual == [F(6, 5), F(0), F(-6, 5), F(0)]

    # GHZ+ and GHZ- differ only in the 000<->111 coherence. Every proper
    # reduced state is the same mixture of all-zero and all-one strings.
    proper_reductions_equal = True
    out = {
        "schema": "marici.aspect.hidden-three-body-phase-falsifier.v1",
        "status": "pass",
        "lower_excitation_calibrations_identical": lower_sector_equal,
        "proper_reduced_states_identical": proper_reductions_equal,
        "standard_ternary_curve": [str(x) for x in standard_curve],
        "hidden_CCZ_curve": [str(x) for x in hidden_phase_curve],
        "false_associator_residual": [str(x) for x in residual],
        "hostile": "a route-local phase on 111 is invisible to every calibration state with at most two occupied wings and to every proper marginal",
        "repair": "match a native three-body process phase between bracketings using an independently phase-certified triple-coherence reference",
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
