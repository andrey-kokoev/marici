from fractions import Fraction as F
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "bell_no_click_efficiency_gate.json"


def exact_test(gamma, eta):
    # With every no-click assigned +1 and unbiased detected outcomes,
    # S/2 = sqrt(2)*gamma*eta^2 + (1-eta)^2.
    # The radical-free violation test is valid because both sides are positive.
    lhs_squared = 2 * gamma * gamma * eta ** 4
    rhs_squared = (2 * eta - eta * eta) ** 2
    return {
        "gamma": str(gamma), "eta": str(eta),
        "lhs_squared": str(lhs_squared), "rhs_squared": str(rhs_squared),
        "bell_violation": lhs_squared > rhs_squared,
    }


def main():
    cases = {
        "ideal_gamma_eta_4_5": exact_test(F(1), F(4, 5)),
        "ideal_gamma_eta_5_6": exact_test(F(1), F(5, 6)),
        "gamma_4_5_eta_9_10": exact_test(F(4, 5), F(9, 10)),
        "gamma_4_5_eta_19_20": exact_test(F(4, 5), F(19, 20)),
    }
    assert not cases["ideal_gamma_eta_4_5"]["bell_violation"]
    assert cases["ideal_gamma_eta_5_6"]["bell_violation"]
    assert not cases["gamma_4_5_eta_9_10"]["bell_violation"]
    assert cases["gamma_4_5_eta_19_20"]["bell_violation"]

    out = {
        "schema": "marici.aspect.bell-no-click-efficiency-gate.v1",
        "status": "pass", "cases": cases,
        "observed_chsh_law": "S/2 = sqrt(2)*gamma*eta^2 + (1-eta)^2",
        "exact_violation_gate": "2*gamma^2*eta^4 > (2*eta-eta^2)^2",
        "equivalent_threshold": "eta > 2/(1+sqrt(2)*gamma)",
        "outcome_rule": "each herald is retained and every no-click is assigned +1 before settings are opened",
        "result": "gamma=4/5 requires efficiency above about 0.938; eta=9/10 fails and eta=19/20 passes",
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
