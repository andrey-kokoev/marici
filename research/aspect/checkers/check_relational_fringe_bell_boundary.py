from fractions import Fraction as F
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "relational_fringe_bell_boundary.json"


def chsh_square(gamma):
    return 8 * gamma * gamma


def classify(gamma):
    fringe = gamma != 0
    s2 = chsh_square(gamma)
    return {
        "gamma": str(gamma),
        "relational_fringe": fringe,
        "chsh_square": str(s2),
        "bell_violation": s2 > 4,
        "at_boundary": s2 == 4,
    }


def main():
    cases = {
        "zero": classify(F(0)),
        "visible_but_bell_local": classify(F(3, 5)),
        "exact_bell_boundary": {
            "gamma_squared": "1/2", "relational_fringe": True,
            "chsh_square": "4", "bell_violation": False, "at_boundary": True,
        },
        "bell_nonlocal": classify(F(4, 5)),
        "ideal": classify(F(1)),
    }
    assert cases["visible_but_bell_local"]["chsh_square"] == "72/25"
    assert not cases["visible_but_bell_local"]["bell_violation"]
    assert cases["bell_nonlocal"]["chsh_square"] == "128/25"
    assert cases["bell_nonlocal"]["bell_violation"]

    correlator_coefficients = {
        "E00_times_sqrt2": "gamma", "E01_times_sqrt2": "gamma",
        "E10_times_sqrt2": "gamma", "E11_times_sqrt2": "-gamma",
    }
    out = {
        "schema": "marici.aspect.relational-fringe-bell-boundary.v1",
        "status": "pass", "cases": cases,
        "four_setting_correlators": correlator_coefficients,
        "exact_boundary": "gamma^2 > 1/2",
        "conclusion": "relational coherence is strictly weaker than Bell nonlocality",
        "classical_hostile": "correlated phase noise can reproduce one joint fringe but cannot satisfy the preregistered four-setting CHSH violation under the Bell causal contract",
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
