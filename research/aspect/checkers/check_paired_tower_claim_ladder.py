from fractions import Fraction as F
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "paired_tower_claim_ladder.json"


def detector_bell(gamma, eta):
    return 2 * gamma * gamma * eta ** 4 > (2 * eta - eta * eta) ** 2


def classify(name, gamma, eta, phase_covariance, coherent_sewing,
             local_flat=True, bell_causal_contract=True):
    relational = gamma != 0 and coherent_sewing and local_flat
    correlated_environment = phase_covariance != 0
    ideal_bell_eligible = gamma * gamma > F(1, 2)
    complete_bell = (
        relational and ideal_bell_eligible and detector_bell(gamma, eta)
        and bell_causal_contract and not correlated_environment
    )
    if complete_bell:
        strongest = "detector_complete_bell_nonlocality"
    elif relational and correlated_environment:
        strongest = "relational_environment_channel"
    elif ideal_bell_eligible and relational:
        strongest = "relational_coherence_with_ideal_bell_eligibility"
    elif relational:
        strongest = "relational_coherence"
    else:
        strongest = "no_relational_claim"
    return {
        "name": name, "gamma": str(gamma), "eta": str(eta),
        "phase_covariance": str(phase_covariance),
        "relational_coherence": relational,
        "correlated_environment": correlated_environment,
        "ideal_bell_eligible": ideal_bell_eligible,
        "detector_complete_bell_nonlocality": complete_bell,
        "strongest_admitted_claim": strongest,
    }


def main():
    cases = [
        classify("visible_bell_local", F(3, 5), F(19, 20), F(0), True),
        classify("ideal_eligible_detector_incomplete", F(4, 5), F(9, 10), F(0), True),
        classify("complete_bell", F(4, 5), F(19, 20), F(0), True),
        classify("correlated_environment", F(1), F(1), F(1), True),
        classify("classical_join", F(1), F(1), F(0), False),
    ]
    by_name = {case["name"]: case for case in cases}
    assert by_name["visible_bell_local"]["strongest_admitted_claim"] == "relational_coherence"
    assert by_name["ideal_eligible_detector_incomplete"]["strongest_admitted_claim"] == "relational_coherence_with_ideal_bell_eligibility"
    assert by_name["complete_bell"]["detector_complete_bell_nonlocality"]
    assert by_name["correlated_environment"]["strongest_admitted_claim"] == "relational_environment_channel"
    assert by_name["classical_join"]["strongest_admitted_claim"] == "no_relational_claim"

    implications = {
        "detector_complete_bell_nonlocality_implies_relational_coherence": all(
            not c["detector_complete_bell_nonlocality"] or c["relational_coherence"] for c in cases),
        "relational_coherence_does_not_imply_bell_nonlocality": (
            by_name["visible_bell_local"]["relational_coherence"]
            and not by_name["visible_bell_local"]["detector_complete_bell_nonlocality"]),
        "ideal_bell_eligibility_does_not_imply_observed_violation": (
            by_name["ideal_eligible_detector_incomplete"]["ideal_bell_eligible"]
            and not by_name["ideal_eligible_detector_incomplete"]["detector_complete_bell_nonlocality"]),
        "joint_fringe_does_not_exclude_correlated_environment": (
            by_name["correlated_environment"]["relational_coherence"]
            and by_name["correlated_environment"]["correlated_environment"]),
    }
    assert all(implications.values())
    out = {
        "schema": "marici.aspect.paired-tower-claim-ladder.v1",
        "status": "pass", "cases": cases, "logical_checks": implications,
        "claim_poset": {
            "environment_branch": ["relational_environment_channel"],
            "coherent_constructor_branch": [
                "relational_coherence",
                "relational_coherence_with_ideal_bell_eligibility",
                "detector_complete_bell_nonlocality"
            ],
            "incomparability": "a correlated environment channel is not ordered against source-authorized coherent sewing without an additional intervention",
        },
        "decision_rule": "report only the strongest claim whose source, sewing, covariance, causal, and detector gates all pass",
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
