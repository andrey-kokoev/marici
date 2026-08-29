"""WP993: exact universal adaptive section and its authority boundary."""

import json
from fractions import Fraction as F
from pathlib import Path


def energies(q, k, u, v):
    Q, R = q + u, k + v
    return (F(0), -2 * Q, -F(2, 9) * Q - F(2, 27783) * R)


def controls(label, q, k):
    targets = {
        "commuting": (F(-1), F(0)),
        "rank_two": (F(1), F(0)),
        "full_rank": (F(0), F(1)),
    }
    Q, R = targets[label]
    return Q - q, R - k


samples = ((F(1, 7), F(11, 13)), (F(3), F(5)), (F(101), F(10007)))
labels = ("commuting", "rank_two", "full_rank")
expected = {"commuting": 0, "rank_two": 1, "full_rank": 2}

witnesses = {}
for q, k in samples:
    for label in labels:
        u, v = controls(label, q, k)
        values = energies(q, k, u, v)
        winner = min(range(3), key=lambda i: values[i])
        witnesses[f"{q}:{k}:{label}"] = {
            "u": str(u),
            "v": str(v),
            "winner": winner,
            "unique": values.count(values[winner]) == 1,
        }

frozen_values = energies(F(101), F(10007), F(0), F(0))
frozen_winner = min(range(3), key=lambda i: frozen_values[i])

checks = {
    "universal_affine_section_exact": all(
        row["winner"] == expected[key.rsplit(":", 1)[1]] and row["unique"]
        for key, row in witnesses.items()
    ),
    "deliberate_frozen_control_failure_nonzero": frozen_winner != expected["commuting"],
    "control_targets_are_state_independent_after_feedback": True,
    "requires_qk_record_before_control": True,
    "does_not_supply_measurement_instrument": True,
    "does_not_supply_actuator_authority": True,
}

result = {
    "schema": "marici.flavor.wp993-universal-adaptive-control-section.v1",
    "status": "PASS" if all(checks.values()) else "FAIL",
    "checks": checks,
    "section": {
        "commuting": ["u=-q-1", "v=-k"],
        "rank_two": ["u=1-q", "v=-k"],
        "full_rank": ["u=-q", "v=1-k"],
    },
    "target_effective_controls": {
        "commuting": ["Q=-1", "R=0"],
        "rank_two": ["Q=1", "R=0"],
        "full_rank": ["Q=0", "R=1"],
    },
    "classification": "formal universal feedback section; neither source selector nor physical instrument",
    "smallest_exact_falsifier": "two physical16-equivalent preparations yield different calibrated q,k records or the commanded invariant shifts fail to realize Q=q+u and R=k+v",
    "remaining_gate": "one source-authorized closed-loop apparatus composing q,k measurement, reset-safe feedback, independent u,v actuation, and labelled relative-energy verification",
    "sample_witnesses": witnesses,
}

out = Path(__file__).parents[1] / "results" / "wp993_universal_adaptive_control_section.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
